from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Documentation', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_diagram(self, diagram_path):
        self.image(diagram_path, x=10, w=190)
        self.ln(10)

# Create instance of PDF class
pdf = PDF()

# Add a page
pdf.add_page()

# Project Overview
pdf.chapter_title('1. Project Overview')
project_overview = 'This project is a comprehensive tool that allows ...'
pdf.chapter_body(project_overview)

# Architecture Diagrams
pdf.chapter_title('2. Architecture Diagrams')
pdf.add_diagram('path/to/architecture_diagram.png')  # Update with actual path

# Technical Documentation
pdf.chapter_title('3. Technical Documentation')
documentation = 'This section provides detailed information on ...'
pdf.chapter_body(documentation)

# Code Samples
pdf.chapter_title('4. Code Samples')
code_samples = """def example_function(param):\n    return param * 2\n"""
pdf.chapter_body(code_samples)

# Metrics
pdf.chapter_title('5. Metrics')
metrics_info = 'The project metrics include ...'
pdf.chapter_body(metrics_info)

# Dashboard Visualizations
pdf.chapter_title('6. Dashboard Visualizations')
pdf.add_diagram('path/to/dashboard_visualization.png')  # Update with actual path

# Save the PDF to a file
pdf.output('Project_Documentation.pdf')

if __name__ == '__main__':
    pdf.output('generate_pdf_documentation.pdf')