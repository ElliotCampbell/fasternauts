from graphics import *
from Tkinter import *

def main():

    root = Tk()
    frame = Frame(root, width=900, height=700)

    def movement(event):
    	dir = event.char

    	if dir is "a":
    		canvas.move(rect, -10, 0)
    	elif dir is "d":
    		canvas.move(rect, 10, 0)
    	elif dir is "s":
    		canvas.move(rect, 0, 10)
    	elif dir is "w":
    		canvas.move(rect, 0, -10)

    	
    canvas = Canvas(frame, width=900, height=700)
    rect = canvas.create_rectangle(50, 25, 150, 75, fill="blue")
    canvas.bind("<Button-1>", lambda event: canvas.focus_set())
    canvas.bind("<Key>", movement)
    frame.pack()
    canvas.pack()
    

    root.mainloop()

main()

