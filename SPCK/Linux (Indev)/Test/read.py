# import os
# import html2text
# from bs4 import BeautifulSoup

# all_notes = os.listdir("All Notes")
# for note_name in all_notes:
#     print(note_name)
#     with open(f"All Notes\\{note_name}", 'r', encoding = 'utf-8') as file:
#         print(file.read())


import html2text
with open("All Notes\\Lần bầu cử đa chủng tộc đầu tiên ở Cộng Hòa Nam Phi", 'r', encoding = 'utf-8') as file: html_code = file.read()
print(html2text.html2text(html_code))