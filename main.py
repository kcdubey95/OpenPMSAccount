from flask import Flask, render_template, make_response
from reportlab.pdfgen import canvas
from io import BytesIO
app = Flask(__name__)


@app.route("/step1")
def index():
    return render_template("step1.html")


@app.route("/mobile")
def mobile_no():
    return render_template("mobile.html")


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
