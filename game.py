
#3/18/23
# create buttons with labels that can be changed when the user clicks on them


from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
import random

# Make tiles
tiles = Fifteen()

# Shuffle board
def shuffleButtons(count, number):
    for i in tiles.tiles:
            if i != 0:
                index = tiles.tiles.index(i) +1
                labels[index].set(str(i))
                gui.nametowidget(str(index)).configure(bg='coral')
            else:
                index = tiles.tiles.index(i)+1
                labels[index].set(' ')
                gui.nametowidget(str(index)).configure(bg='peach puff')
    if count < number:
        tiles.shuffle(1)
       
        gui.after(300, lambda: shuffleButtons(count+1, number))


def solve(self):
    self.tiles = list(range(1, 16)) + [0]
    self.empty_index = 15
    for i in range(16):
        if i != self.empty_index:
            self.tile_frames[i].winfo_children()[0].config(text=str(self.tiles[i]))
        else:
            self.empty_frame = self.tile_frames[i]



# Switches the tiles
def switchButtons(value, pos):
    if value.get() != ' ':
        if tiles.is_valid_move(int(value.get())):
            tiles.update(int(value.get()))

            for i in range(len(labels)):
                if labels[i].get() == ' ':
                    empty = i

            labels[empty].set(value.get())
            labels[int(pos)].set(' ')
            gui.nametowidget(pos).configure(bg='peach puff')
            gui.nametowidget(empty).configure(bg='coral')

            if tiles.is_solved():
                print('Winner')


# Creates the button of the puzzle
def addButton(gui, value, pos):
    return Button(gui, textvariable=value, name=str(pos), bg='coral', fg='black', font=font, height=2, width=5, command=lambda: switchButtons(value, pos))



if __name__ == '__main__':
    # Make tiles
    tiles = Fifteen()
    empty = 16

    # Make a window
    gui = Tk()
    gui.title("Fifteen")

    # Make font
    font = font.Font(family='Helvetica', size='25', weight='bold')

    # Make buttons with labels
    labels = [StringVar() for i in range(16)]

    buttonArray = []
    # Make buttons
    for i in range(1, 16):
        labels[i].set(str(i))
        buttonArray.append(addButton(gui, labels[i], str(i)))

    blank = StringVar()
    blank.set(' ')
    labels.append(blank)
    buttonArray.append(Button(gui, textvariable=blank, name=str(16),
                               bg='peach puff', fg='black', font=font, height=2, width=5,
                               command=lambda: switchButtons(blank, '16')))

    shuffle = StringVar()
    shuffle.set('Shuffle')
    nameShuffle = 'shuffle'
    buttonShuffle = Button(gui, textvariable=shuffle, name=str(nameShuffle),
                         bg='medium aquamarine', fg='black', font=font, height=2, width=10,
                         command=lambda: shuffle(0, 30))


    solve = StringVar()
    solve.set('Solve')
    nameSolve = 'solve'
    buttonSolve = Button(gui, textvariable=solve, name=str(nameSolve),
                            bg='medium aquamarine', fg='black', font=font, height=2, width=10,
                            command=lambda: solve())

    # Pack the buttons
    for i in range(16):
        buttonArray[i].grid(row=(i // 4), column=(i % 4))

    buttonShuffle.grid(row=4, column=0, columnspan=2)
    buttonSolve.grid(row=4, column=2, columnspan=2)

    # Start main loop
    tiles.shuffle
    gui.mainloop()
