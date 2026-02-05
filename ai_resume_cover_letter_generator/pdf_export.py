import io
import re

from fpdf import FPDF


class ResumePDF(FPDF):
    def __init__(self, author: str):
        super().__init__()
        self.author = author

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Generated for {self.author}", align="C")


def export_to_pdf(content: str, author: str, doc_type: str) -> bytes:
    pdf = ResumePDF(author)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=20)

    lines = content.split("\n")

    for line in lines:
        stripped = line.strip()

        if not stripped:
            pdf.ln(4)
            continue

        # H1
        if stripped.startswith("# "):
            text = stripped[2:]
            text = _strip_markdown(text)
            pdf.set_font("Helvetica", "B", 18)
            pdf.set_text_color(30, 30, 30)
            pdf.cell(0, 12, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)

        # H2
        elif stripped.startswith("## "):
            text = stripped[3:]
            text = _strip_markdown(text)
            pdf.set_font("Helvetica", "B", 14)
            pdf.set_text_color(50, 50, 50)
            pdf.ln(4)
            pdf.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
            # Draw a line under the heading
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
            pdf.ln(3)

        # H3
        elif stripped.startswith("### "):
            text = stripped[4:]
            text = _strip_markdown(text)
            pdf.set_font("Helvetica", "B", 12)
            pdf.set_text_color(60, 60, 60)
            pdf.ln(2)
            pdf.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1)

        # Bullet points
        elif stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:]
            text = _strip_markdown(text)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(40, 40, 40)
            pdf.cell(8)
            pdf.cell(4, 6, chr(8226))
            pdf.multi_cell(0, 6, text)

        # Horizontal rule
        elif stripped in ("---", "***", "___"):
            pdf.ln(2)
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 170, pdf.get_y())
            pdf.ln(4)

        # Regular text
        else:
            text = _strip_markdown(stripped)
            pdf.set_font("Helvetica", "", 10)
            pdf.set_text_color(40, 40, 40)
            pdf.multi_cell(0, 6, text)

    buffer = io.BytesIO()
    pdf.output(buffer)
    return buffer.getvalue()


def _strip_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return text
