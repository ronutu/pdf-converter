# ─── src/main.py ───────────────────────────────────────────────────────────────
"""
If called with **no** extra arguments -> launch the old Tk GUI exactly
as before.

If called with two or three extra arguments:
    python src/main.py  <pdf_path>  <output_html>  [<page_nr>]

it skips Tk-inter completely, extracts the requested page (default 0)
and writes the HTML file.
"""
import os
import sys

import build
import gui  # we re-use apply_changes() that you already wrote


def batch_convert(pdf_path: str, output_path: str, page_nr: int = 0) -> None:
    text = gui.apply_changes(pdf_path, page_nr)
    build.build_html(text, output_path, page_nr)


def main() -> None:
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        pdf_path = sys.argv[1]
        output_path = sys.argv[2]
        page_nr = int(sys.argv[3]) if len(sys.argv) == 4 else 0
        # Ensure the output directory exists (avoids FileNotFoundError)
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        batch_convert(pdf_path, output_path, page_nr)
    else:
        # Classic desktop workflow – still launches the file picker
        gui.create_question_box()


if __name__ == "__main__":
    main()
