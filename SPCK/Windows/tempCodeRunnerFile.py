    def save_edit(self):
        global note_name
        with open(f"All Notes\\{note_name}", 'w', encoding='utf-8') as file:
            cursor = self.textEdit.textCursor()

            # Di chuyển con trỏ về đầu văn bản
            cursor.movePosition(QTextCursor.MoveOperation.Start, QTextCursor.MoveMode.MoveAnchor)

            # Lặp qua từng đoạn trong văn bản
            while not cursor.atEnd():
                # Lấy định dạng của đoạn hiện tại
                block = cursor.block()
                char_format = block.charFormat()

                # Ghi thông tin định dạng vào tệp tin
                file.write(f"{block.text()}|{char_format.font().toString()}|{char_format.fontWeight()}|{char_format.fontItalic()}\n")

                # Di chuyển con trỏ đến đoạn tiếp theo
                cursor.movePosition(QTextCursor.MoveOperation.NextBlock, QTextCursor.MoveMode.MoveAnchor)