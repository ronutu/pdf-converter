import tkinter as tk
from tkinter import filedialog, simpledialog
import build
import extract
import clean
import paragraphs
import convert
import combine
import os
import pymupdf


def remove_extra_spaces(text_list):
    # Process each item's first element (if it's a list and a string) to remove extra spaces.
    new_list = []
    for item in text_list:
        if isinstance(item, list) and len(item) > 0 and isinstance(item[0], str):
            item[0] = item[0].replace(" .", ".").replace("( ", "(").replace(" )", ")").replace(" ,", ",")
        new_list.append(item)
    return new_list


def apply_changes(book_path, nr):
    text_attributes_list = extract.extract_pdf(book_path, nr)
    # print(text_attributes_list)
    transformations = [
        clean.clean_text,
        paragraphs.titlu_unitate_romana,
        paragraphs.titlu_unitate_fizica,
        paragraphs.titlu_unitate_chimie,
        paragraphs.titlu_unitate_03mat,
        convert.pdf_to_html,
        combine.combine_text,
        combine.combine_ulv,
        combine.ol_li,
        combine.combine_patrat_albastru,
        combine.combine_blue_arrow,
        combine.combine_bullet,
        combine.combine_exercitiu,
        paragraphs.bkgr_read,
        paragraphs.bkgr_pers,
        paragraphs.text_imp,
        paragraphs.paragraph,
        paragraphs.text_galben,
        paragraphs.text_mov,
        paragraphs.text_blue,
        paragraphs.text_model,
        remove_extra_spaces  # Newly added transformation
    ]

    for transform in transformations:
        text_attributes_list = transform(text_attributes_list)
 # Remove elements with an empty first element
        text_attributes_list = [item for item in text_attributes_list if not (isinstance(item, list) and len(item) > 0 and item[0] == "")]
    return text_attributes_list


def on_button_click(answer, root, path):
    _, filename = os.path.split(path)
    filename = filename[:-4]
    if answer == "ONE":
        page_number = simpledialog.askinteger("Input", "Enter the page number", parent=root)
        root.destroy()
        text_attributes_list = apply_changes(path, page_number)

        if page_number < 10:
            output = r'manuale\\' + filename + r'\pag_00' + str(page_number) + '.html'
        elif page_number < 100:
            output = r'manuale\\' + filename + r'\pag_0' + str(page_number) + '.html'
        else:
            output = r'manuale\\' + filename + r'\pag_' + str(page_number) + '.html'
        build.build_html(text_attributes_list, output, page_number)

    elif answer == "ALL":
        root.destroy()
        doc = pymupdf.open(path)
        for page_nr in range(6 ,len(doc)):
            data = apply_changes(path, page_nr)
        #     html = f"""
        # <p class="clear"></p>
        # <p class="space"></p>
        # <p class="right"><span class="page">{page_nr}</span></p>
        # """
        #     data.append([html, 0, '0', 0, (257, 0, 0)])
            if page_nr < 10:
                output = r'manuale\\' + filename + r'\pag_00' + str(page_nr) + '.html'
            elif page_nr < 100:
                output = r'manuale\\' + filename + r'\pag_0' + str(page_nr) + '.html'
            else:
                output = r'manuale\\' + filename + r'\pag_' + str(page_nr) + '.html'
            build.build_html(data, output)
            print(f"Pagina {page_nr} a fost procesata")


def create_question_box():
    root = tk.Tk()
    root.withdraw()

    window_width = 300
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    path = filedialog.askopenfilename(title="Select a file")

    root.deiconify()
    root.title("Textbook")

    question_label = tk.Label(root, text="One page/all pages?")
    question_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    button_aaa = tk.Button(button_frame, text="ONE", command=lambda: on_button_click("ONE", root, path))
    button_aaa.pack(side=tk.LEFT, padx=10)

    button_bbb = tk.Button(button_frame, text="ALL", command=lambda: on_button_click("ALL", root, path))
    button_bbb.pack(side=tk.LEFT, padx=10)

    root.mainloop()
