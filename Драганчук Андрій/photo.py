from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import (
    QButtonGroup, QLineEdit, QGroupBox, QLabel, QApplication, QWidget,
    QListWidget, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox, QFileDialog,
)
from PIL import ImageFilter, Image

app = QApplication([])
win = QWidget()
win.resize(900, 600)
win.setWindowTitle("photoshop")

btn_dir = QPushButton("Папка")
btn_vlivo = QPushButton("Вліво")
btn_vpravo = QPushButton("Вправо")
btn_dzerkalo = QPushButton("Дзеркало")
btn_rizkist = QPushButton("Різкість")
btn_niga = QPushButton("Ч/Б")
panel = QListWidget()
photo = QLabel()

line4 = QHBoxLayout()
line2 = QHBoxLayout()
line1 = QVBoxLayout()
line3 = QVBoxLayout()

line1.addWidget(btn_dir)
line1.addWidget(panel)
line3.addWidget(photo)
line2.addWidget(btn_vlivo)
line2.addWidget(btn_vpravo)
line2.addWidget(btn_dzerkalo)
line2.addWidget(btn_rizkist)
line2.addWidget(btn_niga)

line3.addLayout(line2)

line4.addLayout(line1, 20)
line4.addLayout(line3, 80)

win.setLayout(line4)  # Додано цей рядок для встановлення макету вікна

workdir = ""

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for file_name in files:
        for ext in extensions:
            if file_name.endswith(ext):
                result.append(file_name)
    return result

def showFilenameList():
    global workdir
    extensions = ['.jpg','.jpeg','.png','.gif']
    chooseWorkdir()
    file_names = filter(os.listdir(workdir), extensions)
    panel.clear()
    for file_name in file_names:
        panel.addItem(file_name)

btn_dir.clicked.connect(showFilenameList)

win.show()
app.exec_()