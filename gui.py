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
import mysql.connector


def apply_changes(book_path, nr):
    text_attributes_list = extract.extract_pdf(book_path, nr)

    transformations = [
        clean.clean_text,
        paragraphs.titlu_unitate_romana,
        paragraphs.titlu_unitate_fizica,
        paragraphs.titlu_unitate_chimie,
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
        paragraphs.text_model
    ]

    for transform in transformations:
        text_attributes_list = transform(text_attributes_list)

    return text_attributes_list


def on_button_click(answer, root, path):
    _, filename = os.path.split(path)
    filename = filename[:-4]
    mydb = mysql.connector.connect(
        host="",
        port=,
        user="",
        password="",
        database="manuale"
    )

    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM {filename}")
    mydb.commit()

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
        for page_nr in range(7, len(doc) - 5):
            data = apply_changes(path, page_nr)
            html = f"""
                <p class="clear"></p>
                <p class="space"></p>
                <p class="right"><span class="page">{page_nr}</span></p>
                """
            data.append([html, 0, '0', 0, (257, 0, 0)])
            if page_nr < 10:
                output = r'manuale\\' + filename + r'\pag_00' + str(page_nr) + '.html'
            elif page_nr < 100:
                output = r'manuale\\' + filename + r'\pag_0' + str(page_nr) + '.html'
            else:
                output = r'manuale\\' + filename + r'\pag_' + str(page_nr) + '.html'
            build.build_html(data, output, page_nr)
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

    question_label = tk.Label(root, text="One page or whole file?")
    question_label.pack(pady=20)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    button_aaa = tk.Button(button_frame, text="ONE", command=lambda: on_button_click("ONE", root, path))
    button_aaa.pack(side=tk.LEFT, padx=10)

    button_bbb = tk.Button(button_frame, text="ALL", command=lambda: on_button_click("ALL", root, path))
    button_bbb.pack(side=tk.LEFT, padx=10)

    root.mainloop()
