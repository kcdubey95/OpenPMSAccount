import re
from datetime import datetime
import logging
from flask import Blueprint, render_template, redirect, url_for, session, make_response, flash, request, jsonify
from reportlab.lib.pagesizes import letter

from controllers.user import add_user_mobile, update_user_stepone, update_user_steptwo, update_user_stepthree, \
    get_all_accont_data, get_user_data, rollback_db, update_user_step
import sys
from models.user import Open_Account, Occupation_Master, Relation_Master
from reportlab.pdfgen import canvas
from io import BytesIO
main = Blueprint('main', __name__)
logging.basicConfig(filename="logfile.log",level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@main.route("/")
def mobile_no():
    session.pop('mobile_no', None)
    return render_template("mobile.html")


@main.route("/mob-validate", methods=["POST"])
def mobile_validate():
    try:
        session.pop('mobile_no', None)
        mobile_no = request.form.get('mob')

        if not re.match(r'^\d{10}$', mobile_no):
            flash("Invalid mobile number. Please enter a 10-digit phone number.", "danger")
            return redirect(request.url)
        data = get_user_data(mobile_no)

        if data:
            print("step1111")
            session['mobile_no'] = data[0]['mobile_no']
            step = data[0]['step']
            routes = {
                1: "/step1",
                2: "/step2",
                3: "/step3",
                4: "/preview"
            }
            redirect_url = routes.get(step)
            if redirect_url:
                return redirect(redirect_url)
        elif mobile_no:
            print("step222")
            session['mobile_no'] = mobile_no
            data1 = add_user_mobile(mobile_no)

            session['mobile_no'] = data1.get("mobile_no")
            logging.info("Mobile step performed successfully.")
            return redirect(url_for("main.step1"))
        else:

            return redirect("/")
    except ValueError as e:
        print(f"Error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Error: {e}", "danger")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Duplicate Mobile entry", "danger")
    return redirect("/")


@main.route("/step1")
def step1():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        data = get_all_accont_data(mobile_no)

        if data:
            step = data[0].get('step')
            routes = {
                1: "step1.html",
                2: "/step2",
                3: "/step3",
                4: "/preview"
            }
            if step == 1:
                return render_template("step1.html", data=data)
            else:
                redirect_url = routes.get(step)
            if redirect_url:
                return redirect(redirect_url)
            return render_template("step1.html", data=data)
        else:
            return render_template("step1.html", data=[])
    else:
        return redirect("/")


@main.route("/step-one-validate", methods=["POST"])
def step_one_validate():
    try:
        if 'mobile_no' in session:
            mobile_no = session['mobile_no']
            fname = request.form.get('fname').strip()
            lname = request.form.get('lname').strip()
            email = request.form.get('email').strip()

            if not fname or not re.match(r"^[A-Za-z]+$", fname):
                flash("Please enter a valid first name (only alphabets allowed).", "danger")
                return redirect(url_for("main.step1"))
            if not lname or not re.match(r"^[A-Za-z]+$", lname):
                flash("Please enter a valid last name (only alphabets allowed).", "danger")
                return redirect(url_for("main.step1"))

            if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                flash("Please enter a valid email address.", "danger")
                return redirect(url_for("main.step1"))

            users = Open_Account.get_user_data(mobile_no=mobile_no)
            if not users or len(users) == 0:
                flash("User not found.", "danger")
                return redirect(url_for("main.step1"))

            user = users[0]  # Assuming you want to update the first user in the list
            update_user_stepone(user, fname, lname, email)

            logging.info("Step1 performed successfully.")
            return redirect(url_for("main.step2"))
        else:
            return redirect("/step2")
    except ValueError as e:
        print(f"Error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Error:Invalid Input", "danger")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Unexpected error: Invalid email", "danger")
    return redirect(url_for("main.step1"))


@main.route("/step2")
def step2():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        data = get_all_accont_data(mobile_no)
        oc_list = Occupation_Master.get_all()
        if data :
            step = data[0].get('step')
            routes = {
                1: "/step1",
                2: "step2.html",
                3: "/step3",
                4: "/preview"
            }
            if step == 2:
                return render_template("step2.html", data=data, oc_list=oc_list)
            else:
                redirect_url = routes.get(step)
            if redirect_url:
                return redirect(redirect_url)
            return render_template("step2.html", oc_list=oc_list, data=data)
        return render_template("step2.html", oc_list=oc_list, data=[])
    else:
        return redirect("/")


@main.route("/step-two-validate", methods=["POST"])
def step_two_validate():
    try:
        if 'mobile_no' in session:
            mobile_no = session['mobile_no']
            fullname = request.form.get('fullname').strip()
            gender = request.form.get('gender').strip()
            dob = request.form.get('dob').strip()
            address = request.form.get('address').strip()
            income = request.form.getlist('income')
            occupation = request.form.get('occupation').strip()

            if not fullname or not re.match(r"^[A-Za-z\s]+$", fullname):
                flash("Please enter a valid full name (only alphabets allowed).", "danger")
                return redirect(url_for("main.step2"))

            if gender not in ['Male', 'Female', 'transgender']:
                flash("Please select a valid gender.", "danger")
                return redirect(url_for("main.step2"))

            try:
                datetime.strptime(dob, '%d/%m/%Y')
            except ValueError:
                flash("Please enter a valid date of birth.", "danger")
                return redirect(url_for("main.step2"))

            if not address:
                flash("Please enter your address.", "danger")
                return redirect(url_for("main.step2"))

            if not income:
                flash("Please select at least one income range.", "danger")
                return redirect(url_for("main.step2"))

            if occupation == 'Select Occupation':
                flash("Please select a valid occupation.", "danger")
                return redirect(url_for("main.step2"))

            users = Open_Account.get_user_data(mobile_no=mobile_no)
            if not users or len(users) == 0:
                flash("User not found.", "danger")
                return redirect(url_for("main.step2"))

            user = users[0]  # Assuming you want to update the first user in the list
            update_user_steptwo(user, fullname, gender, dob, address, income, occupation)

            logging.info("Step2 performed successfully.")
            return redirect(url_for("main.step3"))
        else:
            return redirect("/")
    except ValueError as e:
        print(f"Error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Fill The Data", "danger")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Fill The Data", "danger")
    return redirect(url_for("main.step2"))


@main.route("/step3")
def step3():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        data = get_all_accont_data(mobile_no)
        r_list = Relation_Master.get_all()
        if data:
            step = data[0].get('step')
            routes = {
                1: "/step1",
                2: "/step2",
                3: "step3.html",
                4: "/preview"
            }
            if step == 3:
                return render_template("step3.html", data=data,r_list=r_list)
            else:
                redirect_url = routes.get(step)
            if redirect_url:
                return redirect(redirect_url)
    else:
        return redirect("/")

    return render_template("step3.html", r_list=r_list, data=data)


@main.route("/step-three-validate", methods=["POST"])
def step_three_validate():
    try:
        if 'mobile_no' in session:
            mobile_no = session['mobile_no']
            users = Open_Account.get_user_data(mobile_no=mobile_no)  # Assuming this returns a list

            if not users or len(users) == 0:
                flash("User not found.", "danger")
                return redirect(url_for("main.step3"))

            user = users[0]  # Get the first user object from the list

            nfull_name = request.form.get('nfull_name', '').strip()
            dob = request.form.get('dob', '').strip()
            address = request.form.get('address', '').strip()
            phone = request.form.get('phone', '').strip()
            relation = request.form.get('relation', '').strip()

            if not nfull_name or not dob or not address or not phone or not relation:
                flash("All fields are required.", "danger")
                return redirect(url_for("main.step3"))

            if not phone.isdigit() or len(phone) != 10:
                flash("Phone number must be a valid 10-digit number.", "danger")
                return redirect(url_for("main.step3"))

            if relation == 'Select Relation':
                flash("Please select a valid relation.", "danger")
                return redirect(url_for("main.step3"))

            update_user_stepthree(user, nfull_name, dob, address, phone, relation)
            logging.info("Step3 performed successfully.")
            return redirect(url_for("main.preview"))
        else:
            return redirect("/")
    except ValueError as e:
        print(f"Error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Error: {e}", "danger")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.exception("Exception occurred: %s", str(e))
        flash(f"Unexpected error occurred.", "danger")
    return redirect(url_for("main.step3"))

@main.route("/preview")
def preview():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        data = get_all_accont_data(mobile_no)
        if data :
            step = data[0].get('step')
            routes = {
                1: "/step1",
                2: "/step2",
                3: "/step3",
                4: "preview.html"
            }
            if step == 4:
                return render_template("preview.html", data=data)
            else:
                redirect_url = routes.get(step)
            if redirect_url:
                return redirect(redirect_url)
        else:
            return redirect("/step1")
        return render_template("preview.html", data=data)
    else:
        return redirect("/")


@main.route('/generate_pdf')
def generate_pdf():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        results = get_all_accont_data(mobile_no)
        data = results[0]
        mobile_no = data['mobile_no']
        email = data['email']
        fname = data['fname']
        lname = data['lname']
        fullname = data['fullname']
        gender = data['gender']
        dob = data['dob']
        income_rang = data['income_rang']
        occupation = data['occupation']
        address = data['address']
        nfull_name = data['nfull_name']
        naddress = data['naddress']
        ndob = data['ndob']
        nmobile_no = data['nmobile_no']
        occupation_name = data['occupation_name']
        relation_name = data['relation_name']
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        p.setFont("Helvetica-Bold", 18)
        p.drawCentredString(width / 2.0, height - 50, "Account Preview")
        field_height = height - 120
        field_width = 350
        field_spacing = 40
        p.setFont("Helvetica-Bold", 12)

        fields = [
            ("First Name", fname),
            ("Last Name", lname),
            ("Mobile", mobile_no),
            ("Email", email),
            ("Full Name", fullname),
            ("Gender", gender),
            ("Date of Birth", dob),
            ("Address", address),
            ("Income", income_rang),
            ("Occupation", occupation_name),
            ("Nominee Full Name", nfull_name),
            ("Nominee Date of Birth", ndob),
            ("Nominee Address", naddress),
            ("Nominee Mobile No", nmobile_no),
            ("Nominee Relation", relation_name)
        ]

        for label, value in fields:
            p.drawString(70, field_height, f"{label} *")
            p.rect(200, field_height - 15, field_width, 20)
            p.setFont("Helvetica", 12)
            p.drawString(205, field_height - 10, value)
            field_height -= field_spacing
        p.showPage()
        p.save()
        buffer.seek(0)
        response = make_response(buffer.getvalue())
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename="account_preview.pdf"'
        return response
    else:
        return redirect("/")

@main.route("/terms-and-conditions")
def terms_conditions():
    return render_template("tc.html")


@main.route("/update-step", methods=["POST"])
def step_update():
    if 'mobile_no' in session:
        mobile_no = session['mobile_no']
        request_data = request.get_json()
        step = request_data['step']
        users = Open_Account.get_user_data(mobile_no=mobile_no)
        user = users[0]  # Assuming you want to update the first user in the list
        update_user_step(user, step)
        return jsonify({'status': 'success'})