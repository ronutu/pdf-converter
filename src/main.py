"""pdf-converter - PDF to HTML converter."""

# This file is part of pdf-converter.
#
# pdf-converter is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pdf-converter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pdf-converter. If not, see <https://www.gnu.org/licenses/>.


import time
from datetime import timedelta

import gui

start_time = time.time()


def main() -> None:
    """Main function to run the GUI."""
    gui.create_question_box()


main()

elapsed = time.time() - start_time
FORMATTED_ELAPSED = str(timedelta(seconds=int(elapsed)))
print(f"Elapsed time: {FORMATTED_ELAPSED}")
