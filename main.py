from tkinter import *
from roman_numerals import *
import time

def tick():
    time1 = app.time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        hour = int(time.strftime('%H'))
        minute = int(time.strftime('%M'))
        second = int(time.strftime('%S'))

        roman_time = convert_to_numeral(hour) + ' : ' + convert_to_numeral(minute) + ' : ' + convert_to_numeral(second)
        app.update_time(roman_time)
        # calls itself every 200 ms
        # to update the time display as needed
        # could use > 200 ms, but display gets jerky
    app.clock.after(200, tick)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Roman Clock')
        # self.pack(fill=BOTH, expand=1)

        self.time1 = ''
        self.clock = Label(root, font=('times', 20, 'bold'), bg='navajo white')
        self.clock.pack(fill=BOTH, expand=1)

        self.numberfy_button = Button(self.clock, text="?", highlightbackground="navajo white")
        self.numberfy_button.place(x=0, y=0)
        # self.numberfy_button.pack(fill=BOTH, expand=1)
        # self.numberfy_button.pack()

    def update_time(self, new_time):
        self.clock.config(text=new_time)

root = Tk()
root.geometry('400x100')

app = Window(root)
tick()
root.mainloop()
