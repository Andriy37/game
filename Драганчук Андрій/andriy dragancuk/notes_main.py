
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QGroupBox, QListWidget,QTextEdit ,QLabel, QApplication, QWidget, QInputDialog, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox
import json 

app = QApplication([])




notes = {
    "Ласкаво просимо":{
        "текст":"Це найкращий додаток заміток світі",
        "теги":["інструкція","замітки"]
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

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    fiend_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItem(notes[key]['теги'])

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_teg.text()
        if not tag in notes[key]['теги']:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_teg.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("замітка для додавання тега не обрана")

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItem(notes[key]['теги'])
        with open("notes_data.json", 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = fiend_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана!")


def add_note():
    note_name, ok = QInputDialog.getText(notes_window, "Додати замітку", "Назва замітки: ")
    if ok and note_name != "":
        notes[note_name] = {'текст' : "", 'теги' : [] }
        list_notes.addItem(note_name)


def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        fiend_text.clear()
        list_notes.addItems(notes)
        with open ('notes_data.json', "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")

list_notes.itemClicked.connect(show_note)

btn_note_create.clicked.connect(add_note) 

btn_note_del.clicked.connect(del_note)
 
btn_note_save.clicked.connect(save_note)
 
btn_teg_add.clicked.connect(add_tag)

btn_teg_del.clicked.connect(del_tag)

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)

notes_window.show()
app.exec_()