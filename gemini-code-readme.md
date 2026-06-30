# DocIntel AI - Document Intelligence Workspace

DocIntel AI is a professional-grade tool designed to convert complex, scanned PDFs and images into structured, editable formats like Excel, Word, and PowerPoint. 

## The Vision
Unlike traditional converters that are "black boxes," DocIntel AI focuses on **reconstruction** rather than simple extraction. We specialize in:
* **Academic Research Papers:** Preserving multi-column layouts and complex table structures.
* **Handwritten Medical/Legal Forms:** Digitizing unstructured document types with high layout awareness.
* **Data Integrity:** Ensuring that tables in PDFs are correctly mapped into Excel/CSV formats.

## Key Features
* **Layout Awareness:** Uses advanced document intelligence to understand structural relationships (tables vs. headers vs. paragraphs).
* **Interactive Ready:** Built with a backend API designed for real-time validation and "Human-in-the-Loop" corrections.
* **Privacy Focused:** Designed with a cleanup architecture to ensure uploaded files are processed and discarded.

## Technical Architecture
* **Backend:** FastAPI (Python)
* **AI Processing:** Powered by Docling & Layout analysis engines.
* **Frontend:** Next.js / React (Ready to integrate)

## Getting Started
1. Clone this repository.
2. Ensure you have Python 3.10+ installed.
3. Install requirements: `pip install fastapi uvicorn docling`
4. Run the backend: `uvicorn main:app --reload`