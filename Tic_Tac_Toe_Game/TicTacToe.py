from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Tic Tac Toe')

player_1 = True
count = 0

buttons = []
x_spaces = []
o_spaces = []
winning_combos = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8'], ['0', '3', '6'], ['1', '4', '7'], ['2', '5', '8'],
                  ['0', '4', '8'], ['2', '4', '6']]
win = []


def btn_press(btn, num):
    """This will be the function that executes after every button press"""
    global player_1, count, buttons, x_spaces, o_spaces

    # We will start with player 1's turn, add the appropriate mark, count the number of turns, keep track of what spaces
    #  each player has marked, and then alternate turns
    if player_1 == True:
        btn.config(text='X', state=DISABLED)
        player_1 = False
        count += 1
        buttons.append(btn)
        x_spaces.append(num)
    else:
        btn.config(text='O', state=DISABLED)
        player_1 = True
        count += 1
        buttons.append(btn)
        o_spaces.append(num)

    # After each turn we will check for a winner
    check_for_winner()

    # If a winner hasn't been found and all possible moves have been made a tie is declared
    if count == 9:
        messagebox.showinfo('Tie!', 'Cat\'s Game')
        clear_board()


def check_for_winner():
    """This will check all selected tiles and see if either player has made a winning combination"""
    global player_1, count, buttons, x_spaces, o_spaces, winning_combos, win

    # This loop checks each players marked spaces and sees if any winning combinations have been made
    if player_1 == False:
        for w in winning_combos:
            for n in w:
                if n in x_spaces:
                    win.append(n)
                else:
                    pass
            if win == w:
                messagebox.showinfo('Congratulations!', 'Player 1 Wins!')
                clear_board()
            else:
                win = []
                pass
    else:
        for w in winning_combos:
            for n in w:
                if n in o_spaces:
                    win.append(n)
                else:
                    pass
            if win == w:
                messagebox.showinfo('Congratulations', 'Player 2 Wins!')
                clear_board()
            else:
                win = []
                pass


def clear_board():
    """This clears teh board and resets all global objects"""
    global player_1, count, buttons, x_spaces, o_spaces, win

    for b in buttons:
        b.config(state=NORMAL, text='')
    player_1 = True
    count = 0
    x_spaces = []
    o_spaces = []
    win = []
    buttons = []


# Set up the menu bar with reset and exit functionality
menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Reset', command=clear_board)
file_menu.add_command(label='Exit', command=window.quit)

# create buttons and then place them evenly on the board
btn_0 = Button(window, width=12, height=5, command=lambda: btn_press(btn_0, '0'))
btn_1 = Button(window, width=12, height=5, command=lambda: btn_press(btn_1, '1'))
btn_2 = Button(window, width=12, height=5, command=lambda: btn_press(btn_2, '2'))
btn_3 = Button(window, width=12, height=5, command=lambda: btn_press(btn_3, '3'))
btn_4 = Button(window, width=12, height=5, command=lambda: btn_press(btn_4, '4'))
btn_5 = Button(window, width=12, height=5, command=lambda: btn_press(btn_5, '5'))
btn_6 = Button(window, width=12, height=5, command=lambda: btn_press(btn_6, '6'))
btn_7 = Button(window, width=12, height=5, command=lambda: btn_press(btn_7, '7'))
btn_8 = Button(window, width=12, height=5, command=lambda: btn_press(btn_8, '8'))

btn_0.grid(row=0, column=0)
btn_1.grid(row=0, column=1)
btn_2.grid(row=0, column=2)
btn_3.grid(row=1, column=0)
btn_4.grid(row=1, column=1)
btn_5.grid(row=1, column=2)
btn_6.grid(row=2, column=0)
btn_7.grid(row=2, column=1)
btn_8.grid(row=2, column=2)

window.mainloop()
