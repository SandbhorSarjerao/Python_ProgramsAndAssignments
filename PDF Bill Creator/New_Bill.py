from fpdf import FPDF

# GST calculations for ₹27,000 inclusive of 18% GST
total_price = 27000.00
gst_rate = 18
base_price = round(total_price / (1 + gst_rate / 100), 2)
gst_amount = round(total_price - base_price, 2)

# Create a PDF object
pdf = FPDF()
pdf.add_page()

# Insert logo
logo_path = "coursera_logo.png"  # Replace with your logo path
pdf.image(logo_path, x=10, y=8, w=50)

# Move below logo
pdf.ln(30)

# Header
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "RECEIPT", ln=True)

pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Coursera Inc.", ln=True)
pdf.cell(0, 10, "381 E. Evelyn Avenue", ln=True)
pdf.cell(0, 10, "Mountain View, CA 94041 USA", ln=True)
pdf.cell(0, 10, "09-12-2025", ln=True)

# Order Info
pdf.ln(5)
pdf.cell(0, 10, "Order Number: 413755937", ln=True)
pdf.cell(0, 10, "Professional Certificate Prepaid: Google IT Automation with Python", ln=True)

# Table Header
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(80, 10, "Product Details", border=1)
pdf.cell(30, 10, "Plan", border=1)
pdf.cell(30, 10, "Price", border=1)
pdf.cell(20, 10, "Qty", border=1, ln=True)

# Table Row
pdf.set_font("Arial", '', 12)
pdf.cell(80, 10, "Google IT Automation with Python", border=1)
pdf.cell(30, 10, "3 months", border=1)
pdf.cell(30, 10, f"INR {total_price:,.2f}", border=1)
pdf.cell(20, 10, "1", border=1, ln=True)

# GST & Total Info
pdf.ln(5)
pdf.cell(0, 10, f"GST Rate: {gst_rate}%", ln=True)
pdf.cell(0, 10, f"Base Price (Excl. GST): INR {base_price:,.2f}", ln=True)
pdf.cell(0, 10, f"GST Amount (INR): {gst_amount:,.2f}", ln=True)
pdf.cell(0, 10, "HSN code: 999294", ln=True)
pdf.cell(0, 10, "GSTIN: 9919USA29027OS", ln=True)

# Total
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, f"TOTAL (INR): {total_price:,.2f}", ln=True)

# Footer
pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Please keep this receipt as record of your payment.", ln=True)
pdf.cell(0, 10, "View our refund policy.", ln=True)
pdf.cell(0, 10, "View your purchase history.", ln=True)
pdf.cell(0, 10, "Happy Learning!", ln=True)
pdf.cell(0, 10, "The Coursera Team", ln=True)

# Save PDF
pdf.output("Coursera_Receipt_Sarjerao_Sandbhor.pdf")