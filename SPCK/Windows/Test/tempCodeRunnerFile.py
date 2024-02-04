    def insert_image(self):
        # Lấy tên file ảnh
        filename, _ = QFileDialog.getOpenFileName(self, 'Chèn ảnh', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")

        if filename:
            # Tạo đối tượng ảnh
            image = QImage(filename)

            # Báo lỗi nếu không thể load ảnh
            if image.isNull():
                popup = QMessageBox(QMessageBox.Critical,
                                    "Lỗi khi tải ảnh",
                                    "Không thể tải được tệp ảnh!",
                                    QMessageBox.Ok,
                                    self)
                popup.show()
            else:
                cursor = self.text_edit.textCursor()
                cursor.insertImage(image, filename)