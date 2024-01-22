from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QButtonGroup, QLineEdit, QGroupBox, QLabel, QApplication, QWidget, QListWidget , QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox)
from PIL import ImageFilter , Image

app = QApplication([])
win = QWidget()
win.resize(700, 400)
win.setWindowTitle("photoshop")

btn_dir = QPushButton("Папка")
btn_vlivo = QPushButton("Вліво")
btn_vpravo = QPushButton("Вправо")
btn_dzerkalo = QPushButton("Дзеркало")
btn_rizkist = QPushButton("Різкість")
btn_niga = QPushButton("Ч/Б")
btn_panel = QListWidget()

line4 = QHBoxLayout()


line2 = QHBoxLayout()


line1 = QVBoxLayout()
line1.addWidget(btn_dir)
line1.addWidget(btn_panel)


line3 = QVBoxLayout()



line4.addLayout(line1,20)
line4.addLayout(line3,80)
line3.addLayout(line2)


win.show
app.exec_()