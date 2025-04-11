def build_html(data, output_path, page_nr):
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
        if font_size == 0 and font_type == "0" and color == 0:
            html_content += text
        i += 1
    html_content += """
        </div>
    </body>
</html>
    """

    with open(output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
