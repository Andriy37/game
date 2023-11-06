 random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication

app=QApplication([])

from main_window import *
from menu_window import *

class Question:
    def init(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question=question
        self.answer=answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
        self.isAsking=True
        self.count_ask=0
        self.count_right=0
    def got_right(self):
        self.count_ask+=1
        self.count_right+=1
    def got_wrong(self):
        self.count_ask+=1
q1=Question("Яблуко","apple","eppla","cucumber","apply")
q2=Question("Машина","car","cer","bike","ship")
q3=Question("Дім","Doma","home","city","meet")
q4=Question("Риба","fish","grow","shape","shop")


radio_buttons=[rbtn_ans1,rbtn_ans2,rbtn_ans3,rbtn_ans4]
question=[q1,q2,q3,q4]

def new_question():
    global cur_q
    cur_q=choice(question)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text()==lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText("Вірно!")
                answer.setChecked(False)
                break
    else:
        lb_result.setText("Не вірно!")
        cur_q.got_wrong()

def click_ok():
    if btn_next.text()=='Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText("Наступне запитання")
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText("Відповісти")

        
btn_next.clicked.connect(click_ok)

def rest():
    win_card.hide()
    n=btn_rest.value()*60
    sleep(n)
    win_card.show()


btn_rest.clicked.connect(rest)



def menu_generation():
    if cur_q.count_ask==0:
        c=0
    else:
        c=(cur_q.count_right/cur_q.count_ask)*100

    text=f'Разів відповіли:{cur_q.count_ask}\n' \
         f'Вірних відповідей:{cur_q.count_right}\n' \
         f'Успішність:{round(c,2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)

def back_menu():
    menu_win.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q=Question(le_question.text(),le_right_ans.text(),
                   le_wrong_ans1.text(),le_wrong_ans2.text(),
                   le_wrong_ans3.text())
    question.append(new_q)
    clear()

btn_addquestion.clicked.connect(add_question)


window.show()
app.exec()
