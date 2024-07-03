import re


# Combine text with the same size, font and background color
def combine_text(text_attributes_list):
    new_text_attributes_list = []
    previous_text = ""
    previous_size = 0
    previous_font = ""
    previous_color = 0
    previous_bg_color = (0, 0, 0)
    for element in text_attributes_list:
        text, size, font, color, bg_color = element
        if previous_size - 0.6 <= size <= previous_size + 0.6 and font == previous_font and bg_color == previous_bg_color:
            if previous_text[-1] in ['ț', 'ș']:
                previous_text += text
            else:
                previous_text += " " + text
        else:
            if previous_text:
                new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color, previous_bg_color])
            previous_text = text
            previous_size = size
            previous_font = font
            previous_color = color
            previous_bg_color = bg_color

    if previous_text:
        new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color, previous_bg_color])

    return new_text_attributes_list


def combine_ulv(text_attributes_list):
    # liste de bife
    output_list = []

    list_items = []

    i = 0
    n = len(text_attributes_list)
    while i < n:
        item = text_attributes_list[i]

        if item[0] == '3' and item[4] == (255, 255, 255):
            if i + 1 < n:
                list_items.append(text_attributes_list[i + 1])
                i += 2
            else:
                i += 1
        else:
            if list_items:
                html_list = '''
        <ul class='ulv'>'''
                for li in list_items:
                    html_list += f'''
            <li>{li[0].strip()}</li>'''
                html_list += f'''
        </ul>
        <div class="clear"></div>\n'''
                output_list.append([html_list, 0, '0', 0, (257, 0, 0)])
                list_items = []

            output_list.append(item)
            i += 1

    if list_items:
        html_list = "<ul class='ulv'>\n"
        for li in list_items:
            html_list += f"        <li>{li[0]}</li>\n"
        html_list += '''</ul>
                        <div class="clear"></div>'''
        output_list.append([html_list, 0, '0', 0, (257, 0, 0)])

    return output_list


def ol_li(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        pattern = r'\s(?=[a-z]\))'
        result = re.split(pattern, text_attributes_list[i][0])

        if len(result) == 1:
            new_text_attributes_list.append(text_attributes_list[i])
        else:
            new_text_attributes_list.append([result[0], text_attributes_list[i][1], text_attributes_list[i][2], text_attributes_list[i][3], text_attributes_list[i][4]])
            for j in range(1, len(result)):
                if text_attributes_list[i][4] in [(258, 0, 0), (237, 246, 231), (238, 246, 232)]:
                    new_text_attributes_list.append([f'''
        <p>{result[j]}</p>\n''', 0, '0', 0, (258, 0, 0)])
                else:
                    new_text_attributes_list.append([f'''
        <p>{result[j]}</p>\n''', 0, '0', 0, (257, 0, 0)])
        i += 1

    return new_text_attributes_list


def combine_patrat_albastru(text_attributes_list):
    output_list = []

    list_items = []

    i = 0

    n = len(text_attributes_list)
    while i < n:
        item = text_attributes_list[i]

        if (item[0] == '\x83' and item[2] == 'Wingdings-Regular') or (item[0] == '�' and item[2] == 'Wingdings-Regular'):
            if i + 1 < n:
                list_items.append(text_attributes_list[i + 1])
                i += 2
            else:
                i += 1
        else:
            if list_items:
                html_list = '''
        <ul class='ulsquare'>'''
                for li in list_items:
                    html_list += f'''
            <li>{li[0].strip()}</li>'''
                html_list += f'''
        </ul>
        <div class="clear"></div>\n'''
                if list_items[0][4] != (255, 255, 255):
                    output_list.append([html_list, 0, '0', 0, (258, 0, 0)])
                else:
                    output_list.append([html_list, 0, '0', 0, (257, 0, 0)])
                list_items = []

            output_list.append(item)
            i += 1

    if list_items:
        html_list = "<ul class='ulsquare'>\n"
        for li in list_items:
            html_list += f"        <li>{li[0]}</li>\n"
        html_list += '''</ul>
                        <div class="clear"></div>'''
        if list_items[0][4] != (255, 255, 255):
            output_list.append([html_list, 0, '0', 0, (1, 0, 8)])
        else:
            output_list.append([html_list, 0, '0', 0, (257, 0, 0)])
    return output_list


def combine_blue_arrow(text_attributes_list):
    new_text_attributes_list = []
    arrow_items = ""
    for i, attr in enumerate(text_attributes_list):
        if attr[0] == 't' and attr[4] in [(237, 246, 231), (238, 246, 232)]:
            arrow_items += f"<li>{text_attributes_list[i+1][0]}</li>"
        elif arrow_items:
            html = f"""
                <ul class='ularrow'>
                    {arrow_items}
                </ul>"""
            new_text_attributes_list.append([html, 0, '0', 0, (258, 0, 0)])
            arrow_items = ""
        else:
            new_text_attributes_list.append(attr)

    if arrow_items:
        html = f"""
        <ul class='ularrow'>
        {arrow_items}
        </ul>"""
        new_text_attributes_list.append([html, 0, '0', 0, (258, 0, 0)])

    return new_text_attributes_list


def combine_bullet(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        pattern = '•'
        result = re.split(pattern, text_attributes_list[i][0])
        if len(result) == 1:
            new_text_attributes_list.append(text_attributes_list[i])
        else:

            new_text_attributes_list.append([result[0], text_attributes_list[i][1], text_attributes_list[i][2], text_attributes_list[i][3], text_attributes_list[i][4]])
            for j in range(1, len(result)):
                if text_attributes_list[i][4] in [(258, 0, 0), (237, 246, 231), (238, 246, 232), (236, 240, 231)]:
                    new_text_attributes_list.append([f'''
        <p>• {result[j]}</p>\n''', 0, '0', 0, (258, 0, 0)])
                elif text_attributes_list[i][4] in [(231, 223, 237)]:
                    new_text_attributes_list.append([f'''
                            <p>• {result[j]}</p>\n''', 0, '0', 0, (231, 223, 237)])
                else:
                    new_text_attributes_list.append([f'''
        <p>• {result[j]}</p>\n''', 0, '0', 0, (257, 0, 0)])
        i += 1

    return new_text_attributes_list


def combine_exercitiu(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        text, size, font, color, bg_color = text_attributes_list[i]
        if i < n-1:
            text2, size2, font2, color2, bg_color2 = text_attributes_list[i+1]
            if (size in [9.899495124816895, 10.909099578857422, 9.0]
                    and font in ['PTSans-Bold', 'LMSans10-Bold']
                    and bg_color2 == (255, 255, 255)
                    and 10 <= size2 <= 12
                    and font2 in ['PTSans-Regular', 'MinionPro-Regular', 'LMRoman10-Regular']):
                # exercitiu pt sans regular
                html = f"""
        <div class="block-container">
            <span class="number">{text.strip()}</span>
            <div class="block-number-content">
                <p>{text2}</p>
            </div>
        </div>
        <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
                i += 2
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    if text_attributes_list[-1] != new_text_attributes_list[-1]:
        new_text_attributes_list.append(text_attributes_list[-1])
    return new_text_attributes_list