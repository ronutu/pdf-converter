def pdf_to_html(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 18.0 and text_attributes_list[i][2] == 'PTSans-Bold':
            # Titlu romana
            html = f"""
            <h2>{text_attributes_list[i][0]}</h2>
            """
            new_text_attributes_list.append([html, 101, '101', 101, (1, 0, 1)])
            i += 1
        elif text_attributes_list[i][1] == 18.0 and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO':
            # Titlu fizica
            html = f"""
            <h2>{text_attributes_list[i][0]}</h2>
            """
            new_text_attributes_list.append([html, 101, '101', 101, (1, 0, 1)])
            i += 1
        elif text_attributes_list[i][1] == 11.270000457763672 and text_attributes_list[i][2] == 'PTSans-Regular':
            # Nume autor
            html = f"""
            <h5>{text_attributes_list[i][0]}</h5>
            """
            new_text_attributes_list.append([html, 102, '102', 102, (1, 0, 2)])
            i += 1
        elif text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-It':
            # Italic minion
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.5, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 10.889444351196289 and text_attributes_list[i][2] == 'PTSans-Italic':
            # Italic pt sans
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 10.779999732971191, 'PTSans-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.270000457763672 and text_attributes_list[i][2] == 'MinionPro-It':
            # Italic minion pro
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.270000457763672, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif 11.326186180114746 <= text_attributes_list[i][1] <= 11.384419441223145 and text_attributes_list[i][2] == 'MinionPro-It':
            # Italic minion pro mai mare
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.5, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.154407501220703 and text_attributes_list[i][2] == 'MinionPro-It':
            # Italic minion pro intre
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.154407501220703, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 10.800000190734863 and text_attributes_list[i][2] == 'MinionPro-It':
            # Italic minion pro intre
            html = f"""<span class="italic">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.5, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-Bold' and text_attributes_list[i][3] == 2236191:
            # bold minion pro
            html = f"""<span class="bold">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 11.5, 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.384419441223145 and text_attributes_list[i][2] == 'MinionPro-Bold' and text_attributes_list[i][3] == 2236191:
            # bold minion pro
            html = f"""<span class="bold">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, text_attributes_list[i][1], 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif text_attributes_list[i][1] == 11.44235610961914 and text_attributes_list[i][2] == 'MinionPro-Bold' and text_attributes_list[i][3] == 2236191:
            # alt bold minion pro
            html = f"""<span class="bold">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, text_attributes_list[i][1], 'MinionPro-Regular', text_attributes_list[i][3],
                                             text_attributes_list[i][4]])
            i += 1
        elif (text_attributes_list[i][1] == 10.779999732971191 and text_attributes_list[i][2] == 'PTSans-Bold'
              and text_attributes_list[i][3] == 9710926):
            # Nume autor maro
            html = f"""<span class="bold color-marsala">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, text_attributes_list[i][1], 'PTSans-Regular', 2236191,
                                             text_attributes_list[i][4]])
            i += 1
        elif (text_attributes_list[i][1] == 14.0 and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO' and
              text_attributes_list[i][3] == 7611011 and text_attributes_list[i][0] != 'Portofoliu'
              and text_attributes_list[i][0] != 'Important'):
            # nume paragraf
            html = f"""<h3><span class="italic">{text_attributes_list[i][0]}</span></h3>"""
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1
        elif (text_attributes_list[i][1] == 14.0 and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO' and
              text_attributes_list[i][3] == 16777215 and text_attributes_list[i][0] != 'Portofoliu' and
              text_attributes_list[i][0].strip() != 'Important' and text_attributes_list[i][0] != "Autoevaluare"):
            # alt nume paragraf
            html = f"""
                        <h3>{text_attributes_list[i][0]}</h3>
                        <p class="clear"></p>
                    """
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1
        elif (text_attributes_list[i][0] == 'Experiment' and text_attributes_list[i][1] == 14.0
              and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO'):
            # Experiment
            html = f"""
                        <p class="experiment">Experiment</p>
                    """
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1
        elif (text_attributes_list[i][0] == 'Autoevaluare' and text_attributes_list[i][1] == 14.0
              and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO'):
            # Autoevaluare
            html = f"""
                        <p class="experiment">Experiment</p>
                    """
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1
        elif (text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-Bold'
              and text_attributes_list[i][3] == 32197):
            # text albastru
            html = f"""<span class="bold color-turcoaz">{text_attributes_list[i][0]}</span>"""
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1
        elif (text_attributes_list[i][1] == 11.5 and text_attributes_list[i][2] == 'MinionPro-Bold'
              and text_attributes_list[i][3] == 7611011):
            # text mov
            html = f"""<p class=" bold color-purple">{text_attributes_list[i][0]}</p>"""
            new_text_attributes_list.append([html, 106, '106', 106, (1, 0, 6)])
            i += 1

        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list
