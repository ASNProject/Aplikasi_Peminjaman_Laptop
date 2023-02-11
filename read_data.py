import datetime
import os
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3
import datetime as dt
import serial
import time
import threading
import continuous_threading

root = Tk()

root.title('Aplikasi Peminjaman Laptop - Halaman Pinjaman')
root_width = 320
root_height = 320
# get screen dimension
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
# find the center point
center_x = int(root_screen_width / 2 - root_width / 2)
center_y = int(root_screen_height / 2 - root_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
root.resizable(False, False)

t1 = Label(root, text='HASIL SCAN:', font=("Arial bold", 12))
t1.place(relx=0.08, rely=0.1)

ser = serial.Serial()
ser.baudrate = 9600
try:
    ser.port = '/dev/tty.usbmodem1101'
except:
    ser.port = '/dev/tty.usbmodem1101'

ser.open()
data = ser.readline()
if data:
    data = data.decode()
    data = data.strip()
    data = int(data)

t1 = Label(root, text=data, font=("Arial bold", 12))
t1.place(relx=0.08, rely=0.1)

root.mainloop()
