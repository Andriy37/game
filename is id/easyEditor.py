import os  # Імпорт модуля для роботи з операційною системою
from PyQt5.QtWidgets import (  # Імпорт класів із модуля PyQt6 для графічного інтерфейсу користувача
   QApplication, QWidget,
   QFileDialog,
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PIL import Image, ImageFilter  # Імпорт класів з бібліотеки PIL для роботи з зображеннями
from PyQt5.QtCore import Qt  # Імпорт констант з модуля PyQt6 для роботи з основними функціями
from PyQt5.QtGui import QPixmap  # Імпорт класу для роботи з зображеннями у PyQt6

app = QApplication([])  # Створення об'єкту додатку QApplication
window = QWidget()  # Створення головного вікна програми
window.setWindowTitle('Easy Editor')  # Встановлення заголовку вікна
window.resize(700, 500)  # Встановлення розміру вікна

btn_folder = QPushButton('Папка')  # Створення кнопки для вибору теки
list_file = QListWidget()  # Створення віджету списку файлів

photo = QLabel('Тут буде відображатися фото')  # Створення мітки для відображення зображення

btn_left = QPushButton('Вліво')  # Створення кнопки для повороту зображення вліво
btn_right = QPushButton('Вправо')  # Створення кнопки для повороту зображення вправо
btn_flip = QPushButton("Дзеркало")  # Створення кнопки для відображення зображення в дзеркальному відображенні
btn_sharp = QPushButton("Різкість")  # Створення кнопки для застосування фільтра різкості до зображення
btn_bw = QPushButton('Ч/Б')  # Створення кнопки для перетворення зображення у відтінки сірого

line = QHBoxLayout()  # Створення горизонтального розташування для кнопок і списку
col1 = QVBoxLayout()  # Створення вертикального розташування для кнопок
col2 = QVBoxLayout()  # Створення вертикального розташування для мітки та кнопок

col1.addWidget(btn_folder)  # Додавання кнопки "Папка" до першого стовпця
col1.addWidget(list_file)  # Додавання списку файлів до першого стовпця

col2.addWidget(photo, 95)  # Додавання мітки для відображення зображення до другого стовпця
row = QHBoxLayout()  # Створення горизонтального розташування для кнопок зміни зображення
row.addWidget(btn_left)  # Додавання кнопки "Вліво" до рядка
row.addWidget(btn_right)  # Додавання кнопки "Вправо" до рядка
row.addWidget(btn_flip)  # Додавання кнопки "Дзеркало" до рядка
row.addWidget(btn_sharp)  # Додавання кнопки "Різкість" до рядка
row.addWidget(btn_bw)  # Додавання кнопки "Ч/Б" до рядка
col2.addLayout(row)  # Додавання рядка з кнопками до другого стовпця

line.addLayout(col1, 20)  # Додавання першого стовпця до горизонтального розташування з відсотковою шириною 20%
line.addLayout(col2, 80)  # Додавання другого стовпця до горизонтального розташування з відсотковою шириною 80%
window.setLayout(line)  # Встановлення розташування віджетів у вікні

workdir = ''  # Ініціалізація змінної для збереження поточної теки

def chooseWorkdir():  # Функція для вибору теки
   global workdir  # Використання глобальної змінної для збереження теки
   workdir = QFileDialog.getExistingDirectory()  # Відкриття вікна вибору теки

def filter(files, extensions):  # Функція для фільтрації файлів за розширеннями
   result = []  # Ініціалізація списку результатів
   for filename in files:  # Для кожного файлу у списку файлів
      for ext in extensions:  # Для кожного розширення у списку розширень
         if filename.endswith(ext):  # Якщо ім'я файлу закінчується на поточне розширення
            result.append(filename)  # Додати ім'я файлу до списку результатів
   return result  # Повернути список відфільтрованих файлів

def showFilenameList():  # Функція для відображення списку файлів у віджеті
   extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.ico']  # Список допустимих розширень зображень
   chooseWorkdir()  # Виклик функції для вибору теки
   filenames = filter(os.listdir(workdir), extensions)  # Фільтрація файлів за розширеннями
   list_file.clear()  # Очищення списку файлів
   for filename in filenames:  # Для кожного файлу у списку відфільтрованих файлів
      list_file.addItem(filename)  # Додати ім'я файлу до списку файлів

btn_folder.clicked.connect(showFilenameList)  # Підключення функції до події натискання кнопки "Папка"

class ImageProcessor():  # Створення класу для обробки зображень
   def __init__(self):  # Конструктор класу
      self.image = None  # Ініціалізація змінної для збереження зображення
      self.dir = None  # Ініціалізація змінної для збереження теки
      self.filename = None  # Ініціалізація змінної для збереження імені файлу
      self.new_folder = 'Відредаговані фото'  # Ім'я папки для збереження відредагованих зображень
   
   def loadImage(self, dir, filename):  # Метод для завантаження зображення
      self.dir = dir  # Збереження теки
      self.filename = filename  # Збереження імені файлу
      image_path = os.path.join(dir, filename)  # Формування шляху до файлу
      self.image = Image.open(image_path)  # Відкриття зображення за вказаним шляхом

   def showImage(self, path):  # Метод для відображення зображення у віджеті
      photo.hide()  # Приховання мітки
      pixmapimage = QPixmap(path)  # Створення об'єкту QPixmap з зображенням за вказаним шляхом
      w = photo.width()  # Отримання ширини мітки
      h = photo.height()  # Отримання висоти мітки
      pixmapimage = pixmapimage.scaled(w, h, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)  # Масштабування зображення зі збереженням пропорцій
      photo.setPixmap(pixmapimage)  # Встановлення зображення у мітку
      photo.show()  # Відображення мітки

   def do_bw(self):  # Метод для перетворення зображення у відтінки сірого
      self.image = self.image.convert('L')  # Перетворення зображення
      self.file_save()  # Збереження зображення
      image_path = os.path.join(self.dir, self.new_folder, self.filename)  # Формування шляху до зображення
      self.showImage(image_path)  # Відображення зображення у віджеті

   # Методи для обертання зображення на 90 градусів
   def do_left(self):
      self.image = self.image.transpose(Image.ROTATE_90)
      self.file_save()
      image_path = os.path.join(self.dir, self.new_folder, self.filename)
      self.showImage(image_path)
      
   def do_right(self):
      self.image = self.image.transpose(Image.ROTATE_270)
      self.file_save()
      image_path = os.path.join(self.dir, self.new_folder, self.filename)
      self.showImage(image_path)

   # Метод для відображення зображення у дзеркальному відображенні
   def do_flip(self):
      self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
      self.file_save()
      image_path = os.path.join(self.dir, self.new_folder, self.filename)
      self.showImage(image_path)
   
   # Метод для застосування фільтра різкості до зображення
   def do_sharp(self):
      self.image = self.image.filter(ImageFilter.SHARPEN)
      self.file_save()
      image_path = os.path.join(self.dir, self.new_folder, self.filename)
      self.showImage(image_path)

   def file_save(self):  # Метод для збереження зображення
      path = os.path.join(self.dir, self.new_folder)  # Формування шляху до папки для збереження
      if not os.path.isdir(path):  # Якщо папка не існує
         os.mkdir(path)  # Створити папку
      image_path = os.path.join(path, self.filename)  # Формування шляху до зображення
      self.image.save(image_path)  # Збереження зображення за вказаним шляхом

workimage = ImageProcessor()  # Створення об'єкту для обробки зображень
def showChosenImage():  # Функція для відображення вибраного зображення у віджеті
   if list_file.currentRow() >= 0:  # Якщо вибрано певний елемент списку
      filename = list_file.currentItem().text()  # Отримання імені вибраного файлу
      workimage.loadImage(workdir, filename)  # Завантаження зображення за вказаним шляхом
      image_path = os.path.join(workimage.dir, workimage.filename)  # Формування шляху до зображення
      workimage.showImage(image_path)  # Відображення зображення у віджеті
list_file.currentRowChanged.connect(showChosenImage)  # Підключення функції до події зміни поточного елементу списку
btn_bw.clicked.connect(workimage.do_bw)  # Підключення методу для перетворення у відтінки сірого до події натискання кнопки "Ч/Б"
btn_left.clicked.connect(workimage.do_left)  # Підключення методу для обертання зображення на 90 градусів вліво
btn_right.clicked.connect(workimage.do_right)  # Підключення методу для обертання зображення на 90 градусів вправо
btn_flip.clicked.connect(workimage.do_flip)  # Підключення методу для відображення зображення у дзеркальному відображенні
btn_sharp.clicked.connect(workimage.do_sharp)  # Підключення методу для застосування фільтра різкості до зображення

window.show()  # Відображення головного вікна програми
app.exec()  # Запуск головного циклу подій
