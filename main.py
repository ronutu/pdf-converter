# This file is part of pdf-convertor.
#
# pdf-convertor is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pdf-convertor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdf-convertor. If not, see <https://www.gnu.org/licenses/>.

import extract
import clean
import paragraphs
import convert
import combine
import build
import time
import pandas as pd


start_time = time.time()


def apply_changes(book_path, nr):
    text_attributes_list = extract.extract_pdf(book_path, nr)
    # print(text_attributes_list)
    text_attributes_list = clean.clean_text(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.titlu_unitate(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = convert.pdf_to_html(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = combine.combine_text(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.ol_li(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = combine.combine_patrat_albastru(text_attributes_list)
    # print(text_attributes_list, "\n\n")
    text_attributes_list = combine.combine_blue_arrow(text_attributes_list)
    # print(text_attributes_list, "\n\n")

    df = pd.DataFrame(text_attributes_list, columns=['Text', 'Size', 'Font', 'Text color', 'Background color'])







    text_attributes_list = combine.combine_exercitiu(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.bkgr_read(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.bkgr_pers(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.text_imp(text_attributes_list)
    #print(text_attributes_list)
    text_attributes_list = paragraphs.paragraph(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.text_galben(text_attributes_list)
    # print(text_attributes_list)





    markdown_string = df.to_markdown()

    # Save the Markdown string to a file
    with open('dataframe.md', 'w', encoding="utf-8") as f:
        f.write(markdown_string)



    return text_attributes_list


def main():
    book_path = r'C:\Users\Radu\PycharmProjects\pythonProject\manuale\07llr_interior_2024_book.pdf'
    text_attributes_list = apply_changes(book_path, 34)
    output = r'manuale\Romana_nou\pag0' + str(26) + '.html'
    build.build_html(text_attributes_list, output)
    # for nr in range(5, 211):
    #     data = apply_changes(book_path, nr)
    #     html = f"""
    #             <p class="clear"></p>
    #             <p class="space"></p>
    #             <p class="right"><span class="page">{nr}</span></p>
    #     """
    #     data.append([html, 100, '100', 100, (1, 0, 0)])
    #     if nr < 10:
    #         output = r'manuale\Romana_nou\pag_00' + str(nr) + '.html'
    #     elif nr < 100:
    #         output = r'manuale\Romana_nou\pag_0' + str(nr) + '.html'
    #     else:
    #         output = r'manuale\Romana_nou\pag_' + str(nr) + '.html'
    #     build.build_html(data, output)
    #     print(f"Pagina {nr} a fost procesata")


main()

print("--- %s seconds ---" % (time.time() - start_time))