# Generating an invoice PDF that matches the provided invoice PDF layout and calculations.
# The generated file will be saved to /mnt/data/generated_invoice.pdf
# This uses reportlab (commonly available). If reportlab is not installed in the environment,
# the code will attempt to install it (pip). Installing packages in this environment may or may not be permitted.
# The layout approximates the uploaded invoice and uses values pulled from the uploaded file:
# - Training Cost: 29,520.00
# - SGST: 3,240.00
# - CGST: 3,240.00
# - Total: 36,000.00
# - Enrollment Date: 10th Sept 2025
# - Training Date: 13th Sept 2025
# - Bill No: SEPT13092025/25
# - Company GST: 07AUNPY7160Q1ZF
#
# The script draws a simple logo, computes GST rates from the amounts, and adds a signature and a circular stamp.
# Run this cell to produce /mnt/data/generated_invoice.pdf

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
except Exception as e:
    # Attempt to install reportlab if missing
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors

import math
from decimal import Decimal, ROUND_HALF_UP

OUTPUT_PATH = "/mnt/data/generated_invoice.pdf"

# Values taken from the uploaded PDF (see attached file). Citation will be provided outside this python block.
training_cost = Decimal("29520.00")
sgst = Decimal("3240.00")
cgst = Decimal("3240.00")
total = Decimal("36000.00")
enrollment_date = "10th Sept 2025"
training_date = "13th Sept 2025"
bill_no = "SEPT13092025/25"
company_gst = "07AUNPY7160Q1ZF"

# Derive GST rates from amounts (rounded to 4 decimal places for display)
def percent(part, whole):
    if whole == 0:
        return Decimal("0.00")
    return (part / whole * Decimal(100)).quantize(Decimal("0.0001"))

sgst_rate = percent(sgst, training_cost)
cgst_rate = percent(cgst, training_cost)
total_tax = sgst + cgst
total_tax_rate = percent(total_tax, training_cost)

# Helper to format INR amounts
def fmt(x):
    return "₹{:,}".format(int(x)) if x == x.to_integral() else "₹{:,.2f}".format(x)

# Create PDF
c = canvas.Canvas(OUTPUT_PATH, pagesize=A4)
width, height = A4

# Margins
left_margin = 18 * mm
right_margin = width - 18 * mm
y = height - 20 * mm

# Draw logo (simple box with text) on left
logo_w = 45 * mm
logo_h = 20 * mm
c.setStrokeColor(colors.HexColor("#0B5394"))
c.setLineWidth(1.2)
c.rect(left_margin, y - logo_h, logo_w, logo_h, stroke=1, fill=0)
c.setFont("Helvetica-Bold", 12)
c.drawString(left_margin + 6 * mm, y - 8 * mm, "LEARNINGHUB")
c.setFont("Helvetica", 7)
c.drawString(left_margin + 6 * mm, y - 13 * mm, "Authorized Training Partner")

# Header company info on right
c.setFont("Helvetica-Bold", 12)
c.drawRightString(right_margin, y - 4 * mm, "LearningHub")
c.setFont("Helvetica", 8)
c.drawRightString(right_margin, y - 9 * mm, "S-12 Destination Center, 2nd Floor, Magarpatta City, Hadapsar, Pune 411028")
c.drawRightString(right_margin, y - 14 * mm, "Website: www.learninghub.co.in | Email: akshay@learninghub.co.in | Ph: 020-67230224")

y -= 28 * mm

# Invoice title and bill details
c.setFont("Helvetica-Bold", 16)
c.drawString(left_margin, y, "Payment Invoice")
c.setFont("Helvetica", 9)
c.drawString(right_margin - 120 * mm, y, f"Bill No : {bill_no}")
y -= 6 * mm
c.setFont("Helvetica", 9)
c.drawString(left_margin, y, f"Enrollment Date : {enrollment_date}")
c.drawString(left_margin + 80 * mm, y, f"Training Date : {training_date}")
y -= 10 * mm

# Bill to
c.setFont("Helvetica-Bold", 10)
c.drawString(left_margin, y, "To,")
c.setFont("Helvetica", 10)
c.drawString(left_margin + 12 * mm, y, "Mr. Sarjerao Sandbhor")
y -= 12 * mm

# Draw table headers
table_x = left_margin
table_w = right_margin - left_margin
row_h = 9 * mm

c.setFont("Helvetica-Bold", 9)
c.rect(table_x, y - row_h, table_w, row_h, stroke=1, fill=0)
c.drawString(table_x + 4 * mm, y - 6 * mm, "Sr. No")
c.drawString(table_x + 20 * mm, y - 6 * mm, "Description")
c.drawRightString(right_margin - 4 * mm, y - 6 * mm, "Amount")

# Row 1 - Details
y -= row_h
c.setFont("Helvetica", 9)
c.rect(table_x, y - row_h, table_w, row_h * 1.8, stroke=1, fill=0)
c.drawString(table_x + 4 * mm, y - 6 * mm, "1")
desc_x = table_x + 20 * mm
line_y = y - 6 * mm
c.drawString(desc_x, line_y, "Details:")
c.setFont("Helvetica", 8)
c.drawString(desc_x, line_y - 7, "Training: - Professional Development (PD)")
c.drawString(desc_x, line_y - 14, u"\u2022 Training cost")
c.drawString(right_margin - 40 * mm, line_y - 14, fmt(training_cost))
c.drawString(desc_x, line_y - 21, u"\u2022 Tax details:")
c.drawString(desc_x + 6 * mm, line_y - 28, "o SGST           " + fmt(sgst))
c.drawString(desc_x + 6 * mm, line_y - 35, "o CGST           " + fmt(cgst))

# Totals block on right
totals_w = 60 * mm
totals_x = right_margin - totals_w
totals_y = y - row_h + 8 * mm

c.setFont("Helvetica", 9)
c.drawRightString(right_margin - 6 * mm, totals_y + 18 * mm, "Total")
c.setFont("Helvetica-Bold", 10)
c.drawRightString(right_margin - 6 * mm, totals_y + 6 * mm, fmt(total))
c.setFont("Helvetica", 8)
# Amount in words (simple approximation)
amount_words = "Rupees thirty-six thousand only."
c.drawString(totals_x, totals_y - 6 * mm, f"Total {amount_words}")

y = y - (row_h * 1.8) - 12 * mm

# Footer notes from invoice
notes = [
    "Payment received against the details given above.",
    "Mode of Payment (Cash)",
    "Fees once paid will not be refunded under any circumstances.",
    "The company reserves right to change the schedule (Cancellation/Postponement).",
    "The execution of the training is on best effort basis.",
    f"Company GST# {company_gst} / HSN code: 999210",
    "We accept Bank Transfer, PayPal and Western Union. 100% payment should be made before or upon receipt of the invoice."
]
c.setFont("Helvetica", 8)
ny = y
for note in notes:
    c.drawString(left_margin, ny, u"\u2022 " + note)
    ny -= 6.5 * mm

# Draw signature box on lower-right
sig_x = right_margin - 60 * mm
sig_y = 40 * mm
c.line(sig_x, sig_y + 18 * mm, right_margin - 6 * mm, sig_y + 18 * mm)
c.setFont("Helvetica", 9)
c.drawString(sig_x, sig_y + 4 * mm, "Authorised Sign")
# Draw sample handwritten-like signature text (italic)
c.setFont("Helvetica-Oblique", 10)
c.drawString(sig_x, sig_y - 4 * mm, "Akshay")
c.setFont("Helvetica", 7)
c.drawString(sig_x, sig_y - 10 * mm, "LearningHub")

# Draw a circular stamp near signature
stamp_center_x = sig_x - 20 * mm
stamp_center_y = sig_y + 10 * mm
stamp_radius = 18 * mm
c.setLineWidth(1.2)
c.circle(stamp_center_x, stamp_center_y, stamp_radius, stroke=1, fill=0)
c.setFont("Helvetica-Bold", 8)
c.drawCentredString(stamp_center_x, stamp_center_y + 4 * mm, "LEARNINGHUB")
c.setFont("Helvetica", 7)
c.drawCentredString(stamp_center_x, stamp_center_y - 2 * mm, "Authorized Partner")

# Small GST calculation summary table
gst_table_x = left_margin
gst_table_y = stamp_center_y - 12 * mm
c.setFont("Helvetica-Bold", 9)
c.drawString(gst_table_x, gst_table_y + 10 * mm, "GST Calculation")
c.setFont("Helvetica", 9)
c.drawString(gst_table_x, gst_table_y + 4 * mm, f"Taxable Value: {fmt(training_cost)}")
c.drawString(gst_table_x + 60 * mm, gst_table_y + 4 * mm, f"SGST @ {sgst_rate}% : {fmt(sgst)}")
c.drawString(gst_table_x, gst_table_y - 3 * mm, f"")
c.drawString(gst_table_x + 60 * mm, gst_table_y - 3 * mm, f"CGST @ {cgst_rate}% : {fmt(cgst)}")
c.drawString(gst_table_x, gst_table_y - 10 * mm, f"Total Tax: {fmt(total_tax)} ({total_tax_rate}%)")

# Footer small print about acceptance
c.setFont("Helvetica-Oblique", 7)
c.drawString(left_margin, 18 * mm, "This is a computer generated invoice and does not require a physical signature when emailed.")

c.showPage()
c.save()

print("Generated:", OUTPUT_PATH)
