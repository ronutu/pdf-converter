import pandas as pd


def clean_text(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
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
        elif (text == 'Limba și literatura română' and size == 9.0
              and font == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif (text == 'Fizică' and size == 9.0
              and font == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif (text == 'Informatică și TIC' and size == 9.0
              and font == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif bkgr_color == (1.0, 0.9450980392156862, 0.8392156862745098):
            # remove textul de la 'Citeste si'
            i += 1
        elif text == 'Citește și...' and size == 14.0 and font == 'ITCKabelStd-BoldRO':
            # Remove 'Citește și...' (se pune poza)
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    return new_text_attributes_list
