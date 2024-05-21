import turtle
import time

# Configuração da tela
screen = turtle.Screen()
screen.title("Pomodoro Timer")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Configuração do timer
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.color("white")
timer.goto(0, 0)

# Função para desenhar o círculo
def draw_circle():
    circle = turtle.Turtle()
    circle.hideturtle()
    circle.penup()
    circle.goto(0, -150)
    circle.pendown()
    circle.pensize(5)
    circle.circle(150)
    circle.hideturtle()

# Função para mostrar o tempo restante
def display_time(minutes, seconds):
    timer.clear()
    timer.write(f"{minutes:02d}:{seconds:02d}", align="center", font=("Arial", 48, "normal"))

# Função principal do timer
def start_timer(work_minutes, short_break_minutes, long_break_minutes, cycles):
    for cycle in range(cycles):
        # Período de trabalho
        countdown(work_minutes, "Work")
        if cycle < cycles - 1:
            # Pausa curta
            countdown(short_break_minutes, "Short Break")
        else:
            # Pausa longa
            countdown(long_break_minutes, "Long Break")
    timer.write("Pomodoro Complete!", align="center", font=("Arial", 36, "bold"))

# Função de contagem regressiva
def countdown(minutes, mode):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        display_time(mins, secs)
        time.sleep(1)
        seconds -= 1
    if mode == "Work":
        screen.bgcolor("lightgreen")
    elif mode == "Short Break":
        screen.bgcolor("lightblue")
    else:
        screen.bgcolor("lightcoral")

# Desenhar o círculo
draw_circle()

# Iniciar o timer (25 minutos de trabalho, 5 minutos de pausa curta, 15 minutos de pausa longa, 4 ciclos)
start_timer(work_minutes=25, short_break_minutes=5, long_break_minutes=15, cycles=4)

# Manter a janela aberta
screen.mainloop()
