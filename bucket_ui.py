import bucket_main
from tkinter import *

win = Tk()

win.geometry("300x330")
win.maxsize(330, 350)
win.minsize(330, 350)
win.title("Bucket")

mainframe = Frame(win)
frame_a = Frame(mainframe)
frame_b = Frame(mainframe)

goal = Label(mainframe, text="Objectif : %s dans %s" % (bucket_main.goal_number, bucket_main.goal_bucket))
goal.grid(row=1, column=2)

ba = Entry(frame_a, width=1, state = "disabled", font = ("default",80))
ba.pack()

ba_button = Button(frame_a, text="A max:%s"%(bucket_main.max_a), command=bucket_main.b_to_a, width=15, height=5)
ba_button.pack(pady=30)

fill_a_button = Button(frame_a, text="remplir", command=bucket_main.fill_a, width=5, height=1)
fill_a_button.pack()

empty_a_button = Button(frame_a, text="vider", command=bucket_main.empty_a, width=5, height=1)
empty_a_button.pack(pady=5)

bb = Entry(frame_b, width=1, state = "disabled", font = ("default",80))
bb.pack()

bb_button = Button(frame_b, text="B max:%s"%(bucket_main.max_b), command=bucket_main.a_to_b, width=15, height=5)
bb_button.pack(pady=30)

fill_b_button = Button(frame_b, text="remplir", command=bucket_main.fill_b, width=5, height=1)
fill_b_button.pack()

empty_b_button = Button(frame_b, text="vider", command=bucket_main.empty_b, width=5, height=1)
empty_b_button.pack(pady=5)


frame_a.grid(row=2, column=1)
frame_b.grid(row=2, column=3)
mainframe.pack()
win.mainloop()
