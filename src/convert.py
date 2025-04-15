def pdf_to_html(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    # print(text_attributes_list)
    while i < n:
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if size == 15.0 and font in ['ITCKabelStd-BoldRO'] and color == 8399247:

            # Titlu
            html = f"""
        <h2>{text}</h2>"""
            new_text_attributes_list.insert(0, [html, 0, '0', 0, (257, 0, 0)])
            i += 1

        elif (size == 14.0 and font == 'ITCKabelStd-BoldRO' and
              color == 16777215 and text.strip() not in ['Portofoliu', 'Important', 'Autoevaluare',
                                                         'Organizarea portofoliului', 'Concluzii', 'Concluzii:']):
            #  nume paragraf
            html = f"""
       <h3>{text}</h3>
       <p class="clear"></p>
               """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1

        elif size in [11.270000457763672, 10.21099853515625] and font == 'PTSans-Regular':
            # Nume autor
            html = f"""
        <h5>{text}</h5>"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1

        elif 10 < size < 11 and font == 'PTSans-Italic':
            # Italic PTSans
            html = f"""<span class="italic">{text}</span>"""
            new_text_attributes_list.append([html, size, 'PTSans-Regular', color, bkgr_color])
            i += 1

        elif (10.5 <= size <= 11.5 or size == 10.800000190734863) and font == 'MinionPro-It':
            # Italic MinionPro
            html = f"""<span class="italic">{text}</span>"""
            new_text_attributes_list.append([html, size, 'MinionPro-Regular', color, bkgr_color])
            i += 1

        elif size == 12 and font == 'Roboto-LightItalic':
            # Italic MinionPro
            html = f"""<span class="italic">{text}</span>"""
            new_text_attributes_list.append([html, size, 'Roboto-Light', color, bkgr_color])
            i += 1

        elif 10 <= size <= 11.6 and font == 'MinionPro-Bold' and color == 2236191 and text.strip() != '•':
            # Bold MinionPro
            html = f"""<span class="bold">{text.strip()}</span>"""
            new_text_attributes_list.append([html, 10.779999732971191, 'MinionPro-Regular', color, bkgr_color])
            i += 1

        elif 10 <= size <= 11 and font == 'PTSans-Bold' and color == 2236191:
            # Bold PTSans
            html = f"""<span class="bold">{text.strip()}</span>"""
            new_text_attributes_list.append([html, size, 'PTSans-Regular', color, bkgr_color])
            i += 1

        elif 10 <= size <= 11 and font == 'PTSans-Bold' and color == 9710926:
            # Nume autor maro
            html = f"""<span class="bold color-marsala">{text}</span>"""
            new_text_attributes_list.append([html, size, 'PTSans-Regular', 2236191, bkgr_color])
            i += 1
        elif (size == 14.0 and font == 'ITCKabelStd-BoldRO' and
              color == 7611011 and text != 'Portofoliu'
              and text != 'Important' and text != 'Organizarea portofoliului'):
            # nume paragraf
            html = f"""
        <h2 class="lesson-title">{text}</h2>"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif size == 14.0 and bkgr_color == (237, 19, 90):
            # observ
            html = f"""
         <h3 class="observ">Observ!</h3>
         <p class="clear"></p>
                 """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1

        elif (text == 'Experiment' and size == 14.0
              and font == 'ITCKabelStd-BoldRO'):
            # Experiment
            html = f"""
                        <p class="experiment">Experiment</p>
                    """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif text == 'Autoevaluare' and size == 14.0 and font == 'ITCKabelStd-BoldRO':
            # Autoevaluare
            html = f"""
        <h3 class="important">Autoevaluare</h3>
        """
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif (size == 11.5 and font == 'MinionPro-Bold'
              and color == 32197):
            # text albastru
            html = f"""<span class="bold color-turcoaz">{text}</span>"""
            if bkgr_color in [(258, 0, 0), (237, 246, 231), (238, 246, 232)]:
                new_text_attributes_list.append([html, size, font, 2236191, bkgr_color])
            else:
                new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif font == 'LMSans10-Bold' and size == 10.909099578857422 and color == 32197:
            # exemplu
            html = f"""<span class="exemplu">{text}</span>"""
            new_text_attributes_list.append([html, size, 'LMSans10-Regular', 2236191, bkgr_color])
            i += 1
        elif font == 'LMSans10-Bold' and size == 10.909099578857422 and color == 3027090:
            # model
            html = f"""<span class="model">{text}</span>"""
            new_text_attributes_list.append([html, size, 'LMSans10-Regular', 2236191, bkgr_color])
            i += 1
        elif size == 11.5 and font == 'MinionPro-Bold' and color == 7611011:
            # text mov
            html = f"""<span class=" bold color-purple">{text}</span>"""
            new_text_attributes_list.append([html, size, 'MinionPro-Regular', 2236191, bkgr_color])
            i += 1

        elif size == 11.5 and font == 'ITCKabelStd-BoldRO' and color == 7611011:
            # text mov
            html = f"""<span class=" bold color-purple">{text}</span>"""
            new_text_attributes_list.append([html, size, 'MinionPro-Regular', 2236191, bkgr_color])
            i += 1

        elif font == 'PTSans-Bold' and color == 14295079:
            # text rosu cu bold
            html = f"""<span class="color-red bold">{text}</span>"""
            new_text_attributes_list.append([html, size, 'PTSans-Regular', 2236191, bkgr_color])
            i += 1

        elif font == 'PTSans-BoldItalic' and color == 2236191:
            # PTSans bold italic
            html = f"""<span class="italic bold">{text.strip()}</span>"""
            new_text_attributes_list.append([html, size, 'PTSans-Regular', color, bkgr_color])
            i += 1

        elif font == 'MinionPro-BoldIt' and color == 2236191:
            # MinionPro bold italic
            html = f"""<span class="italic bold">{text.strip()}</span>"""
            new_text_attributes_list.append([html, size, 'MinionPro-Regular', color, bkgr_color])
            i += 1
        elif font == 'Itim-Regular':
            # Titlu text
            html = f"""
        <h4>{text}</h4>"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif (bkgr_color in [(236, 0, 140), (236, 0, 139)] or text == 'Organizarea portofoliului') and text not in ['Important']:
            # portofoliu
            html = f"""
        <h3 class="portofoliu">{text}</h3>"""
            new_text_attributes_list.append([html, 0, '0', 0, (257, 0, 0)])
            i += 1
        elif text.strip() == '•' and size in [11.5, 11.030412673950195, 11.557356834411621] and font in ['MinionPro-Bold', 'SymbolMT', 'ITCKabelStd-BoldRO']:
            new_text_attributes_list.append([text, size, 'MinionPro-Regular', color, bkgr_color])
            i += 1
        elif i < n-1:
            text2, size2, font2, color2, bkgr_color2 = text_attributes_list[i+1]
            if text[-1] == 't' and text2 == ',' and size2 == 5.97760009765625:
                # diacritice
                text = text[:-1] + 'ț'
                new_text_attributes_list.append([text, size, font, color, bkgr_color])
                i += 2
            elif text[-1] == 's' and text2 == ',' and size2 == 5.97760009765625:
                # diacritice
                text = text[:-1] + 'ș'
                new_text_attributes_list.append([text, size, font, color, bkgr_color])
                i += 2
            else:
                new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1


    # print(new_text_attributes_list)
    return new_text_attributes_list