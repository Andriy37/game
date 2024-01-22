from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QButtonGroup, QLineEdit, QGroupBox, QLabel, QApplication, QWidget,
    QListWidget, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox
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
btn_panel = QListWidget()
photo = QLabel()

line4 = QHBoxLayout()
line2 = QHBoxLayout()
line1 = QVBoxLayout()
line3 = QVBoxLayout()

line1.addWidget(btn_dir)
line1.addWidget(btn_panel)
line3.addWidget(photo)
line2.addWidget(btn_vlivo)
line2.addWidget(btn_vpravo)
line2.addWidget(btn_dzerkalo)
line2.addWidget(btn_rizkist)
line2.addWidget(btn_vlivo)


line3.addLayout(line2)

line4.addLayout(line1, 80)
line4.addLayout(line3, 20)

win.setLayout(line4)  # Додано цей рядок для встановлення макету вікна

win.show()
app.exec_()
