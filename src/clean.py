def clean_text(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        text_attributes_list[i][0] = text_attributes_list[i][0].replace('\x07', ' ')
        text_attributes_list[i][0] = text_attributes_list[i][0].replace('\xa0', ' ')
        text, size, font, color, bkgr_color = text_attributes_list[i]
        if size == 10.0 and font == 'MinionPro-Bold':
            # Remove page number
            i += 1
        elif text == ' ':
            # Remove empty spaces
            i += 1
        elif text == "\uf072":
            # remove formule mate
            i += 1
        elif font == 'TimesNewRomanPS-ItalicMT' or font == 'TimesNewRomanPSMT':
            # remove alte formule mate
            i += 1
        elif 6.24370002746582 <= size <= 6.704500198364258:
            # remove alte alte formule mate
            i += 1
        elif (size == 9.0
              and font == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i + 1][0] == ' – Manual pentru clasa a VII-a'):
            # remove text de langa nr paginii
            i += 5
        elif bkgr_color == (255, 241, 214):
            # remove textul de la 'Citeste si'
            i += 1
        elif text == 'Citește și...' and size == 14.0 and font == 'ITCKabelStd-BoldRO':
            # Remove 'Citește și...' (se pune poza)
            i += 1
        elif text == '\u2003':
            # Remove 'Citește și...' (se pune poza)
            i += 1
        elif font == 'SymbolMT' and text.strip() != '•':
            # remove math symbols
            i += 1

        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list