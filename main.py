from tkinter import *
from roman_numerals import *
import time

root = Tk()
time1 = ''
clock = Label(root, font=('times', 20, 'bold'), bg='navajo white')
clock.pack(fill=BOTH, expand=1)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        hour = int(time.strftime('%H'))
        minute = int(time.strftime('%M'))
        second = int(time.strftime('%S'))

        roman_time = convert_to_numeral(hour) + ' : ' + convert_to_numeral(minute) + ' : ' + convert_to_numeral(second)
        clock.config(text=roman_time)
        # calls itself every 200 ms
        # to update the time display as needed
        # could use > 200 ms, but display gets jerky
    clock.after(200, tick)

tick()
root.mainloop()
