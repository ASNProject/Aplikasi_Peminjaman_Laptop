import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter

root = Tk()

# ################### SETUP SCREEN ################ #
root.title('Aplikasi Peminjaman Laptop - Halaman Pengembalian')
root_width = 1280
root_height = 720
# get screen dimension
root_screen_width = root.winfo_screenwidth()
root_screen_height = root.winfo_screenheight()
# find the center point
center_x = int(root_screen_width / 2 - root_width / 2)
center_y = int(root_screen_height / 2 - root_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
root.resizable(False, False)

# ##################### UI DESIGN ##################### #
# ##### HEADER ##### #
# load image
image1 = Image.open("assets/logoaau.png")
img_resize1 = image1.resize((80, 80))
img1 = ImageTk.PhotoImage(img_resize1)
# reading the image
panel1 = tkinter.Label(root, image=img1)
# set location image
panel1.place(x=10, y=10, anchor=NW)

# Text Header
t1 = Label(root, text='APLIKASI PEMINJAMAN LAPTOP', font=("Arial", 25))
t1.place(relx=0.08, y=10)
t2 = Label(root, text='AKADEMI ANGKATAN UDARA', font=("Arial", 20))
t2.place(relx=0.08, y=40)
t3 = Label(root, text='Jl. Raya Solo - Yogyakarta, Mereden, Sendangtirto, Kec. Kalasan, Kabupaten Sleman, '
                      'Daerah Istimewa Yogyakarta 55281', font=("Arial", 7))
t3.place(relx=0.08, y=70)

# ##### BODY ##### #
b1 = customtkinter.CTkButton(master=root, corner_radius=10, text="SCAN ID CARD", height=40, width=200)
b1.place(relx=0.08, rely=0.2)

t4 = Label(root, text='HASIL SCAN:', font=("Arial bold", 12))
t4.place(relx=0.08, rely=0.29)

t5 = Label(root, text='ID', font=("Arial", 12))
t5.place(relx=0.08, rely=0.32)
t6 = Label(root, text=':', font=("Arial", 12))
t6.place(relx=0.13, rely=0.32)

t7 = Label(root, text='NAMA', font=("Arial", 12))
t7.place(relx=0.08, rely=0.35)
t8 = Label(root, text=':', font=("Arial", 12))
t8.place(relx=0.13, rely=0.35)

t9 = Label(root, text='MEMBER', font=("Arial", 12))
t9.place(relx=0.08, rely=0.38)
t10 = Label(root, text=':', font=("Arial", 12))
t10.place(relx=0.13, rely=0.38)

b2 = customtkinter.CTkButton(master=root, corner_radius=10, text="SCAN ID LAPTOP", height=40, width=200)
b2.place(relx=0.75, rely=0.2)

t4 = Label(root, text='HASIL SCAN:', font=("Arial bold", 12))
t4.place(relx=0.75, rely=0.29)

t5 = Label(root, text='ID', font=("Arial", 12))
t5.place(relx=0.75, rely=0.32)
t6 = Label(root, text=':', font=("Arial", 12))
t6.place(relx=0.80, rely=0.32)

t7 = Label(root, text='NAMA', font=("Arial", 12))
t7.place(relx=0.75, rely=0.35)
t8 = Label(root, text=':', font=("Arial", 12))
t8.place(relx=0.80, rely=0.35)

t9 = Label(root, text='UNIT', font=("Arial", 12))
t9.place(relx=0.75, rely=0.38)
t10 = Label(root, text=':', font=("Arial", 12))
t10.place(relx=0.80, rely=0.38)

t11 = Label(root, text='NOTA PENGEMBALIAN', font=("Arial bold", 14))
t11.place(relx=0.05, rely=0.46)

c = Canvas(root, bg="white",
           height=300, width=800)
c.place(relx=0.05, rely=0.5)

b3 = customtkinter.CTkButton(master=root, corner_radius=10, text="PENGEMBALIAN", height=40, width=270)
b3.place(relx=0.73, rely=0.52)
b4 = customtkinter.CTkButton(master=root, corner_radius=10, text="PRINT", height=40, width=270)
b4.place(relx=0.73, rely=0.6)
b4 = customtkinter.CTkButton(master=root, corner_radius=10, text="KEMBALI", height=40, width=270,
                             command=root.destroy)
b4.place(relx=0.73, rely=0.85)

t12 = Label(root, text='Copyright: Aplikasi Peminjaman Laptop 2023', font=("Arial", 12))
t12.place(relx=0.8, rely=0.96)

root.mainloop()
