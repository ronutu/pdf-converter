# This file is part of pdf-convertor.
#
# pdf-convertor is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pdf-convertor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdf-convertor. If not, see <https://www.gnu.org/licenses/>.

def combine_text(text_attributes_list):  # Combines the text with the same size and font
    new_text_attributes_list = []
    previous_text = ""
    previous_size = 0
    previous_font = ""
    previous_color = 0
    previous_bg_color = (0, 0, 0)
    for element in text_attributes_list:
        text, size, font, color, bg_color = element
        if previous_size - 0.2 <= size <= previous_size + 0.2 and font == previous_font and bg_color == previous_bg_color:
            previous_text += " " + text
        else:
            if previous_text:
                new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color,
                                                 previous_bg_color])
            previous_text = text
            previous_size = size
            previous_font = font
            previous_color = color
            previous_bg_color = bg_color

    if previous_text:
        new_text_attributes_list.append([previous_text, previous_size, previous_font, previous_color,
                                         previous_bg_color])

    return new_text_attributes_list


def combine_patrat_albastru(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)
    string_patrate = ""
    while i < n:
        if i < n-1:
            if (text_attributes_list[i][0] == '�' and text_attributes_list[i][1] == 10.779999732971191 and
                    text_attributes_list[i][2] == 'Wingdings-Regular' and text_attributes_list[i][3] == 32197):
                string_patrate += (f"""
                                   <li>{text_attributes_list[i+1][0]}</li>
                                   """)
                i += 2
            else:
                if string_patrate:
                    new_text_attributes_list.append([string_patrate, 107, '107', 107])
                    string_patrate = ""
                else:
                    new_text_attributes_list.append(text_attributes_list[i])
                i += 1
        else:
            new_text_attributes_list.append(text_attributes_list[i])
            i += 1

    new_new_text_attributes_list = []
    i = 0
    n = len(new_text_attributes_list)
    while i < n:
        if (new_text_attributes_list[i][1] == 107 and new_text_attributes_list[i][2] == '107'
                and new_text_attributes_list[i][3] == 107):
            html = f"""
            <ul class="ulsquare">
                {new_text_attributes_list[i][0]}
            </ul>
            """
            new_new_text_attributes_list.append([html, 108, '108', 108, (1, 0, 8)])
            i += 1
        else:
            new_new_text_attributes_list.append(new_text_attributes_list[i])
            i += 1

    return new_new_text_attributes_list


def combine_exercitiu(text_attributes_list):
    new_text_attributes_list = []
    i = 0
    n = len(text_attributes_list)

    while i < n:
        if i < n-1:
            if (text_attributes_list[i][0] == 'Portofoliu' and text_attributes_list[i][1] == 14.0
                    and text_attributes_list[i][2] == 'ITCKabelStd-BoldRO' and text_attributes_list[i][3] == 16777215):
                # portofoliu
                html = f"""<h3 class="portofoliu">Portofoliu</h3>
                            <div class="block-container">
                                <span class="number portofoliu">{text_attributes_list[i+1][0]}</span>
                                <div class="block-number-content">
                                    <p>
                                        {text_attributes_list[i+2][0]}
                                    </p>
                                </div>
                            </div>"""
                new_text_attributes_list.append([html, 110, '110', 110, (1, 1, 0)])
                i += 3
            elif (text_attributes_list[i][1] == 9.899495124816895 and text_attributes_list[i][2] == 'PTSans-Bold'
                  and text_attributes_list[i+1][1] == 10.779999732971191
                  and text_attributes_list[i+1][2] == 'PTSans-Regular'):
                # exercitiu pt sans regular
                html = f"""
                    <div class="block-container">
                        <span class="number u7">{text_attributes_list[i][0]}</span>
                        <div class="block-number-content">
                            <p>{text_attributes_list[i+1][0]}</p>
                        </div>
                    </div>
                    <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 105, '105', 105, (1, 0, 5)])
                i += 2
            elif (text_attributes_list[i][1] == 9.899495124816895 and text_attributes_list[i][2] == 'PTSans-Bold'
                  and text_attributes_list[i+1][1] == 11.384419441223145
                  and text_attributes_list[i+1][2] == 'MinionPro-Regular'):
                # exercitiu pt info
                html = f"""
                    <div class="block-container">
                        <span class="number u7">{text_attributes_list[i][0]}</span>
                        <div class="block-number-content">
                            <p>{text_attributes_list[i+1][0]}</p>
                        </div>
                    </div>
                    <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 105, '105', 105, (1, 0, 5)])
                i += 2
            elif (text_attributes_list[i][1] == 9.899495124816895 and text_attributes_list[i][2] == 'PTSans-Bold'
                  and text_attributes_list[i+1][1] == 11.270000457763672
                  and text_attributes_list[i+1][2] == 'MinionPro-Regular'):
                # exercitiu pt minion pro regular
                html = f"""
                    <div class="block-container">
                        <span class="number u7">{text_attributes_list[i][0]}</span>
                        <div class="block-number-content">
                            <p>{text_attributes_list[i+1][0]}</p>
                        </div>
                    </div>
                    <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 105, '105', 105, (1, 0, 5)])
                i += 2
            elif (text_attributes_list[i][1] == 9.899495124816895 and text_attributes_list[i][2] == 'PTSans-Bold'
                  and text_attributes_list[i+1][1] == 11.154407501220703
                  and text_attributes_list[i+1][2] == 'MinionPro-Regular'):
                # exercitiu pt minion pro regular alt font size
                html = f"""
                    <div class="block-container">
                        <span class="number u7">{text_attributes_list[i][0]}</span>
                        <div class="block-number-content">
                            <p>{text_attributes_list[i+1][0]}</p>
                        </div>
                    </div>
                    <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 105, '105', 105, (1, 0, 5)])
                i += 2
            elif (text_attributes_list[i][1] == 9.899495124816895 and text_attributes_list[i][2] == 'PTSans-Bold' and
                  text_attributes_list[i+1][1] == 10.444787979125977
                  and text_attributes_list[i+1][2] == 'PTSans-Regular'):
                # exercitiu pt sans regular font size mai mic
                html = f"""
                    <div class="block-container">
                        <span class="number u7">{text_attributes_list[i][0]}</span>
                        <div class="block-number-content">
                            <p>{text_attributes_list[i+1][0]}</p>
                        </div>
                    </div>
                    <p class="clear"></p>\n
                    """
                new_text_attributes_list.append([html, 105, '105', 105, (1, 0, 5)])
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
