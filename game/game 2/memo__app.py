from PyQt5.QtWidgets import QApplication
from time import sleep
from random import choice, shuffle
app = QApplication([])
from memo__main import *
from memo__card_layout import*

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.all_answer = 0
        self.right_answer = 0
        self.isAsking = True
    def got_right(self):
        self.right_answer += 1
        self.all_answer += 1
    def got_wrong(self):
        self.all_answer += 1

q1 = Question("Яблуко", 'apple', 'aplle', 'aple', 'epple')
q2 = Question("Цукерок", 'candy', 'cendi', 'cendy', 'candi')
q3 = Question("Гарбуз", 'pumpkin', 'pupkin', 'punpkin', 'pupka')

questions = [q1, q2, q3] 
radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def new_question():
    global osnova_q
    osnova_q = choice(questions)
    text_q.setText(osnova_q.question)
    true_answer.setText(osnova_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(osnova_q.wrong_answer1)
    radio_buttons[1].setText(osnova_q.wrong_answer2)
    radio_buttons[2].setText(osnova_q.wrong_answer3)
    radio_buttons[3].setText(osnova_q.answer)
new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == true_answer.text():
                osnova_q.got_right()
                true_false.setText('Вірно')
                answer.setChecked(False)
                break
    else:
        true_false.setText('Не вірно')
        osnova_q.got_wrong()
    

def oki():
    if btn_next.text() == "Відповісти":
        check()
        ramochka1.hide()
        ramochka2.show()
        btn_next.setText('Наступне питання')
    else:
        new_question()
        ramochka2.hide()
        ramochka1.show()
        btn_next.setText("Відповісти")

btn_next.clicked.connect(oki)

def rest():
    win_1.hide()
    t = sp_time.value()
    sleep(t)
    win_1.show()

btn_relax.clicked.connect(rest)

def menu_generation():
    if osnova_q.all_answer == 0:
        u = 0
    else:
        u = (osnova_q.right_answer / osnova_q.all_answer)*100
    text = f'Разів відповіли: {osnova_q.all_answer} \n'\
        f'Правильних відповідей: {osnova_q.right_answer} \n'\
        f'Успішність: {u}%'
    yspishnist.setText(text)
    win_1.hide()
    menu_win.show()

btn_menu.clicked.connect(menu_generation)
    
def nazad():
    menu_win.hide()
    win_1.show()

back.clicked.connect(nazad)

def clear():
    ln_q.clear()
    ln_answer.clear()
    ln_wrong_ans1.clear()
    ln_wrong_ans2.clear()
    ln_wrong_ans3.clear()
btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(ln_q.text(), ln_answer.text(), ln_wrong_ans1.text(), ln_wrong_ans2.text(), ln_wrong_ans3.text() )
    questions.append(new_q)
    clear()
add_q.clicked.connect(add_question)



win_1.show()
app.exec_()
