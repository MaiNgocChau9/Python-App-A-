    print("Something very cool",task)
                print("Item:",item.text())
                check_state = item.checkState()
                if check_state == QtCore.Qt.CheckState.Unchecked:
                    local_item.append(task)
                    print(local_item)
                if check_state == QtCore.Qt.CheckState.Checked:
                    local_item.remove(task)
                    print(local_item)
                if task == local_item[-1]:
                    break