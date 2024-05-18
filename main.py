import extract
import clean
import paragraphs
import convert
import combine
import build
import time


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
    text_attributes_list = combine.combine_exercitiu(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.bkgr_read(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.bkgr_pers(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.text_imp(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.paragraph(text_attributes_list)
    # print(text_attributes_list)
    text_attributes_list = paragraphs.text_galben(text_attributes_list)
    # print(text_attributes_list)

    return text_attributes_list


def main():
    book_path = r'C:\Users\Radu\PycharmProjects\pythonProject\manuale\07llr_interior_2024_book.pdf'
    text_attributes_list = apply_changes(book_path, 26)
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