import fitz  # PyMuPDF
import markdownify

def pdf_to_text(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    try:
        pdf_document = fitz.open(pdf_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text("text")  # Extract raw text
        pdf_document.close()
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None  # Handle errors gracefully
    return text

def convert_to_markdown(text):
    """Converts text to Markdown using markdownify."""
    md = markdownify.markdownify(text, heading_style="ATX")  # ATX for # headings
    return md


# **Correct the file path here!** Use the correct relative or absolute path.
pdf_file_path = '/Users/meet/Library/CloudStorage/GoogleDrive-meetj665@gmail.com/My Drive/ColabNotebooks/MLPIITM/IITMTemp/tds4/q-pdf-to-markdown.pdf'  #absolute path
output_md_file = 'output.md'  # Name of the output Markdown file


extracted_text = pdf_to_text(pdf_file_path)

if extracted_text:
    # **Manual Heading Insertion (Example)**
    # This is a VERY basic example.  You'll need to adjust it to match
    # the actual headings in your PDF.  Look at the extracted_text first!

    extracted_text = extracted_text.replace("Convert a PDF to Markdown", "# Convert a PDF to Markdown")
    extracted_text = extracted_text.replace("Convert PDFs to Markdown", "## Convert PDFs to Markdown")
    extracted_text = extracted_text.replace("Digital Documentation Transformation for EduDocs Inc.", "## Digital Documentation Transformation for EduDocs Inc.")
    extracted_text = extracted_text.replace("Your Task", "## Your Task")
    extracted_text = extracted_text.replace("Impact", "## Impact")


    markdown_text = convert_to_markdown(extracted_text)

    # Save the Markdown to a file
    try:
        with open(output_md_file, 'w') as f:
            f.write(markdown_text)
        print(f"Markdown saved to {output_md_file}")  # Confirmation message
    except Exception as e:
        print(f"Error saving Markdown to file: {e}")


else:
    print("Could not extract text from the PDF.")

# **DO NOT PRINT THE ORIGINAL PDF CONTENT HERE!**  This is what's causing the error.
# Remove everything from here to the end of the file that is just the text from the pdf