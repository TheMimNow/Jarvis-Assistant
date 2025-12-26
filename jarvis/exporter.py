from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

class ChatExporter:
    def __init__(self, memory):
        self.memory = memory

    def export_pdf(self, filename="jarvis_chat.pdf"):
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        y = height - 40
        c.setFont("Helvetica-Bold", 10)

        c.drawString(40, y, "Jarvis Chat History")

        y -= 30

        for msg in self.memory.get_history():
            role = msg["role"].upper()
            text = msg["message"]

            lines = text.split('\n')
            c.drawString(40, y, f"{role}:")
            y -= 15

            for line in lines:
                if y < 50:
                    c.showPage()
                    c.setFont("Helvetica", 10)
                    y = height - 40
                c.drawString(60, y, line)
                y -= 14

            y -= 10

        c.drawString(40, 30, f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")    

        c.save()
        return filename
