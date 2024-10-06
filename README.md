# PDF to HTML convertor
This project provides a solution for converting textbook PDFs into clean, structured HTML format. It is designed to process textbooks, extract and clean text, combine elements such as lists and paragraphs, and then generate accessible HTML files.

## Features:
- PDF Parsing: Extracts text and image elements from each page of the PDF using pymupdf.
- Text Cleanup: Removes unwanted elements like formulas, page numbers, and whitespace using customized cleaning functions.
- HTML Generation: Converts cleaned and processed text into structured HTML files using Bootstrap for styling.
- Custom Lists and Layouts: Combines text blocks with similar styles, supports lists (unordered, ordered, and bullet points), and processes textbook-specific elements like exercise blocks and example sections.
- GUI Interface: Built with Tkinter to allow easy selection of PDF files and conversion options (single page or entire textbook).
- MySQL Integration: Saves processed text to a MySQL database for further use or analysis.

## How It Works:
1. Extract Text: The project extracts text attributes (font, size, color, etc.) from each page of the PDF.
2. Clean and Combine: The text is cleaned and combined based on predefined rules to ensure proper formatting.
3. Convert to HTML: Generates structured HTML with appropriate tags for headers, paragraphs, lists, and more, suitable for digital textbooks.





## License

This project is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://www.gnu.org/licenses/agpl-3.0.html). See the COPYING file for details.
