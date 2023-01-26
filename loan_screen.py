import tkinter
from tkinter import *
from PIL import ImageTk, Image
import customtkinter
import sqlite3

root = Tk()
database = "database/apl_database.db"
connection = sqlite3.connect(database)

# ################### SETUP SCREEN ################ #
root.title('Aplikasi Peminjaman Laptop - Halaman Pinjaman')
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
b1 = customtkinter.CTkButton(master=root, corner_radius=10, text="SCAN ID CARD", height=40, width=200,
                             command=lambda: scanidcard(234)
                             )
b1.place(relx=0.08, rely=0.2)

t4 = Label(root, text='HASIL SCAN:', font=("Arial bold", 12))
t4.place(relx=0.08, rely=0.29)

t5 = Label(root, text='ID', font=("Arial", 12))
t5.place(relx=0.08, rely=0.32)
t6 = Label(root, text=':', font=("Arial", 12))
t6.place(relx=0.13, rely=0.32)
ids = tkinter.StringVar()
t7 = Label(root, textvariable=ids, font=("Arial", 12))
t7.place(relx=0.14, rely=0.32)

t8 = Label(root, text='NAMA', font=("Arial", 12))
t8.place(relx=0.08, rely=0.35)
t9 = Label(root, text=':', font=("Arial", 12))
t9.place(relx=0.13, rely=0.35)
nama = tkinter.StringVar()
t10 = Label(root, textvariable=nama, font=("Arial", 12))
t10.place(relx=0.14, rely=0.35)

t11 = Label(root, text='MEMBER', font=("Arial", 12))
t11.place(relx=0.08, rely=0.38)
t12 = Label(root, text=':', font=("Arial", 12))
t12.place(relx=0.13, rely=0.38)
member = tkinter.StringVar()
t13 = Label(root, textvariable=member, font=("Arial", 12))
t13.place(relx=0.14, rely=0.38)

b2 = customtkinter.CTkButton(master=root, corner_radius=10, text="SCAN ID LAPTOP", height=40, width=200,
                             command=lambda: scanidlaptop(123))
b2.place(relx=0.75, rely=0.2)

t14 = Label(root, text='HASIL SCAN:', font=("Arial bold", 12))
t14.place(relx=0.75, rely=0.29)

t15 = Label(root, text='ID', font=("Arial", 12))
t15.place(relx=0.75, rely=0.32)
t16 = Label(root, text=':', font=("Arial", 12))
t16.place(relx=0.80, rely=0.32)
idlaptop = tkinter.StringVar()
t17 = Label(root, textvariable=idlaptop, font=("Arial", 12))
t17.place(relx=0.81, rely=0.32)

t18 = Label(root, text='BRAND', font=("Arial", 12))
t18.place(relx=0.75, rely=0.35)
t19 = Label(root, text=':', font=("Arial", 12))
t19.place(relx=0.80, rely=0.35)
brand = tkinter.StringVar()
t20 = Label(root, textvariable=brand, font=("Arial", 12))
t20.place(relx=0.81, rely=0.35)

t21 = Label(root, text='UNIT', font=("Arial", 12))
t21.place(relx=0.75, rely=0.38)
t22 = Label(root, text=':', font=("Arial", 12))
t22.place(relx=0.80, rely=0.38)
unit = tkinter.StringVar()
t23 = Label(root, textvariable=unit, font=("Arial", 12))
t23.place(relx=0.81, rely=0.38)

t24 = Label(root, text='NOTA PEMINJAMAN', font=("Arial bold", 14))
t24.place(relx=0.05, rely=0.46)

c = Canvas(root, bg="white",
           height=300, width=800)
c.place(relx=0.05, rely=0.5)

b3 = customtkinter.CTkButton(master=root, corner_radius=10, text="PINJAM", height=40, width=270)
b3.place(relx=0.73, rely=0.52)
b4 = customtkinter.CTkButton(master=root, corner_radius=10, text="PRINT", height=40, width=270)
b4.place(relx=0.73, rely=0.6)
b4 = customtkinter.CTkButton(master=root, corner_radius=10, text="KEMBALI", height=40, width=270,
                             command=root.destroy)
b4.place(relx=0.73, rely=0.85)

t25 = Label(root, text='Copyright: Aplikasi Peminjaman Laptop 2023', font=("Arial", 12))
t25.place(relx=0.8, rely=0.96)

# #### def #### #
idmember = tkinter.StringVar()
statuslaptop = tkinter.StringVar()


def scanidcard(rfid):
    try:
        val = int(rfid)
        try:
            data = (val,)
            q = "SELECT * FROM member_data WHERE rfid= ?"
            cursor = connection.execute(q, data)
            data_row = cursor.fetchmany(rfid)
            for row in data_row:
                ids.set(row[0])
                idmember.set(row[1])
                nama.set(row[2])
                member.set(row[3])
                statuslaptop.set(row[5])
        except sqlite3.Error as error:
            print("error:", error)
    except:
        print("ada error")


def scanidlaptop(rfid):
    check_member = t13.getvar(t13.cget("textvariable"))
    laptop = tkinter.StringVar()
    status = tkinter.StringVar()

    if check_member == "AKTIF":
        try:
            val = int(rfid)
            try:
                data = (val,)
                q = "SELECT * FROM laptop_data WHERE rfid= ?"
                cursor = connection.execute(q, data)
                data_row = cursor.fetchmany(rfid)
                for row in data_row:
                    idlaptop.set(row[0])
                    laptop.set(row[1])
                    brand.set(row[2])
                    unit.set(row[3])
                    status.set(row[4])

                    if laptop.get() == idmember.get():
                        if status.get() == statuslaptop.get():
                            print("Data Sesuai")
                        else:
                            laptop_is_loan()
                    else:
                        cant_loan()

            except sqlite3.Error as error:
                print("error:", error)
        except:
            print("ada error")
    else:
        not_member()


# #### POP UP #### #
def not_member():
    top = Toplevel(root)

    top_width = 320
    top_height = 120
    # get screen dimension
    top_screen_width = top.winfo_screenwidth()
    top_screen_height = top.winfo_screenheight()
    # find the center point
    top_center_x = int(top_screen_width / 2 - top_width / 2)
    top_center_y = int(top_screen_height / 2 - top_height / 2)
    # set the position of the window to the center of the screen
    top.geometry(f'{top_width}x{top_height}+{top_center_x}+{top_center_y}')
    top.resizable(False, False)
    top.title("Pemberitahuan!")
    t26 = Label(top, text='Maaf anda bukan member!\nSilahkan daftar/aktivasi terlebih dahulu!',
                font=("Arial bold", 14))
    t26.place(relx=.5, rely=.5, anchor=CENTER)


def laptop_is_loan():
    top = Toplevel(root)

    top_width = 320
    top_height = 120
    # get screen dimension
    top_screen_width = top.winfo_screenwidth()
    top_screen_height = top.winfo_screenheight()
    # find the center point
    top_center_x = int(top_screen_width / 2 - top_width / 2)
    top_center_y = int(top_screen_height / 2 - top_height / 2)
    # set the position of the window to the center of the screen
    top.geometry(f'{top_width}x{top_height}+{top_center_x}+{top_center_y}')
    top.resizable(False, False)
    top.title("Pemberitahuan!")
    t26 = Label(top, text='Maaf laptop sudah dipinjam!\nMungkin terjadi kesalahan peminjaman!',
                font=("Arial bold", 14))
    t26.place(relx=.5, rely=.5, anchor=CENTER)


def cant_loan():
    top = Toplevel(root)

    top_width = 320
    top_height = 120
    # get screen dimension
    top_screen_width = top.winfo_screenwidth()
    top_screen_height = top.winfo_screenheight()
    # find the center point
    top_center_x = int(top_screen_width / 2 - top_width / 2)
    top_center_y = int(top_screen_height / 2 - top_height / 2)
    # set the position of the window to the center of the screen
    top.geometry(f'{top_width}x{top_height}+{top_center_x}+{top_center_y}')
    top.resizable(False, False)
    top.title("Pemberitahuan!")
    t26 = Label(top, text='Maaf verifikasi tidak sesuai!\nSilahkan periksa id member dan id laptop!',
                font=("Arial bold", 14))
    t26.place(relx=.5, rely=.5, anchor=CENTER)


root.mainloop()
