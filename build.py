def build_html(data, output_path):
    html_content = f"""<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" type="text/css" rel="stylesheet" />
        <link href="stylesheet.css" type="text/css" rel="stylesheet" />
    </head>

    <body>
        <div>
    """

    i = 0
    while i < len(data):
        text, font_size, font_type, color, bg_color = data[i]
        if font_size == 100 and font_type == '100' and color == 100:
            # Titlu unitate
            html_content += text
        elif font_size == 101 and font_type == '101' and color == 101:
            # Titlu
            html_content += text
        elif font_size == 102 and font_type == '102' and color == 102:
            # Nume autor
            html_content += text
        elif font_size == 103 and font_type == '103' and color == 103:
            # bkgr_read
            html_content += text
        elif font_size == 104 and font_type == '104' and color == 104:
            # bkgr_read
            html_content += text
        elif font_size == 105 and font_type == '105' and color == 105:
            # exercitiu
            html_content += text
        elif font_size == 106 and font_type == '106' and color == 106:
            # nume paragraf
            html_content += text
        elif font_size == 108 and font_type == '108' and color == 108:
            # patrat albastru
            html_content += text
        elif font_size == 109 and font_type == '109' and color == 109:
            # portofoliu
            html_content += text
        elif font_size == 110 and font_type == '110' and color == 110:
            # portofoliu
            html_content += text
        elif font_size == 111 and font_type == '111' and color == 111:
            # paragraph
            html_content += text
        i += 1
    html_content += """
        </div>
    </body>
</html>
    """

    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)