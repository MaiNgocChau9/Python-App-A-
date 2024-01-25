        background = self.capture_widget_background(main_widget)
        palette = main_widget.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QColor(255, 255, 255, 128), Qt.BrushStyle.SolidPattern))
        main_widget.setPalette(palette)
