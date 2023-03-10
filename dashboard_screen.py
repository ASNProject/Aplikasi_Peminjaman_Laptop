import os
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from tkinter import ttk
import sqlite3
from random import randint


def dashboardScreen():
    root = Tk()

    # ################### SETUP SCREEN ################ #
    root.title('Aplikasi Peminjaman Laptop')
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
    conn = sqlite3.connect('database/apl_database.db')
    cursor = conn.cursor()
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
    t4 = Label(root, text='SELAMAT DATANG,', font=("Arial", 25))
    t4.place(relx=0.05, y=140)
    p1 = Label(root, text="''Aplikasi ini adalah layanan peminjaman laptop untuk "
                          "seluruh Civitas Akademika\ndi Akademi Angkatan Udara Yogyakarta. Pastikan ID peminjam "
                          "merupakan\npengguna aktif dan ID Laptop yang akan dipinjam sesuai dan sudah terverifikasi''",
               font=("Arial italic", 16), anchor="e", justify=LEFT)
    p1.place(relx=0.05, y=175)
    p2 = Label(root, text="PETUNJUK PENGGUNAAN\n1. Koneksikan perangakat dengan aplikasi\n2. Pilih layanan yang akan "
                          "digunakan\n3. Scan ID Pengguna(utama) dan ID Laptop", font=("Arial", 16), anchor="e",
               justify=LEFT)
    p2.place(relx=0.05, y=250)

    image2 = Image.open("assets/group.png")
    img_resize2 = image2.resize((550, 150))
    img2 = ImageTk.PhotoImage(img_resize2)
    # reading the image
    panel2 = tkinter.Label(root, image=img2)
    # set location image
    panel2.place(relx=0.04, y=340, anchor=NW)

    def runLoanScreen():
        os.system('python loan_screen.py')
    b1 = customtkinter.CTkButton(master=root, corner_radius=10, text="MEMINJAM", height=40, width=550,
                                 command=runLoanScreen)
    b1.place(relx=0.05, rely=0.7)

    def runReturnLoanScreen():
        os.system('python return_loan_screen.py')
    b2 = customtkinter.CTkButton(master=root, corner_radius=10, text="PENGEMBALIAN", height=40, width=550,
                                 command=runReturnLoanScreen)
    b2.place(relx=0.05, rely=0.78)

    t5 = Label(root, text='DAFTAR PEMINJAM', font=("Arial", 16))
    t5.place(relx=0.52, rely=0.02)

    # Table
    tbl = ttk.Treeview(root)
    tbl['columns'] = ('ID', 'Nama', 'LaptopID', 'Brand',  'Tanggal Pinjam', 'Tanggal Kembali')
    tbl.column('#0', width=0, stretch=NO)
    tbl.column('ID', anchor=CENTER, width=80)
    tbl.column('Nama', anchor=CENTER, width=100)
    tbl.column('LaptopID', anchor=CENTER, width=100)
    tbl.column('Brand', anchor=CENTER, width=100)
    tbl.column('Tanggal Pinjam', anchor=CENTER, width=100)
    tbl.column('Tanggal Kembali', anchor=CENTER, width=100)

    tbl.heading('#0', text='', anchor=CENTER)
    tbl.heading('ID', text='Id', anchor=CENTER)
    tbl.heading('Nama', text='Nama', anchor=CENTER)
    tbl.heading('LaptopID', text='LaptopID', anchor=CENTER)
    tbl.heading('Brand', text='Brand', anchor=CENTER)
    tbl.heading('Tanggal Pinjam', text='Tanggal Pinjam', anchor=CENTER)
    tbl.heading('Tanggal Kembali', text='Tanggal kembali', anchor=CENTER)

    cursor.execute("SELECT * FROM peminjaman_data")
    all_rows = cursor.fetchall()
    for i in all_rows:
        tbl.insert(parent='', index=0, values=(i[0], i[1], i[3], i[4], i[6], i[7]))
    conn.commit()
    tbl.place(relx=0.52, rely=0.06)

    # ##### FOOTER ##### #
    t6 = Label(root, text='Pusat Informasi', font=("Arial", 14))
    t6.place(relx=0.22, rely=0.9)

    # Icons Social Media
    image3 = Image.open("assets/mail.png")
    img_resize3 = image3.resize((30, 30))
    img3 = ImageTk.PhotoImage(img_resize3)
    panel3 = tkinter.Label(root, image=img3)
    panel3.place(relx=0.05, rely=0.94, anchor=NW)
    t7 = Label(root, text='example@gmail.com', font=("Arial", 12))
    t7.place(relx=0.08, rely=0.95)

    image4 = Image.open("assets/whatsapp.png")
    img_resize4 = image4.resize((30, 30))
    img4 = ImageTk.PhotoImage(img_resize4)
    panel4 = tkinter.Label(root, image=img4)
    panel4.place(relx=0.193, rely=0.94, anchor=NW)
    t8 = Label(root, text='081234567890', font=("Arial", 12))
    t8.place(relx=0.222, rely=0.95)

    image5 = Image.open("assets/instagram.png")
    img_resize5 = image5.resize((30, 30))
    img5 = ImageTk.PhotoImage(img_resize5)
    panel5 = tkinter.Label(root, image=img5)
    panel5.place(relx=0.31, rely=0.94, anchor=NW)
    t9 = Label(root, text='@AplikasiPeminjamLaptopAAU', font=("Arial", 12))
    t9.place(relx=0.34, rely=0.95)

    t10 = Label(root, text='Copyright: Aplikasi Peminjaman Laptop 2023', font=("Arial", 12))
    t10.place(relx=0.8, rely=0.96)

    def refresh():
        # do stuff
        root.after(1, refresh)  # 5 minutes in milliseconds

    refresh()

    root.mainloop()


if __name__ == '__main__':
    dashboardScreen()
