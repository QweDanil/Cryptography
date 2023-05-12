import tkinter as tk
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x400+100+100")


def score():
    lbl["text"] = "Score: " + str(int(en1.get()) + int(en2.get()))


en1 = tk.Entry(window)
en1.grid(column=0, row=0)
en2 = tk.Entry(window)
en2.grid(column=0, row=1)
but = tk.Button(window, text="PREEEEEEEEEEEEEES", command=score).grid(column=1, row=0)
lbl = tk.Label(window, text="Score: ", fg="Green")
lbl.grid(column=0, row=2)

window.mainloop()
import tkinter as tk
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x400+100+100")


def score():
    lbl["text"] = "Score: " + str(int(en1.get()) + int(en2.get()))


en1 = tk.Entry(window)
en1.grid(column=0, row=0)
en2 = tk.Entry(window)
en2.grid(column=0, row=1)
but = tk.Button(window, text="PREEEEEEEEEEEEEES", command=score).grid(column=1, row=0)
lbl = tk.Label(window, text="Score: ", fg="Green")
lbl.grid(column=0, row=2)

window.mainloop()
import tkinter as tk
window = tk.Tk()
window.resizable(False, False)
window.geometry("400x400+100+100")


def score():
    lbl["text"] = "Score: " + str(int(en1.get()) + int(en2.get()))


en1 = tk.Entry(window)
en1.grid(column=0, row=0)
en2 = tk.Entry(window)
en2.grid(column=0, row=1)
but = tk.Button(window, text="PREEEEEEEEEEEEEES", command=score).grid(column=1, row=0)
lbl = tk.Label(window, text="Score: ", fg="Green")
lbl.grid(column=0, row=2)

item.add_command(label="новый", command=pp)


item.add_command(label="новый", command=pp)


file = fd.askopenfilename(filetypes=[('Images', '*.png')])


file = fd.askopenfile(filetypes=(('text files', '*.txt'), ('All files', '*.*')))
with open(str(file.name), mode="r") as ofile:
    text = ofile.read()
    print(text)


window.mainloop()