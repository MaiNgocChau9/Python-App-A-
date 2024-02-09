with open("data\\account.ecl", "r+", encoding='utf-8') as f:
                        f.write(f"logged: {logged}\naccount: {self.lineEdit.text()}")