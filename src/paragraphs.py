def titlu_unitate_romana(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)

    while i < n:
        if i < n-3:
            text, size, font, color, bk_color = text_attributes_list[i]
            text2, size2, font2, color2, bk_color2 = text_attributes_list[i+1]
            text3, size3, font3, color3, bk_color3 = text_attributes_list[i+2]
            if bk_color == (139, 196, 62):
                # Combine text for titlu unitate
                html = f"""
        <div class="center">
            <h1 class="titlu-unitate">
                <span class="text-unitate">UNITATEA<br/><span class="numar-unitate">{text2}</span></span>
            {text3}
            </h1>
        </div>
        <p class="clear"></p>\n
        """
                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
                i += 3
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def titlu_unitate_fizica(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if i < n-3:
            text, size, font, color, bk_color = text_attributes_list[i]
            text2, size2, font2, color2, bk_color2 = text_attributes_list[i+1]
            text3, size3, font3, color3, bk_color3 = text_attributes_list[i+2]
            if bk_color == (222, 120, 113):
                # Combine text for titlu unitate
                html = f"""
        <div class="center">
            <h1 class="titlu-unitate">
                <span class="text-unitate">UNITATEA<br/><span class="numar-unitate">{text2}</span></span>
            {text3}
            </h1>
        </div>
        <p class="clear"></p>\n
        """
                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
                i += 3
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def titlu_unitate_chimie(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if i < n-3:
            text, size, font, color, bk_color = text_attributes_list[i]
            text2, size2, font2, color2, bk_color2 = text_attributes_list[i+1]
            text3, size3, font3, color3, bk_color3 = text_attributes_list[i+2]
            if bk_color == (184, 40, 65) and color == 16777215:
                # Combine text for titlu unitate
                html = f"""
        <div class="center">
            <h1 class="titlu-unitate">
                <span class="text-unitate">UNITATEA<br/><span class="numar-unitate">{text3}</span></span>
            {text2}
            </h1>
        </div>
        <p class="clear"></p>\n
        """
                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
                i += 3
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list


def bkgr_read(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][4] in [(255, 253, 232), (255, 243, 222), (255, 253, 233)]:
            # bkgr_read
            html = f"""
        <div class="bkgr-read">
            <p>{text_attributes_list[i][0]}</p>
        </div>\n"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def bkgr_pers(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 10.779999732971191 and text_attributes_list[i][2] == 'PTSans-Regular' and text_attributes_list[i][4] in [(235, 247, 248), (234, 246, 247)]:
            # bkgr_pers
            html = f"""
                <div class="bkgr-pers">
                        <p>{text_attributes_list[i][0]}</p>
                    </div>\n
                    """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def text_imp(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    imp_text = ""
    # print(text_attributes_list)
    while i < len(text_attributes_list):
        if text_attributes_list[i][0].strip() == 'Important' or text_attributes_list[i][0].strip() == 'Concluzii' or text_attributes_list[i][0].strip() == 'Concluzii:':
            html = f"""
        <h3 class="important">{text_attributes_list[i][0].strip()}</h3>"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif text_attributes_list[i][4] in [(258, 0, 0), (237, 246, 231), (238, 246, 232), (236, 240, 231), (233, 244, 232), (232, 244, 231)]:
            imp_text += text_attributes_list[i][0]
            i += 1
        else:
            if imp_text:

                html = f"""
            <div class="bkgr-imp">
            {imp_text}
            </div>
                """
                html = html.replace('\u2007', '')

                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
                imp_text = ""
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    if imp_text:
        html = f"""
        <div class="bkgr-imp">
        {imp_text}
        </div>
        """

        new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
    return new_text_attributes_list


def text_galben(text_attributes_list):
    # fizica
    new_text_attributes_list = []
    i = 1
    if text_attributes_list[0][4] in [(254, 243, 229), (255, 244, 230)]:
        html_galben = text_attributes_list[0][0]
    else:
        html_galben = ""
        new_text_attributes_list = [text_attributes_list[0]]

    while i < len(text_attributes_list):
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if bkgr_color in [(254, 243, 229), (255, 244, 230)]:
            html_galben += text_attributes_list[i][0]
            i += 1
        elif (bkgr_color not in [(254, 243, 229), (255, 244, 230)] and text_attributes_list[i-1][4] in [(254, 243, 229), (255, 244, 230)]) or (text_attributes_list[i] == text_attributes_list[-1]):

            html_galben = f"""
            <div class="bkgr-yellow">
            <p>{html_galben}</p>
            </div>
            """
            if html_galben != f"""
            <div class="bkgr-yellow">
            <p></p>
            </div>
            """:
                new_text_attributes_list.append([html_galben, 0, '0', 0, (257, 0, 0)])

            new_text_attributes_list.append(text_attributes_list[i])
            html_galben = ""
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def paragraph(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if size == 11.5 and font == 'MinionPro-Regular' and bkgr_color == (255, 255, 255):
            # paragraph
            html = f"""
            <p>{text_attributes_list[i][0]}</p>
            """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def text_mov(text_attributes_list):
    # chimie
    new_text_attributes_list = []
    i = 1
    if text_attributes_list[0][4] in [(231, 223, 237)]:
        html_mov = text_attributes_list[0][0]
    else:
        html_mov = ""
        new_text_attributes_list = [text_attributes_list[0]]

    while i < len(text_attributes_list):
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if bkgr_color in [(231, 223, 237), (233, 225, 239)]:
            html_mov += text_attributes_list[i][0]
            i += 1
        elif (bkgr_color not in [(231, 223, 237)] and text_attributes_list[i-1][4] in [(231, 223, 237)]) or (text_attributes_list[i] == text_attributes_list[-1]):

            html_mov = f"""
            <div class="bkgr-purple">
            <p>{html_mov}</p>
            </div>
            """
            if html_mov != f"""
            <div class="bkgr-purple">
            <p></p>
            </div>
            """:
                new_text_attributes_list.append([html_mov, 0, '0', 0, (257, 0, 0)])

            new_text_attributes_list.append(text_attributes_list[i])
            html_mov = ""
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def text_blue(text_attributes_list):
    # mate
    new_text_attributes_list = []
    i = 1
    if text_attributes_list[0][4] in [(224, 234, 247)]:
        html_blue = text_attributes_list[0][0]
    else:
        html_blue = ""
        new_text_attributes_list = [text_attributes_list[0]]

    while i < len(text_attributes_list):
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if bkgr_color in [(224, 234, 247)]:
            html_blue += text_attributes_list[i][0]
            i += 1
        elif (bkgr_color not in [(224, 234, 247)] and text_attributes_list[i-1][4] in [(224, 234, 247)]) or (text_attributes_list[i] == text_attributes_list[-1]):

            html_blue = f"""
            <div class="exemple">
            <p>{html_blue}</p>
            </div>
            """
            if html_blue != f"""
            <div class="exemple">
            <p></p>
            </div>
            """:
                new_text_attributes_list.append([html_blue, 0, '0', 0, (257, 0, 0)])

            new_text_attributes_list.append(text_attributes_list[i])
            html_blue = ""
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list


def text_model(text_attributes_list):
    # mate
    new_text_attributes_list = []
    i = 1
    if text_attributes_list[0][4] in [(224, 222, 239)]:
        html_model = text_attributes_list[0][0]
    else:
        html_model = ""
        new_text_attributes_list = [text_attributes_list[0]]

    while i < len(text_attributes_list):
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if bkgr_color in [(224, 222, 239)]:
            html_model += text_attributes_list[i][0]
            i += 1
        elif (bkgr_color not in [(224, 222, 239)] and text_attributes_list[i-1][4] in [(224, 222, 239)]) or (text_attributes_list[i] == text_attributes_list[-1]):

            html_model = f"""
            <div class="background-model">
            <p>{html_model}</p>
            </div>
            """
            if html_model != f"""
            <div class="background-model">
            <p></p>
            </div>
            """:
                new_text_attributes_list.append([html_model, 0, '0', 0, (257, 0, 0)])

            new_text_attributes_list.append(text_attributes_list[i])
            html_model = ""
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list

def titlu_unitate_03mat(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    # print(text_attributes_list)


    new_new_text_attributes_list = []
    previous_text = ""
    previous_size = 0
    previous_font = ""
    previous_color = 0
    previous_bg_color = (0, 0, 0)
    for element in text_attributes_list:
        text, size, font, color, bg_color = element
        if (previous_size == 16.0 and size == 16 and previous_color == 27537 and color == 27537 and previous_font == 'Roboto-Bold' and font == 'Roboto-Bold') or (previous_size == 18.0 and size == 18 and previous_color == 16777215 and color == 16777215 and previous_font == 'Roboto-Bold' and font == 'Roboto-Bold' and previous_bg_color == (98, 199, 204) and bg_color == (98, 199, 204)):
            if previous_text[-1] in ['ț', 'ș']:
                previous_text += text
            else:
                previous_text += " " + text
        else:
            if previous_text:
                new_new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color, previous_bg_color])
            previous_text = text
            previous_size = size
            previous_font = font
            previous_color = color
            previous_bg_color = bg_color

    if previous_text:
        new_new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color, previous_bg_color])
    # print(new_new_text_attributes_list)

    n = len(new_new_text_attributes_list)
    while i < n:
        if i < n-3:
            text, size, font, color, bk_color = new_new_text_attributes_list[i]
            if bk_color == (98, 199, 204):
                # Combine text for titlu unitate
                html = f"""
        <div class="center">
            <h1 class="titlu-unitate">
                <span class="text-unitate">Unitatea<br/><span class="numar-unitate"></span></span>
            {text}
            </h1>
        </div>
        <p class="clear"></p>\n
        """
                new_text_attributes_list.insert(0, [html, 0, '0', 0, (257, 0, 0)])
                i += 1
            else:
                new_text_attributes_list.append(new_new_text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(new_new_text_attributes_list[i])
            i += 1
    return new_text_attributes_list