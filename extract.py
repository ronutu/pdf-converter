import fitz
import PIL.Image as Image
import io
import struct


def extract_pdf(path, page_nr):
    text_attributes_list = []
    doc = fitz.Document(path)
    page = doc.load_page(page_nr+1)
    text_attributes_dict = page.get_text("dict")

    zoom_f = 3
    mat = fitz.Matrix(zoom_f, zoom_f)
    pixmap = page.get_pixmap(matrix=mat)
    img = Image.open(io.BytesIO(pixmap.tobytes()))

    img_border = fitz.Rect(0, 0, img.width, img.height)

    for block in text_attributes_dict['blocks']:
        if block['type'] == 0:
            rect = fitz.Rect(*tuple(xy * zoom_f for xy in block['bbox']))

            if img_border.contains(rect):
                color = pixmap.color_topusage(clip=rect)[1]
                block['bg_color'] = tuple(color)

    for block in text_attributes_dict["blocks"]:
        if "lines" in block.keys():
            for line in block["lines"]:
                for span in line["spans"]:
                    text_attributes_list.append([span["text"], span["size"], span["font"], span["color"],
                                                 block["bg_color" if "bg_color" in block.keys() else None]])

    doc.close()
    return text_attributes_list
