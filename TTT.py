import random
import time
import turtle

def start_tic_tac_toe():
    window = turtle.Screen()
    BOK = 600
    X = -300
    Y = 300

    window.setup(BOK, BOK)
    window.title('Tic-Tac-Toe')
    window.bgcolor('black')

    xo = turtle.Turtle()
    xo.color('white')
    xo.pensize(7)
    xo.speed(0)
    xo.hideturtle()

    tablica = [[None, None, None],
               [None, None, None],
               [None, None, None]]

    turn = random.choice(['x', 'o'])

    ODSTEP = int(BOK / 3)
    for a in [1, 2]:
        xo.penup()
        xo.goto(X + a * ODSTEP, Y)
        xo.pendown()
        xo.goto(X + a * ODSTEP, -Y)

        xo.penup()
        xo.goto(X, Y - a * ODSTEP)
        xo.pendown()
        xo.goto(-X, Y - a * ODSTEP)

    def check():
        if tablica[0][0] == tablica[1][1] == tablica[2][2] and tablica[0][0] is not None:
            return tablica[2][2]
        elif tablica[0][2] == tablica[1][1] == tablica[2][0] and tablica[0][2] is not None:
            return tablica[1][1]

        for w in range(3):
            if tablica[w][0] == tablica[w][1] == tablica[w][2] and tablica[w][0] is not None:
                return tablica[w][2]

        for i in range(3):
            if tablica[0][i] == tablica[1][i] == tablica[2][i] and tablica[0][i] is not None:
                return tablica[2][i]

        return None

    def computer_move():
        global turn
        available_moves = [(i, j) for i in range(3) for j in range(3) if tablica[i][j] is None]
        if available_moves:
            move = random.choice(available_moves)
            kolumna, wiersz = move

            kolumna_srodek = (kolumna * ODSTEP + ODSTEP / 2) - BOK / 2
            wiersz_srodek = (-wiersz * ODSTEP - ODSTEP / 2) + BOK / 2

            xo.penup()
            xo.goto(kolumna_srodek - 25, wiersz_srodek - 25)
            xo.write('O', font=('Arial', 50))

            tablica[wiersz][kolumna] = 'o'
            turn = 'x'

            if check() is not None:
                xo.penup()
                xo.goto(-150, 0)
                time.sleep(1)
                xo.clear()
                xo.write("Wins " + check(), font=("Arial", 50))

    def click(x, y):
        global turn

        kolumna = 0
        wiersz = 0

        if x < X + ODSTEP:
            kolumna = 0
        elif x > X + 2 * ODSTEP:
            kolumna = 2
        else:
            kolumna = 1

        if y < Y - 2 * ODSTEP:
            wiersz = 2
        elif y > Y - ODSTEP:
            wiersz = 0
        else:
            wiersz = 1

        if tablica[wiersz][kolumna] is not None:
            return

        kolumna_srodek = (kolumna * ODSTEP + ODSTEP / 2) - BOK / 2
        wiersz_srodek = (-wiersz * ODSTEP - ODSTEP / 2) + BOK / 2

        xo.penup()
        xo.goto(kolumna_srodek - 25, wiersz_srodek - 25)
        xo.write('x', font=('Arial', 50))

        tablica[wiersz][kolumna] = 'x'
        turn = 'o'

        if check() is not None:
            xo.penup()
            xo.goto(-150, 0)
            time.sleep(1)
            xo.clear()
            xo.write("Wins " + check(), font=("Arial", 50))
        else:
            computer_move()

    window.onclick(click)
    window.listen()
    window.mainloop()
