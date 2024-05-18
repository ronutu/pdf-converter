import fitz
import PIL.Image as Image
from PIL import ImageDraw
import io


def extract_pdf(path, page_nr):
    text_attributes_list = []

    doc = fitz.Document(path)
    page = doc.load_page(page_nr+1)
    text_attributes_dict = page.get_text("dict")

    zoom_factor = 3
    matrix = fitz.Matrix(zoom_factor, zoom_factor)
    pixmap = page.get_pixmap(matrix=matrix)
    print(pixmap.tobytes())
    img = Image.open(io.BytesIO(pixmap.tobytes()))
    img_border = fitz.Rect(0, 0, img.width, img.height)

    draw = ImageDraw.Draw(img)

    for block in text_attributes_dict['blocks']:
        if block['type'] == 0:
            #print(block)
            rect = fitz.Rect(*tuple(xy * zoom_factor for xy in block['bbox']))
            #draw.rectangle(rect, outline='red', width=2)
            if img_border.contains(rect):
                color = pixmap.color_topusage(clip=rect)[1]
                block['bg_color'] = tuple(color)
    img.save("test.png")
    #print(page.get_text("dict"))
    for block in text_attributes_dict["blocks"]:
        if "lines" in block.keys():
            for line in block["lines"]:
                for span in line["spans"]:
                    text_attributes_list.append([span["text"], span["size"], span["font"], span["color"],
                                                 block["bg_color" if "bg_color" in block.keys() else None]])

    doc.close()
    return text_attributes_list
