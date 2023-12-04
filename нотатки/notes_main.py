
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QGroupBox, QListWidget,QTextEdit ,QLabel, QApplication, QWidget,  QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox

app = QApplication([])

notes={
    "Ласкаво просимо":{
        "текст":"Це найкращий додаток заміток у світі"
        "текст":["інструкція","замітки"]
    }
}
with open("notes_data.json","w") as file:
    json.dump(notes,file)
notes_window = QWidget()
notes_window.setWindowTitle('Розумні замітки')
notes_window.resize(900,600)

list_notes_lable = QLabel('Список Заміток')
list_notes = QListWidget()
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



col_1 = QVBoxLayout ()
col_1.addWidget(fiend_text)

col_2 = QVBoxLayout ()
col_2.addWidget(list_notes_lable)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout ()
row_1.addWidget(btn_note_create)
row_1.addWidget(btn_note_del)

row_2 = QHBoxLayout ()
row_2.addWidget(btn_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)
col_2.addWidget(list_tags_lable)
col_2.addWidget(list_tags)
col_2.addWidget(field_teg)



row_3 = QHBoxLayout ()
row_3.addWidget(btn_teg_add)
row_3.addWidget(btn_teg_del)

row_4 = QHBoxLayout ()
row_4.addWidget(btn_teg_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes = QHBoxLayout ()
layout_notes.addLayout(col_1)
layout_notes.addLayout(col_2)


notes_window.setLayout(layout_notes)



notes_window.show()
app.exec_()