        for task in self.all_task:
            item = QtWidgets.QListWidgetItem(task)
            item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.listWidget.addItem(item)