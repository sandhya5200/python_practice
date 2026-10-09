
import fitz  # PyMuPDF
import re
import csv

pdf_path = "/home/thrymr/Downloads/medical_rag1/medical_rag/books/Harrison's  İnternal Medicine_first_100_pages.pdf"
index = []

doc = fitz.open(pdf_path)

# Process only the first 40 pages
for page_num in range(min(40, len(doc))):
    page = doc[page_num]
    text = page.get_text("text")

    # Extract headings using font size
    data = page.get_text("dict")

    for block in data["blocks"]:
        if "lines" not in block:
            continue

        for line in block["lines"]:
            for span in line["spans"]:
                heading = span["text"].strip()

                # Basic heading detection
                if (
                    heading
                    and len(heading) > 3
                    and span["size"] >= 14
                    and len(heading) < 120
                ):
                    index.append({
                        "Topic": heading,
                        "Page Number": page_num + 1
                    })

# Save index to CSV
with open("/home/thrymr/Downloads/multimodal_Pharyngolaryngeal applied anatomy_20261007_190815.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file, fieldnames=["Topic", "Page Number"]
    )
    writer.writeheader()
    writer.writerows(index)

print("Index generated: book_index.csv")
