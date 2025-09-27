from PIL import Image
from fpdf import FPDF

# === SETTINGS ===
logo_path = "coursera_logo.png"  # Replace with your actual logo file name
output_pdf = "Coursera_Receipt_Rs27000_Sarjerao_Sandbhor.pdf"

# Billing info
customer_name = "Sarjerao Sandbhor"
billing_date = "09-12-2025"
order_number = "413755937"
product_name = "Google IT Automation with Python"
plan = "3 months (Prepaid)"
total_amount = 27000.00
gst_rate = 0.18
base_amount = total_amount / (1 + gst_rate)
gst_amount = total_amount - base_amount
hsn_code = "999294"
gstin = "9919USA29027OS"

# === PDF GENERATION ===
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)

# Add logo
pdf.image(logo_path, x=10, y=8, w=50)
pdf.ln(30)

# Greeting
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Dear {customer_name},", ln=True)
pdf.cell(0, 10, "Thank you for your purchase.", ln=True)
pdf.ln(5)

# Receipt header
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "RECEIPT", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "Coursera Inc.\n381 E. Evelyn Avenue\nMountain View, CA 94041 USA")
pdf.cell(0, 10, f"Date: {billing_date}", ln=True)
pdf.cell(0, 10, f"Order Number: {order_number}", ln=True)
pdf.ln(5)

# Product details
pdf.set_font("Arial", "B", 12)
pdf.cell(80, 10, "Product Details")
pdf.cell(40, 10, "Plan")
pdf.cell(30, 10, "Amount", ln=True)

pdf.set_font("Arial", "", 12)
pdf.cell(80, 10, product_name)
pdf.cell(40, 10, plan)
pdf.cell(30, 10, f"INR {total_amount:.2f}", ln=True)
pdf.ln(5)

# Tax details
pdf.cell(0, 10, f"GST Rate: {int(gst_rate * 100)}%", ln=True)
pdf.cell(0, 10, f"GST (INR): {gst_amount:.2f}", ln=True)
pdf.cell(0, 10, f"HSN code: {hsn_code}", ln=True)
pdf.cell(0, 10, f"GSTIN: {gstin}", ln=True)
pdf.ln(5)

# Total
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, f"TOTAL (INR): {total_amount:.2f}", ln=True)
pdf.ln(10)

# Footer
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "Please keep this receipt as record of your payment.", ln=True)
pdf.cell(0, 10, "View our refund policy.", ln=True)
pdf.cell(0, 10, "View your purchase history.", ln=True)
pdf.ln(10)
pdf.cell(0, 10, "Happy Learning!", ln=True)
pdf.cell(0, 10, "The Coursera Team", ln=True)

# Save PDF
pdf.output(output_pdf)
print(f"PDF saved as: {output_pdf}")