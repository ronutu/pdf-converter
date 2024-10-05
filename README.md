﻿# PDF convertor to HTML

This app automates the process of converting PDF textbooks into structured HTML pages. The application extracts content from PDF files and applies various transformations to clean, organize, and style the data for seamless HTML output. Key features include:

Content Extraction: Extracts text and images from each page of the PDF using powerful parsing algorithms.
Text Cleaning: Automatically removes unwanted characters, such as mathematical symbols, page numbers, and irrelevant text formatting, for a cleaner result.
Styling and Structure: Combines related text blocks and applies proper HTML tags to recreate the structure of the textbook (headings, paragraphs, lists).
Page Management: Converts individual or multiple pages at once, generating HTML files for each page with consistent numbering and styling.
Customizable Output: Supports various formatting elements, including bold, italics, colored backgrounds, and lists, to maintain the visual identity of the original textbook.
GUI Interface: Provides a simple GUI to choose between processing a single page or the entire textbook at once.
This app ensures that textbooks are converted into accessible and well-structured HTML pages while preserving their educational layout and design​(build)​(clean)​(combine)​(convert)​(extract)​(gui)​(main)​(paragraphs).




1. PDF Extraction
The extraction step pulls content from the PDF and organizes it into a structured array. 

Data format after extraction:

Text: The actual text extracted from the PDF
Size: The font size of the text
Font: The font family
Color: The text color
bg_color: The background color of the text block
Example output after extraction:

css
Copy code
[    ['Chapter 1', 18.0, 'PTSans-Bold', 0, (255, 255, 255)],
    ['Introduction', 14.0, 'ITCKabelStd-BoldRO', 16777215, (255, 241, 214)],
    ['This is some sample text...', 11.0, 'PTSans-Regular', 2236191, (255, 255, 255)]
]
The content is extracted block by block (text and images), and this structured data is passed to the next phase​(extract).

2. Text Cleaning
In the cleaning phase (clean_text function in clean.py), the extracted array is filtered to remove unwanted elements, like page numbers, empty spaces, symbols, and irrelevant formatting.

Key cleaning operations:

Page Numbers: Identifies and removes page numbers based on specific font and size conditions (e.g., font 'MinionPro-Bold' with size 10).
Empty Spaces: Removes unnecessary spaces and special characters (e.g., \xa0).
Symbols: Removes mathematical symbols and formulas by checking font types (e.g., 'SymbolMT').
Section Headers: Removes or replaces specific phrases like "Citește și..." and formulas commonly found in textbooks.
Example cleaning transformation:

Input: ['10', 10.0, 'MinionPro-Bold', 0, (255, 255, 255)] (Page number)
Output: This entry would be removed from the array.
After cleaning, the text_attributes_list contains only relevant and meaningful content​(clean).

3. Text Combination
After cleaning, the app enters the combination phase (combine_text and related functions in combine.py), which merges or restructures text blocks based on their formatting and visual alignment.

Combination process:

Text Merging: Consecutive text blocks with similar font size, font family, and background color are merged. For example, two paragraphs that are visually the same but separated by line breaks in the PDF may be combined into one.
Unordered Lists (UL): Text elements identified as bullet points are grouped together into <ul> tags to preserve the list structure.
Ordered Lists (OL): Similarly, elements recognized as numbered lists are grouped into <ol> tags.
Special Shapes and Symbols: Recognizes unique elements like blue arrows, squares, or specific background colors, and wraps them in appropriate HTML tags (e.g., <div class="ulsquare">).
Example combination transformation: If two elements have the same size, font, and background color, such as:

css
Copy code
['This is some', 11.0, 'PTSans-Regular', 2236191, (255, 255, 255)],
['sample text...', 11.0, 'PTSans-Regular', 2236191, (255, 255, 255)]
They are combined into:

css
Copy code
['This is some sample text...', 11.0, 'PTSans-Regular', 2236191, (255, 255, 255)]
Handling special cases: The app also handles other text elements such as:

Icons: Bullet points (•) and other symbols are detected and replaced with corresponding HTML elements.
Lists: Items in numbered or bulleted lists are grouped under <ul> or <ol> HTML tags with list items <li>​(combine)​(convert).
4. Formatting and HTML Conversion
Once the text is cleaned and combined, the data is converted to HTML. This is done in the pdf_to_html function in convert.py. Based on the extracted font size, color, and text types, the corresponding HTML tags are applied.

HTML Tagging:

Headings: Titles and subtitles are converted into <h2>, <h3>, and other heading tags.
Paragraphs: Regular text is wrapped in <p> tags.
Lists: As mentioned earlier, lists are identified and enclosed in <ul> or <ol>.
Special Elements: Text with different colors or special importance (like bold, italics, etc.) is marked with appropriate HTML classes (e.g., <span class="bold"> for bold text).
Example HTML conversion:

css
Copy code
<h2>Chapter 1</h2>
<p>This is some sample text...</p>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
After applying these transformations, the build_html function in build.py saves the final HTML file, which includes both the content and its styling​(build)​(convert)​(main).

This workflow ensures that the PDF content is not only preserved but also cleaned, structured, and formatted properly into HTML, making it suitable for web display.





## License

This project is licensed under the terms of the [GNU Affero General Public License (AGPL)](https://www.gnu.org/licenses/agpl-3.0.html). See the COPYING file for details.
