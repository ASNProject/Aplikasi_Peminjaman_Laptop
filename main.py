import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

# ################### Setup Base Window ################ #
root.title('Aplikasi Peminjaman Laptop')
root_width = 1280
root_height = 720
# get screen dimension
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
# find the center point
center_x = int(root_screen_width/2 - root_width / 2)
center_y = int(root_screen_height/2 - root_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')

# ##################### UI Design ##################### #
# ##### Header ######
# load image
image = Image.open("assets/logoaau.png")
img_resize = image.resize((80, 80))
img = ImageTk.PhotoImage(img_resize)
# reading the image
panel = tkinter.Label(root, image=img)
# setting the application
panel.place(x=10, y=10, anchor=NW)

# Text Header
text1 = Label(root, text='APLIKASI PEMINJAMAN LAPTOP', font=("Arial", 25))
text1.place(relx=0.08, y=10)
text2 = Label(root, text='AKADEMI ANGKATAN UDARA', font=("Arial", 20))
text2.place(relx=0.08, y=40)
text3 = Label(root, text='Jl. Raya Solo - Yogyakarta, Mereden, Sendangtirto, Kec. Kalasan, Kabupaten Sleman, '
                         'Daerah Istimewa Yogyakarta 55281', font=("Arial", 7))
text3.place(relx=0.08, y=70)

root.mainloop()
