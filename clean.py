def clean_text(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    while i < n:
        if text_attributes_list[i][1] == 10.0 and text_attributes_list[i][2] == 'MinionPro-Bold':
            # Remove page number
            i += 1
        elif text_attributes_list[i][0] == ' ':
            # Remove empty spaces
            i += 1
        elif text_attributes_list[i][0] == "\uf072":
            # remove formule mate
            i += 1
        elif text_attributes_list[i][2] == 'TimesNewRomanPS-ItalicMT' or text_attributes_list[i][2] == 'TimesNewRomanPSMT':
            # remove alte formule mate
            i += 1
        elif 6.24370002746582 <= text_attributes_list[i][1] <= 6.704500198364258:
            # remove alte alte formule mate
            i += 1
        elif (text_attributes_list[i][0] == 'Limba și literatura română' and text_attributes_list[i][1] == 9.0
              and text_attributes_list[i][2] == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif (text_attributes_list[i][0] == 'Fizică' and text_attributes_list[i][1] == 9.0
              and text_attributes_list[i][2] == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif (text_attributes_list[i][0] == 'Informatică și TIC' and text_attributes_list[i][1] == 9.0
              and text_attributes_list[i][2] == 'ITCKabelStd-MediumRO'
              and text_attributes_list[i+1][0] == ' – Manual pentru clasa a VII-a'
              and text_attributes_list[i+1][1] == 9.0 and text_attributes_list[i+1][2] == 'ITCKabelStd-BookRO'
              and text_attributes_list[i+2][0] == 'Unitatea' and text_attributes_list[i+2][1] == 9.0
              and text_attributes_list[i+2][2] == 'ITCKabelStd-BookRO' and text_attributes_list[i+3][1] == 10.0
              and text_attributes_list[i+3][2] == 'MinionPro-Bold'
              and text_attributes_list[i+4][1] == 11.0 and text_attributes_list[i+4][2] == 'ITCKabelStd-UltraRO'):
            # remove text de langa nr paginii
            i += 5
        elif text_attributes_list[i][4] == (1.0, 0.9450980392156862, 0.8392156862745098):
            # remove textul de la 'Citeste si'
            i += 1
        elif text_attributes_list[i][0] == 'Citește și...' and text_attributes_list[i][1] == 14.0 and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO':
            # Remove 'Citește și...' (se pune poza)
            i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1
    return new_text_attributes_list
