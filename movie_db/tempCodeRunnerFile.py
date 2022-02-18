reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes: