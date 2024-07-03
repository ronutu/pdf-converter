import pymupdf
import PIL.Image as Image
import io


def extract_pdf(path, page_nr):
    # Open PDF and extract text as a dictionary
    pdf = pymupdf.open(path)
    page = pdf.load_page(page_nr + 1)
    text_attributes_list = []
    text_attributes_dict = page.get_text('dict')

    # Turn page into a pixmap
    zoom_factor = 3
    matrix = pymupdf.Matrix(zoom_factor, zoom_factor)
    pixmap = page.get_pixmap(matrix=matrix)
    image = Image.open(io.BytesIO(pixmap.tobytes()))
    img_border = pymupdf.Rect(0, 0, image.width, image.height)

    for block in text_attributes_dict['blocks']:
        if block['type'] == 0:  # if type is 0 then it is a text block / if type is 1 then it is an image block
            bbox = block['bbox']
            x0, y0, x1, y1 = bbox
            x0_zoomed = x0 * zoom_factor
            y0_zoomed = y0 * zoom_factor
            x1_zoomed = x1 * zoom_factor
            y1_zoomed = y1 * zoom_factor
            rect = pymupdf.Rect(x0_zoomed, y0_zoomed, x1_zoomed, y1_zoomed)

            if img_border.contains(rect):  # Check if the text block is in the image
                color = pixmap.color_topusage(clip=rect)[1]  # Find the most used color in the bbox
                block['bg_color'] = tuple(color)
            else:
                continue
            for line in block['lines']:
                for span in line['spans']:
                    text_attributes_list.append([span['text'], span['size'], span['font'], span['color'], block['bg_color']])
        elif block['type'] == 1:
            text_attributes_list.append(['''
        <img class="img-responsive" src="images/.png" alt="" />''', 0, '0', 0, (256, 0, 0)])
    image.close()
    pdf.close()
    return text_attributes_list