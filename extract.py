import fitz
import PIL.Image as Image
from PIL import ImageDraw
import io


def extract_bkgr_color(page, doc):
    page = page
    image_list = page.get_images()
    #print(page.get_image_info())
    for image_index, img in enumerate(image_list, start=1):  # enumerate the image list
        xref = img[0]  # get the XREF of the image
        pix = fitz.Pixmap(doc, xref)  # create a Pixmap

        if pix.n - pix.alpha > 3:  # CMYK: convert to RGB first
            pix = fitz.Pixmap(fitz.csRGB, pix)

        pix.save("page_%s-image_%s.png" % (27, image_index))  # save the image as png
        pix = None

    text_attributes_dict = page.get_text("dict")
    zoom_factor = 3
    matrix = fitz.Matrix(zoom_factor, zoom_factor)
    pixmap = page.get_pixmap(matrix=matrix)
    img = Image.open(io.BytesIO(pixmap.tobytes()))
    img_border = fitz.Rect(0, 0, img.width, img.height)

    draw = ImageDraw.Draw(img)
    for block in text_attributes_dict['blocks']:
        if block['type'] == 0:
            bbox = block['bbox']
            x0, y0, x1, y1 = bbox

            x0_zoomed = x0 * zoom_factor
            y0_zoomed = y0 * zoom_factor
            x1_zoomed = x1 * zoom_factor
            y1_zoomed = y1 * zoom_factor

            rect = fitz.Rect(x0_zoomed, y0_zoomed, x1_zoomed, y1_zoomed)
            # rect = fitz.Rect(*tuple(xy * zoom_factor for xy in block['bbox']))
            draw.rectangle(rect, outline='red', width=2)
            if img_border.contains(rect):
                color = pixmap.color_topusage(clip=rect)[1]
                block['bg_color'] = tuple(color)
    img.save("test.png")
    return text_attributes_dict


def extract_pdf(path, page_nr):
    doc = fitz.Document(path)
    page = doc.load_page(page_nr + 1)
    text_attributes_list = []
    text_attributes_dict = extract_bkgr_color(page, doc)
    for block in text_attributes_dict["blocks"]:
        if "lines" in block.keys():
            for line in block["lines"]:
                for span in line["spans"]:
                    text_attributes_list.append([span["text"], span["size"], span["font"], span["color"],
                                                 block["bg_color" if "bg_color" in block.keys() else None]])

    return text_attributes_list
