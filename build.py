import mysql.connector
import re


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
        if font_size == 0 and font_type == '0' and color == 0:
            html_content += text
        i += 1
    html_content += """
        </div>
    </body>
</html>
    """

    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    filename = re.search(r'\\([^\\]+)\\', output_path).group(1)

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="radu",
        password="1235",
        database="manuale"
    )
    page_nr = str(page_nr)
    mycursor = mydb.cursor()
    for row in data:
        # if row[1] != 0 and row[2] != '0' and row[3] != 0:
        sql = f"INSERT INTO {filename} (page_nr, text, size, font, color, bg_color) VALUES (%s, %s, %s, %s, %s, %s)"
        text = row[0][:5000]
        val = (page_nr, text, row[1], row[2], row[3], ','.join(map(str, row[4])))
        mycursor.execute(sql, val)
    mydb.commit()
