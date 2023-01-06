import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTextEdit widget and set it as the central widget
        # of the main window
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Create the "Open" action
        open_action = QAction(QIcon('open.png'), 'Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_text)

        # Create the "Save" action
        save_action = QAction(QIcon('save.png'), 'Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_text)

        # Create the "Undo" action
        undo_action = QAction(QIcon('undo.png'), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit.undo)

        # Create the "Redo" action
        redo_action = QAction(QIcon('redo.png'), 'Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit.redo)

        # Create the "Find" action
        find_action = QAction(QIcon('find.png'), 'Find', self)
        find_action.setShortcut('Ctrl+F')
        find_action.triggered.connect(self.find_text)

        # Add the "Open", "Save", "Undo", "Redo", and "Find" actions to the toolbar
        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addAction(undo_action)
        self.toolbar.addAction(redo_action)
        self.toolbar.addAction(find_action)

        # Create a line edit for entering the search text
        self.find_edit = QLineEdit(self)
        self.find_edit.setClearButtonEnabled(True)
        self.find_edit.returnPressed.connect(self.find_text)

        # Add the find line edit to the toolbar
        self.toolbar.addWidget(self.find_edit)

    def open_text(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text files (*.txt);;All files (*)', options=options)
        if file_name:
            with open(file_name, 'r') as f:
                text = f.read()
            self.text_edit.setText(text)

    def save_text(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text files (*.txt);;All files (*)', options=options)
        if file_name:
            # Save the text in the QTextEdit widget to the specified file
            text = self.text_edit.toPlainText()
            with open(file_name, 'w') as f:
                f.write(text)

    def find_text(self):
        # Get the search text and the QTextEdit widget
        text = self.find_edit.text()
        editor = self.text_edit

        # Use the QTextEdit find() method to search for the text
        if editor.find(text):
            return

        # If the text is not found, show a message box
        QMessageBox.warning(self, 'Text Editor', 'Text not found')


app = QApplication(sys.argv)
editor = TextEditor()
editor.show()
sys.exit(app.exec_())

