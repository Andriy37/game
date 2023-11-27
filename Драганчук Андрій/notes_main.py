from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QGroupBox, QListWidget,QTextEdit ,QLabel, QApplication, QWidget,  QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox

app = QApplication([])

notes_window = QWidget()
notes_window.setWindowTitle('Розумні замітки')
notes_window.resize(900,600)

list_notes_lable = QLabel('Список Заміток')
list_notes_lable = QListWidget()
btn_note_create = QPushButton("Створити замітку")
btn_note_del = QPushButton("Видалит замітку")
btn_note_save = QPushButton("Зберегти замітку")

fiend_text = QTextEdit()
field_teg = QLineEdit("Введіть")

btn_teg_add = QPushButton("Додати замітки")
btn_teg_del = QPushButton("Відкріпити від замітки")
btn_teg_search = QPushButton("ШУкати замітки")

list_tags_lable = QLabel("Список тегів")
list_tags = QListWidget()
field_teg.setPlaceholderText("Ведіть тег...")