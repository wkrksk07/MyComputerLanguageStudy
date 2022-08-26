import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)
def turn_up():
    t.setheading(90)
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear() # clear() : 화면을 지우는 함수

#키보드
t.shape("turtle") # 거북이 모양을 사용
t.speed(0) # 거북이 속도를 가장 빠르게 지정
t.onkeypress(turn_right, "Right") # →키 를 누르면 turn_right 함수 호출
t.onkeypress(turn_up, "Up") # ↑
t.onkeypress(turn_left, "Left") # ←
t.onkeypress(turn_down, "Down") # ↓
t.onkeypress(blank, "Escape") # ESC 키 를 누르면 blank 함수 호출
t.listen()

#마우스
t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)


t.mainloop()
