    def save_edit(self):
        global note_name
        tree = ET.ElementTree(ET.Element('notes'))
        root = tree.getroot()

        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start, QTextCursor.MoveMode.MoveAnchor)

        while not cursor.atEnd():
            block = cursor.block()
            char_format = block.charFormat()

            note_element = ET.SubElement(root, 'note')
            text_element = ET.SubElement(note_element, 'text')
            text_element.text = block.text()

            font_element = ET.SubElement(note_element, 'font')
            font_element.text = char_format.font().toString()

            weight_element = ET.SubElement(note_element, 'weight')
            weight_element.text = str(char_format.fontWeight())

            italic_element = ET.SubElement(note_element, 'italic')
            italic_element.text = str(char_format.fontItalic())

            cursor.movePosition(QTextCursor.MoveOperation.NextBlock)
            print(cursor.atEnd())

        tree.write(f"All Notes\\{note_name}.xml")