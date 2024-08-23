from flask import Flask, render_template, make_response, redirect, request, url_for
from reportlab.pdfgen import canvas
from io import BytesIO
from models.open_accont_form import Mobile,Step_One,Step_Tow,Step_Three

app = Flask(__name__)


@app.route("/")
def mobile_no():
    return render_template("mobile.html")


@app.route("/mob-validate", methods=["POST"])
def mobile_validate():
    if request.method == "POST":
        mobile_number = request.form.get("mob")
        try:
            data = {'mobile': int(mobile_number)}
            op = Mobile.parse_obj(data)
            print(op.mobile)
            return redirect("/step1")
        except ValueError as e:
            print(f"Error: {e}")
        return redirect("/")


@app.route("/step1")
def step1():
    return render_template("step1.html")


@app.route("/step-one-validate", methods=["POST"])
def step_one_validate():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        try:
            data = {'fname': str(fname), 'lname': str(lname), 'email': str(email)}
            op = Step_One.parse_obj(data)
            # print(op.mobile)
            return redirect("/step2")
        except ValueError as e:
            print(f"Error: {e}")
        return redirect("/")


@app.route("/step2")
def step2():
    return render_template("step2.html")


@app.route("/step-two-validate", methods=["POST"])
def step_two_validate():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        gender = request.form.get("gender")
        dob = request.form.get("dob")
        address = request.form.get("address")
        income = request.form.get("income")
        occupation = request.form.get("occupation")
        try:
            data = {'fullname': str(fullname), 'gender': int(gender), 'dob': dob, 'income': int(income),
                    'occupation': int(occupation), 'address': address}
            op = Step_Tow.parse_obj(data)
            # print(op.mobile)
            return redirect("/step3")
        except ValueError as e:
            print(f"Error: {e}")
        return redirect("/")


@app.route("/step3")
def step3():
    return render_template("step3.html")


@app.route("/step-three-validate", methods=["POST"])
def step_three_validate():
    if request.method == "POST":
        nfull_name = request.form.get("nfull_name")
        dob = request.form.get("dob")
        address = request.form.get("address")
        phone = request.form.get("phone")
        relation = request.form.get("relation")
        try:
            data = {'nfull_name': str(nfull_name), 'address': str(address), 'dob': dob, 'phone': int(phone),
                    'relation': int(relation)}
            op = Step_Three.parse_obj(data)
            # print(op.mobile)
            return redirect("/step1")
        except ValueError as e:
            print(f"Error: {e}")
        return redirect("/")


@app.route("/preview")
def preview():
    return render_template("preview.html")


@app.route('/generate_pdf')
def generate_pdf():
    # Create a PDF in memory
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Add content to the PDF
    pdf.drawString(100, 750, "Hello, this is a PDF created with Flask and ReportLab!")

    # Finish the PDF
    pdf.showPage()
    pdf.save()

    # Move the buffer to the beginning so we can return it
    buffer.seek(0)

    # Send the PDF as a response
    response = make_response(buffer.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=generated_pdf.pdf'

    return response


app.run(debug=True)
