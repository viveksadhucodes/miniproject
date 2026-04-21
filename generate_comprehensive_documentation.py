from __future__ import annotations

from pathlib import Path

from fpdf import FPDF


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = PROJECT_ROOT / "comprehensive_documentation.pdf"
DASHBOARD_DIR = PROJECT_ROOT / "Dashboards"


class DocumentationPDF(FPDF):
    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(70, 70, 70)
        self.cell(0, 8, "Transportation Lakeflow Pipeline", 0, 1, "R")
        self.ln(2)

    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def add_section_title(pdf: DocumentationPDF, title: str) -> None:
    pdf.ln(2)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(25, 25, 25)
    pdf.cell(0, 10, title, 0, 1)
    pdf.set_draw_color(220, 220, 220)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(4)


def add_paragraph(pdf: DocumentationPDF, text: str) -> None:
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(45, 45, 45)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin, 6, text)
    pdf.ln(1)


def add_bullets(pdf: DocumentationPDF, bullets: list[str]) -> None:
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(45, 45, 45)
    for bullet in bullets:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin, 6, f"- {bullet}")
    pdf.ln(1)


def add_code_block(pdf: DocumentationPDF, code: str, font_size: int = 9) -> None:
    pdf.set_font("Courier", "", font_size)
    pdf.set_fill_color(248, 248, 248)
    pdf.set_text_color(30, 30, 30)
    for line in code.strip("\n").splitlines():
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin, 5, line, border=0, fill=True)
    pdf.ln(2)


def add_table_rows(pdf: DocumentationPDF, rows: list[tuple[str, str]]) -> None:
    pdf.set_font("Helvetica", "", 11)
    for left, right in rows:
        start_y = pdf.get_y()
        pdf.set_font("Helvetica", "B", 11)
        pdf.multi_cell(48, 6, left, border=1)
        x = pdf.l_margin + 48
        pdf.set_xy(x, start_y)
        pdf.set_font("Helvetica", "", 11)
        pdf.multi_cell(0, 6, right, border=1)
        pdf.ln(0)


def add_image_grid(pdf: DocumentationPDF, images: list[tuple[str, str]]) -> None:
    if not images:
        return

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(90, 90, 90)
    col_width = (pdf.w - pdf.l_margin - pdf.r_margin - 8) / 2
    x_start = pdf.l_margin
    y_start = pdf.get_y()

    for index, (label, image_path) in enumerate(images):
        col = index % 2
        row = index // 2
        x = x_start + col * (col_width + 8)
        y = y_start + row * 78

        pdf.set_xy(x, y)
        pdf.multi_cell(col_width, 5, label)

        image_y = pdf.get_y() + 2
        try:
            pdf.image(str(image_path), x=x, y=image_y, w=col_width)
        except Exception:
            pdf.set_xy(x, image_y)
            pdf.set_font("Helvetica", "I", 10)
            pdf.multi_cell(col_width, 5, f"[Unable to render {image_path.name}]")

    pdf.ln(max(78 * ((len(images) + 1) // 2), 78))


def build_pdf() -> None:
    pdf = DocumentationPDF()
    pdf.set_auto_page_break(auto=True, margin=16)

    pdf.add_page()
    pdf.set_fill_color(15, 23, 42)
    pdf.rect(0, 0, pdf.w, 52, style="F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_xy(16, 14)
    pdf.cell(0, 12, "Transportation Lakeflow Pipeline", 0, 1)
    pdf.set_font("Helvetica", "", 13)
    pdf.set_x(16)
    pdf.cell(0, 8, "A medallion architecture project for trip analytics in Databricks", 0, 1)

    pdf.ln(20)
    pdf.set_text_color(35, 35, 35)
    add_paragraph(
        pdf,
        "This repository demonstrates an end-to-end transportation analytics pipeline built with Databricks Delta Live Tables, Lakeflow, PySpark, and Unity Catalog. The code organizes ingestion and transformation across Bronze, Silver, and Gold layers, while a custom calendar dimension enriches trip records for time-series analysis.",
    )

    add_section_title(pdf, "At a Glance")
    add_table_rows(
        pdf,
        [
            ("Tech Stack", "Databricks, Delta Live Tables, Lakeflow, PySpark, Python, Unity Catalog"),
            ("Architecture", "Bronze -> Silver -> Gold medallion pipeline"),
            ("Core Inputs", "City data, trip data, and a parameterized calendar range"),
            ("Output", "Gold analytics views for reporting and dashboarding"),
        ],
    )

    add_section_title(pdf, "Key Features")
    add_bullets(
        pdf,
        [
            "Automated schema evolution for raw ingestion and resilient pipelines.",
            "Data quality expectations that validate trip dates and rating ranges.",
            "Parameter-driven ETL using start_date and end_date Spark settings.",
            "Unity Catalog-aligned design for governance and discoverability.",
        ],
    )

    add_section_title(pdf, "Repository Structure")
    add_code_block(
        pdf,
        """
miniproject/
|-- README.md
|-- Goodcabs-Travels/
|   |-- README.md
|   `-- transformations/
|       |-- bronze/
|       |   |-- city.py
|       |   `-- trips.py
|       |-- silver/
|       |   |-- calendar.py
|       |   |-- city.py
|       |   `-- trips.py
|       `-- gold/
|           |-- trips_gold.sql
|           `-- city-specific gold views
`-- Dashboards/
    `-- PNG screenshots and supporting assets
        """,
    )

    add_section_title(pdf, "Layer Breakdown")
    add_bullets(
        pdf,
        [
            "Bronze: reads raw city and trip files, adds lineage metadata, and preserves source fidelity.",
            "Silver: cleans and standardizes data, builds the calendar table, and applies validation rules.",
            "Gold: joins trip, city, and calendar data into analytics-ready views and SQL outputs.",
        ],
    )

    add_section_title(pdf, "Setup")
    add_paragraph(
        pdf,
        "Configure the DLT pipeline JSON before execution so the calendar layer can generate the correct reporting window.",
    )
    add_code_block(
        pdf,
        """
{
  "configuration": {
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
  }
}
        """,
    )
    add_paragraph(
        pdf,
        "Inside the pipeline code, these values are read from Spark configuration and used to build the calendar dimension.",
    )
    add_code_block(
        pdf,
        """
start_date = spark.conf.get("start_date")
end_date = spark.conf.get("end_date")
        """,
    )

    add_section_title(pdf, "Dashboard Visuals")
    dashboard_images = []
    preferred_assets = [
        "Total Revenue.png",
        "Total Trips.png",
        "Revenue Over Time.png",
        "Trips Over Time.png",
        "Trips by City.png",
        "Revenue by City.png",
    ]
    for name in preferred_assets:
        path = DASHBOARD_DIR / name
        if path.exists():
            dashboard_images.append((path.stem, path))

    add_image_grid(pdf, dashboard_images[:6])

    add_section_title(pdf, "Next Steps")
    add_bullets(
        pdf,
        [
            "Replace placeholder screenshots in the repository with curated dashboard exports.",
            "Extend the Gold layer with additional city or KPI-specific reporting views.",
            "Add CI/CD and deployment automation for repeatable Databricks releases.",
        ],
    )

    pdf.output(str(OUTPUT_PATH))


if __name__ == "__main__":
    build_pdf()