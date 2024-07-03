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


import time
import gui

start_time = time.time()


def main():
    gui.create_question_box()


main()

print("--- %s seconds ---" % (time.time() - start_time))