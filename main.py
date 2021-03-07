from tkinter import * 
from tkinter import messagebox
import tkinter.font as font 
import datetime
import time
import sqlite3
import random
from random import randint

root = Tk()
root.title("Main Window")
root.state('zoomed')
root['bg'] = 'white'
myFont = font.Font(family="Arial", size=17, weight='bold', slant="italic")
headFont = font.Font(family="Arial", size=25, weight='bold', underline=1)

add_cust = PhotoImage(file='add_customer_white.png')
booking = PhotoImage(file='book.png')
return2 = PhotoImage(file='return2.png')
login = PhotoImage(file='login3.png')
img1 = PhotoImage(file='circle2.png')
search = PhotoImage(file='search.png')
delete = PhotoImage(file='delete.png')
man = PhotoImage(file='man.png')
woman = PhotoImage(file='woman.png')
bike = PhotoImage(file='bike.png')
scooter = PhotoImage(file='scooter.png')
car = PhotoImage(file='car.png')
submit = PhotoImage(file='submit.png')
fwd = PhotoImage(file='fwd.png')
bck = PhotoImage(file='bck.png')
show_pwd = PhotoImage(file="show_pwd2.png")
hide_pwd = PhotoImage(file="hide_pwd2.png")
update_img = PhotoImage(file="update2.png")

#Connect to a database
con = sqlite3.connect('main.db')
cur = con.cursor()

# ****************************************** FRAMES *************************************************
# CUSTOMER FRAME
add_customer_frame = Frame(root, borderwidth=5)
add_customer_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=40)

# BOOKING FRAME
booking_frame = LabelFrame(root, text='Book Vehicle...', borderwidth=4)
booking_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=40)

# RETURN FRAME
return_frame = LabelFrame(root, text='Book Vehicle...', borderwidth=4)
return_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=40)

# AVAILABLE VEHICLES FRAME
available_frame = LabelFrame(root, text='vehicles available', borderwidth=4, padx=20, pady=20)
available_frame.grid(row=1, rowspan=3, column=2, columnspan=7, padx=20, pady=20)

option_frame = LabelFrame(root, text='Delete Transaction...', borderwidth=4, padx=20, pady=20, fg='blue')
option_frame.grid(row=1, column=0, columnspan=13, padx=20, pady=10)

search_frame = LabelFrame(root, text='Search...', borderwidth=4, padx=10, pady=10)
search_frame.grid(row=1, column=0, columnspan=13, padx=20, pady=10)


# ******************************************* FRAME END ***************************************************

# --------------------- ADD INFO ----------------------

def customer_db(f_name, l_name, age, ph_no, dl_no, gen, alt_ph, user, password):
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    dl_no_entry.delete(0, END)
    alt_phone_entry.delete(0, END)
    user_entry.delete(0, END)
    pass_entry.delete(0, END)

    if f_name=='' or l_name=='' or age=='' or ph_no=='' or dl_no=='' or gen=='' or user=='' or password=='':
        messagebox.showinfo('INFO', 'Enter all the information!')
    
    elif len(ph_no) < 10:
        messagebox.showinfo("INFO", "Phone must have 10 Digits.")
    elif len(ph_no) > 10:
        messagebox.showinfo("INFO", "Phone must not exceed 10 Digits.")

    else:
        values = [f_name, l_name, age, dl_no, gen]

        con = sqlite3.connect('main.db')
        cur = con.cursor()

        cur.execute("INSERT INTO customers(first_name, last_name, age, dl_no, gender) VALUES (?, ?, ?, ?, ?)", values)
        cur.execute("INSERT INTO customer_phone(phone_no, dl_no) VALUES (?, ?)", (ph_no, dl_no))
        cur.execute("INSERT INTO user (username, password, role, dl_no) VALUES (?, ?, ?, ?)", (user, password, 'user', dl_no))

        messagebox.showinfo("SUCCESS",'Information added successfully!')

        if alt_ph != '':
            cur.execute("INSERT INTO customer_phone(phone_no, dl_no) VALUES (?, ?)", (alt_ph, dl_no))

        con.commit()
        con.close()


def customer_info():
    global add_customer_frame, first_name_entry, last_name_entry, age_entry, phone_entry, dl_no_entry, alt_phone_entry, user_entry, pass_entry

    add_customer_btn['state'] = 'disabled'
    add_label['state'] = 'disabled'
    book_label['state'] = 'normal'
    book_vehicle_btn['state'] = 'normal'
    return_btn['state'] = 'normal'
    return_label['state'] = 'normal'

    booking_frame.grid_forget()
    return_frame.grid_forget()

    add_customer_frame = Frame(root, borderwidth=5, padx=20, pady=10, bg='#7efff5', relief=FLAT)
    add_customer_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=15, sticky=N)

    #first name widget
    first_name_label = Label(add_customer_frame,text="First Name", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=15, anchor=W)
    first_name_label.config(font=myFont)
    first_name_label.grid(row=0,column=0, padx=15, pady=10, sticky=W)

    first_name_entry = Entry(add_customer_frame,borderwidth=0, width=20, highlightthickness=2)
    first_name_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    first_name_entry.grid(row=0,column=1, padx=15,sticky=E)

    #last name widget
    last_name_label = Label(add_customer_frame,text="Last Name", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=15, anchor=W)
    last_name_label.config(font=myFont)
    last_name_label.grid(row=1,column=0, padx=15, pady=10, sticky=W)

    last_name_entry = Entry(add_customer_frame,borderwidth=0,width=20, highlightthickness=2)
    last_name_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    last_name_entry.grid(row=1,column=1, padx=15,sticky=E)

    #age widget
    age_label = Label(add_customer_frame,text="Age", bg='#7efff5', fg='#2c3e50',padx=5, pady=5, width=15, anchor=W)
    age_label.config(font=myFont)
    age_label.grid(row=2,column=0, padx=15, pady=10, sticky=W)

    age_entry = Entry(add_customer_frame,borderwidth=0,width=20, highlightthickness=2)
    age_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    age_entry.grid(row=2,column=1, padx=15,sticky=E)

    #phone number widget
    phone_no_label = Label(add_customer_frame,text="Phone No", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=15, anchor=W)
    phone_no_label.config(font=myFont)
    phone_no_label.grid(row=3,column=0, padx=15, pady=10, sticky=W)

    phone_entry = Entry(add_customer_frame,borderwidth=0,width=20, highlightthickness=2)
    phone_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    phone_entry.grid(row=3,column=1, padx=15,sticky=E)

    #DL number widget
    dl_no_label = Label(add_customer_frame,text="DL Number", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=15, anchor=W)
    dl_no_label.config(font=myFont)
    dl_no_label.grid(row=4,column=0, padx=15, pady=10, sticky=W)

    dl_no_entry = Entry(add_customer_frame,borderwidth=0,width=20, highlightthickness=2)
    dl_no_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    dl_no_entry.grid(row=4,column=1, padx=15,sticky=E)

    #gender number widget
    gender_label = Label(add_customer_frame,text="Gender", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=12, anchor=W)
    gender_label.config(font=myFont)
    gender_label.grid(row=5,column=0, padx=15, pady=(20, 15), sticky=W)

    frame_2 = LabelFrame(add_customer_frame)
    frame_2.grid(row=5, column=1, columnspan=3)

    r = StringVar()

    Radiobutton(add_customer_frame, image=man, variable=r, value="M", font=myFont, bg='#7efff5', fg='white', selectcolor='#808e9b').place(x=260, y=310)
    Radiobutton(add_customer_frame, image=woman, variable=r, value="F", font=myFont, bg='#7efff5', fg='white', selectcolor='#808e9b').place(x=380, y=310)

    #phone number widget
    alt_phone_no_label = Label(add_customer_frame,text="ALT Phone No", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, width=15, anchor=W)
    alt_phone_no_label.config(font=myFont)
    alt_phone_no_label.grid(row=6,column=0, padx=15, pady=20, sticky=W)

    alt_label = Label(add_customer_frame, text='(Optional)', bg='#7efff5', fg='red', padx=5)
    alt_label.config(font=('bold', 12))
    alt_label.place(x=40, y=440)

    alt_phone_entry = Entry(add_customer_frame,borderwidth=0,width=20, highlightthickness=2)
    alt_phone_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    alt_phone_entry.grid(row=6, column=1, padx=15, sticky=E)

    username_label = Label(add_customer_frame, text="Username", bg='#7efff5', fg='#2c3e50', font=myFont)
    username_label.place(x=40, y=485)

    user_entry = Entry(add_customer_frame,borderwidth=0,width=15, highlightthickness=2)
    user_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    user_entry.place(x=30, y=525)

    pass_label = Label(add_customer_frame, text="Password", bg='#7efff5', fg='#2c3e50', font=myFont)
    pass_label.place(x=350, y=485)

    pass_entry = Entry(add_customer_frame,borderwidth=0,width=15, highlightthickness=2)
    pass_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", show="*", font=myFont, relief=FLAT)
    pass_entry.place(x=330, y=525)
    
    def show_pass(a, test):
        global pass_entry
        if test == 0:
            pass_entry = Entry(add_customer_frame,borderwidth=0,width=15, highlightthickness=2)
            pass_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
            pass_entry.place(x=330, y=525)
            pass_entry.insert(END, a)
            button_submit = Button(add_customer_frame, image=hide_pwd, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda:show_pass(pass_entry.get(),1))
            button_submit.place(x=280, y=530)

            button_submit = Button(add_customer_frame, image=submit, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get(), alt_phone_entry.get(),
            user_entry.get(), pass_entry.get()))
            button_submit.grid(row=7, column=0, columnspan=3, padx=20, pady=(150, 30))

        elif test == 1:
            a = pass_entry.get()
            pass_entry = Entry(add_customer_frame,borderwidth=0,width=15, highlightthickness=2)
            pass_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", show="*", font=myFont, relief=FLAT)
            pass_entry.place(x=330, y=525)
            pass_entry.insert(END, a)
            button_submit = Button(add_customer_frame, image=show_pwd, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda:show_pass(pass_entry.get(),0))
            button_submit.place(x=280, y=525)

            button_submit = Button(add_customer_frame, image=submit, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get(), alt_phone_entry.get(),
            user_entry.get(), pass_entry.get()))
            button_submit.grid(row=7, column=0, columnspan=3, padx=20, pady=(150, 30))

    button_submit = Button(add_customer_frame, image=show_pwd, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda:show_pass(pass_entry.get(),0))
    button_submit.place(x=280, y=525)

    button_submit = Button(add_customer_frame, image=submit, bg='#7efff5', fg='white',borderwidth=0,relief=FLAT, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get(), alt_phone_entry.get(),
    user_entry.get(), pass_entry.get()))
    button_submit.grid(row=7, column=0, columnspan=3, padx=20, pady=(150, 30))

# ------------------- ADD INFO END ---------------------


# -------------------- BOOKING INFO ----------------------

def available_vehicles(vehicle):
    global available_frame

    available_frame.grid_forget()

    available_frame = Frame(root, borderwidth=4, padx=20, pady=20, bg='#7efff5', relief=FLAT)
    available_frame.grid(row=3, column=4, columnspan=7, padx=(60,80), pady=40, sticky=NE)

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM vehicles WHERE vehicle_type = ? AND available=1", (vehicle, ))
    a = cur.fetchall()

    headers = ['Index','Vehicle Model', 'Vehicle No.', 'Price/hr']
    val = [10, 20, 20, 10]

    for j in range(len(headers)):
        e = Entry(available_frame, width=val[j], borderwidth=2, bg="#7f8c8d", fg='white', highlightthickness=2)
        e.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        e.grid(row=1, column=j, padx=10, pady=5)
        e.insert(END, headers[j])
    
    for i in range(len(a)):
        for j in range(len(headers)):
            if j == 0:
                e = Entry(available_frame, width=val[j], borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, i+1)
            else:
                e = Entry(available_frame, width=val[j], borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, a[i][j-1])

    con.commit()
    con.close()


def book_db(hour, minute, vehicle_id, dl_number):
    dl_no.delete(0, END)
    vehicle_no_entry.delete(0, END)

    if dl_number == '' or vehicle_id == '' or (hour == 0 and minute == 0):
        messagebox.showinfo('INFO', 'Enter all the information.')

    else:
        #TO get the current date
        date = datetime.date.today()
        date = str(date)
        
        #To get current time
        t = time.localtime()   
        time1 = str(t[3])+':'+str(t[4])+':'+str(t[5])

        dateTime = date + ' ' + time1

        con = sqlite3.connect('main.db')
        cur = con.cursor()

        cur.execute("SELECT * FROM transactions")
        num = cur.fetchall()

        if len(num) == 0:
            tran_id = 1000
        else:
            tran_id = int(num[len(num)-1][7]) + 1
            
        tran_id = str(tran_id)

        cur.execute("UPDATE vehicles SET available=0 WHERE vehicle_no = ?", (vehicle_id, ))

        cur.execute("INSERT INTO transactions (date_time, hours, minutes, amount, vehicle_no, dl_no, vehicle_returned, transaction_id, return_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (dateTime, hour, minute, 0, vehicle_id, dl_number, 0, tran_id, 'Rented'))

        con.commit()

        hour_val.set(0)
        min_val.set(0)


def booking_info():
    global booking_frame, dl_no, vehicle_no_entry, hour_val, min_val

    add_customer_btn['state'] = 'normal'
    add_label['state'] = 'normal'
    book_vehicle_btn['state'] = 'disabled'
    book_label['state'] = 'disabled'
    return_btn['state'] = 'normal'
    return_label['state'] = 'normal'

    add_customer_frame.grid_forget()
    return_frame.grid_forget()

    booking_frame = Frame(root, borderwidth=0, padx=90, pady=20, bg='#7efff5', relief=FLAT)
    booking_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky=N)

    # vehicle widget
    vehicle_label = Label(booking_frame, text="Vehicle", padx=0, pady=5, bg='#7efff5', fg='#2c3e50', anchor=W)
    vehicle_label.config(font=myFont)
    vehicle_label.grid(row=0, column=0, padx=(0, 20), pady=30, sticky=W)

    v_type = StringVar()

    Radiobutton(booking_frame, image=bike, variable=v_type, value='bike', font=myFont, bg='#7efff5', fg='white', selectcolor='#808e9b').place(x=155, y=25)
    Radiobutton(booking_frame, image=scooter, variable=v_type, value='scooter', font=myFont, bg='#7efff5', fg='white', selectcolor='#808e9b').place(x=260, y=35)
    Radiobutton(booking_frame, image=car, variable=v_type, value='car', font=myFont, bg='#7efff5', fg='white', selectcolor='#808e9b').place(x=370, y=30)

    serach_btn = Button(booking_frame, image=search, borderwidth=0, bg='#7efff5', relief=FLAT, command=lambda: available_vehicles(v_type.get()))
    serach_btn.config(font=("Helvetica", 10))
    serach_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=(20, 40))

    # dl_no widget
    dl_no_label = Label(booking_frame,text="DL No.", bg='#7efff5', fg='#2c3e50', padx=0, pady=5, anchor=W)
    dl_no_label.config(font=myFont)
    dl_no_label.grid(row=2, column=0, padx=(0, 20), pady=25, sticky=W)

    dl_no = Entry(booking_frame,borderwidth=0, width=20, highlightthickness=2)
    dl_no.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    dl_no.grid(row=2, column=1, padx=15, pady=15, sticky=E)

    # duration widget
    duration_label = Label(booking_frame,text="Duration", bg='#7efff5', fg='#2c3e50', padx=0, pady=5, anchor=W)
    duration_label.config(font=myFont)
    duration_label.grid(row=3, column=0, padx=(0, 20), pady=15, sticky=W)

    # Hours Entry
    hour_list = [0, 1, 2, 3, 4]

    hour_val = IntVar()

    hour_menu = OptionMenu(booking_frame, hour_val, *hour_list)
    hour_menu.config(font=myFont, bg='#808e9b', fg='white', relief=FLAT)
    hour_menu.grid(row=3, column=1, padx=(25, 15), pady=15, sticky=W)
    hour_val.set(hour_list[0])

    hrs_label = Label(booking_frame,text="hrs", bg='#7efff5', fg='#2c3e50')
    hrs_label.config(font=myFont)
    hrs_label.place(x=240, y=353)

    # Minutes Entry
    min_val = IntVar()

    min_menu = OptionMenu(booking_frame, min_val, 0, 30)
    min_menu.config(font=myFont, bg='#808e9b', fg='white', relief=FLAT)
    min_menu.place(x=330, y=340)
    min_val.set(hour_list[0])

    min_label = Label(booking_frame, text="mins", bg='#7efff5', fg='#2c3e50')
    min_label.config(font=myFont)
    min_label.place(x=405, y=353) 
 

    #vehicle_no widget
    vehicle_no_label = Label(booking_frame,text="Vehicle No.", bg='#7efff5', fg='#2c3e50', padx=0, pady=5, anchor=W)
    vehicle_no_label.config(font=myFont)
    vehicle_no_label.grid(row=4, column=0, padx=(0, 20), pady=25, sticky=W)

    vehicle_no_entry = Entry(booking_frame,borderwidth=0, width=20, highlightthickness=2)
    vehicle_no_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    vehicle_no_entry.grid(row=4, column=1, padx=15, pady=15, sticky=E)

    add_customer = Button(booking_frame, image=submit, borderwidth=2, bg='#7efff5', fg='white', relief=FLAT, command=lambda: book_db(hour_val.get(), min_val.get(), vehicle_no_entry.get(), dl_no.get()))
    add_customer.grid(row=5, column=0, columnspan=3, padx=20, pady=40)

# --------------------- BOOKING INFO END ----------------------


# --------------------- RETURN INFO -------------------------

def return_db(vehicle_no_etr):
    vehicle_no_etr

    if vehicle_no_etr == '':
        messagebox.showinfo('INFO', 'Enter Vehicle Number!')

    else:
        con = sqlite3.connect('main.db')
        cur = con.cursor()

        #To get current time
        t = time.localtime()   
        time2 = str(t[3])+':'+str(t[4])+':'+str(t[5])
        
        cal2 = time2.split(':')

        cur.execute("SELECT date_time FROM transactions WHERE vehicle_no=? AND vehicle_returned=?", (vehicle_no_etr, 0))
        date_time = cur.fetchone()
        date_time1 = list(date_time)
        
        t = [subl.split() for subl in date_time1] 
        time1 = t[0][1]
        cal1 = time1.split(':')
        
        h_time = int(cal2[0]) - int(cal1[0])
        m_time = int(cal2[1]) - int(cal1[1])
        m_time = m_time / 60
        total_time = h_time + m_time 
        
        cur.execute(f"SELECT {total_time}*price_hrs FROM vehicles WHERE vehicle_no=?", (vehicle_no_etr, ))
        amount = cur.fetchone()

        total = int(amount[0])

        cur.execute("UPDATE vehicles SET available=1 WHERE vehicle_no = ?", (vehicle_no_etr, ))

        cur.execute("UPDATE transactions SET vehicle_returned=1, amount=?, return_time=? WHERE vehicle_no=?", (total, time2, vehicle_no_etr, ))

        amount_label = Label(return_frame, text='Total Rent:', font=('Bold', 20), padx=30, pady=30, bg='#7efff5', fg="#2ecc72")
        amount_label.grid(row=3, column=0, columnspan=3, padx=20, pady=10)

        amount_label = Label(return_frame, text="Rs."+str(total), font=('Bold', 40), bg='#7efff5', fg='white', padx=30, pady=30)
        amount_label.grid(row=4, column=0, columnspan=3, padx=20, pady=30)

        con.commit()
        con.close()


def return_vehicle():
    global return_frame 

    add_customer_btn['state'] = 'normal'
    add_label['state'] = 'normal'
    book_vehicle_btn['state'] = 'normal'
    book_label['state'] = 'normal'
    return_btn['state'] = 'disabled'
    return_label['state'] = 'disabled'

    add_customer_frame.grid_forget()
    booking_frame.grid_forget()

    return_frame = Frame(root, borderwidth=0, bg='#7efff5', relief=FLAT)
    return_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #vehicle_no widget
    vehicle_no_label = Label(return_frame,text="Vehicle No.", bg='#7efff5', fg='#2c3e50', padx=5, pady=5, anchor=W)
    vehicle_no_label.config(font=myFont)
    vehicle_no_label.grid(row=0, column=0, padx=30, pady=30, sticky=W)

    vehicle_no_etr = Entry(return_frame,borderwidth=0,width=20, highlightthickness=2)
    vehicle_no_etr.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    vehicle_no_etr.grid(row=0, column=1, padx=30, pady=30, sticky=E)

    confirm_return = Button(return_frame, image=submit, borderwidth=0, bg='#7efff5', relief=FLAT, command=lambda: return_db(vehicle_no_etr.get()))
    confirm_return.grid(row=1, column=0, columnspan=3, padx=30, pady=40)
    

# --------------------- RETURN INFO END -------------------------

# Function to display all the contents of the table
def table(headers, b, val, startNum, frame, x, y):
    for j in range(len(headers)):
        e = Entry(frame, width=val[j], borderwidth=2, bg="#7f8c8d", fg='white', highlightthickness=2)
        e.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        e.grid(row=1, column=j, padx=x, pady=y)
        e.insert(END, headers[j])
    
    for i in range(len(b)):
        for j in range(len(headers)):
            if j == 0:
                e = Entry(frame, width=val[j], borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=x, pady=y)
                e.insert(END, i+startNum)
            else:
                e = Entry(frame, width=val[j], borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=x, pady=y)
                e.insert(END, b[i][j-1])

# ---------------------- ADMIN WINDOW ------------------------

# delete all the transactions
def delete_all():
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    a = messagebox.askyesno('DELETE ALL', 'Are you sure you want to delete all transactions?')

    if a:
        cur.execute("DELETE FROM transactions")

    con.commit()
    con.close()

# change admin's username or password
def change():
    change_window = Toplevel(root)
    change_window.title("Change Username or Password")

    frame = LabelFrame(change_window, text="Frame...", borderwidth=4, padx=10,pady=10)
    frame.grid(row=0, column=1, columnspan=2, padx=75,pady=20)

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM user")
    user = cur.fetchall()

    user_label = Label(frame, text="Username", padx=20, pady=10, font=('bold', 15))
    user_label.grid(row=0, column=0)

    user_input = Entry(frame, borderwidth=2)
    user_input.config(font=('bold', 15))
    user_input.grid(row=0, column=1)

    old_pwd_label = Label(frame, text="Password", padx=20, pady=10, font=('bold', 15))
    old_pwd_label.grid(row=1, column=0, padx=20)

    old_pwd_input = Entry(frame, borderwidth=2)
    old_pwd_input.config(font=('bold', 15))
    old_pwd_input.grid(row=1, column=1, padx=20)

    label = Label(frame, text="What do you want to change?", font=("Bold", 15), padx=5, pady=5)
    label.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 40))

    def check(val):
            username = user_input.get()
            old_pwd = old_pwd_input.get()
            if val == 'username':
                new_user = new_user_input.get()
                if username == user[0][0] and old_pwd == user[0][1]:
                    cur.execute("UPDATE user SET username=? WHERE username=?",(new_user, username))
                    con.commit()
                    con.close()
                    change_window.destroy()
                else:
                    messagebox.showerror("INFO","Wrong username or password")
            elif val == 'password':
                new_pwd = new_pwd_input.get()
                if username == user[0][0] and old_pwd == user[0][1]:
                    cur.execute("UPDATE user SET password=? WHERE username=?",(new_pwd, username))
                    con.commit()
                    con.close()
                    change_window.destroy()
                else:
                    messagebox.showerror("INFO","Wrong username or password")
            

    def entry(val):
        global new_user_input, new_pwd_input
        if val == 'username':
            new_user_label = Label(frame, text="New Username", padx=20, pady=10, font=('bold', 15))
            new_user_label.grid(row=3, column=0, padx=(30,20))
            
            new_user_input = Entry(frame, borderwidth=2)   
            new_user_input.config(font=('bold', 15)) 
            new_user_input.grid(row=3, column=1, padx=20)

            button = Button(frame, image=submit, relief=FLAT, command=lambda: check(val))
            button.grid(row=4, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)
        else:
            new_pwd_label = Label(frame, text="New Password", padx=20, pady=10, font=('bold', 15))
            new_pwd_label.grid(row=3, column=0, padx=(30,20))
            
            new_pwd_input = Entry(frame, borderwidth=2)   
            new_pwd_input.config(font=('bold', 15)) 
            new_pwd_input.grid(row=3, column=1, padx=20)

            button = Button(frame, image=submit, relief=FLAT, command=lambda: check(val))
            button.grid(row=4, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)

    chn = StringVar()

    Radiobutton(frame, text="Username", variable=chn, value='username', font=('bold', 14), command=lambda: entry('username')).place(x=75, y=130)
    Radiobutton(frame, text="Password", variable=chn, value='password', font=('bold', 14), command=lambda: entry('password')).place(x=225, y=130)


    con.commit()

# store into the database
def vhl_db(v_model, v_no, price, v_type):
    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("INSERT INTO vehicles (vehicle_model, vehicle_no, price_hrs, vehicle_type, available) VALUES (?, ?, ?, ?, ?)", (v_model, v_no, price, v_type, 1))

    con.commit()
    con.close()

# add new vehicle for renting
def add_vehicle():
    add_vhl_win = Toplevel(root)
    add_vhl_win.title("Add Vehicle Window")
    add_vhl_win['bg'] = 'white'

    add_vhl_frame = Frame(add_vhl_win, borderwidth=5, padx=20, pady=20, bg='#7efff5', highlightthickness=2, highlightbackground = "blue", highlightcolor= "blue" )
    add_vhl_frame.pack(padx=30, pady=30)

    # vehicle model widget
    vhl_model_label = Label(add_vhl_frame,text="Vehicle Model", bg='#7efff5', padx=5, pady=5, width=15, anchor=W)
    vhl_model_label.config(font=("Bold",15))
    vhl_model_label.grid(row=0,column=0, padx=15, pady=15, sticky=W)

    vhl_model_entry = Entry(add_vhl_frame,borderwidth=3,width=15, highlightthickness=2)
    vhl_model_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    vhl_model_entry.grid(row=0,column=1, padx=15,sticky=E)

    # vehicle no. widget
    vhl_no_label = Label(add_vhl_frame,text="Vehicle No.", bg='#7efff5', padx=5, pady=5, width=15, anchor=W)
    vhl_no_label.config(font=("Bold",15))
    vhl_no_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    vhl_no_entry = Entry(add_vhl_frame,borderwidth=3,width=15, highlightthickness=2)
    vhl_no_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    vhl_no_entry.grid(row=1,column=1, padx=15,sticky=E)

    # price/hr widget
    price_label = Label(add_vhl_frame,text="Price/hr", bg='#7efff5',padx=5, pady=5, width=15, anchor=W)
    price_label.config(font=("Bold",15))
    price_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    price_entry = Entry(add_vhl_frame,borderwidth=3,width=15, highlightthickness=2)
    price_entry.config(highlightbackground = "#2c3e50", highlightcolor= "#2c3e50", font=myFont, relief=FLAT)
    price_entry.grid(row=2,column=1, padx=15,sticky=E)

    # vehicle type widget
    vehicle_label = Label(add_vhl_frame,text="Vehicle Type", bg='#7efff5', padx=5, pady=5, width=15, anchor=W)
    vehicle_label.config(font=("Bold",15))
    vehicle_label.grid(row=3, column=0, padx=15, pady=25, sticky=W)

    v_type = StringVar()

    Radiobutton(add_vhl_frame, image=bike, variable=v_type, value='bike', bg='#7efff5').place(x=155, y=218)
    Radiobutton(add_vhl_frame, image=scooter, variable=v_type, value='scooter', bg='#7efff5').place(x=255, y=225)
    Radiobutton(add_vhl_frame, image=car, variable=v_type, value='car', bg='#7efff5').place(x=360, y=220)

    button_submit = Button(add_vhl_frame,image=submit,relief=FLAT, bg='#7efff5', command=lambda: vhl_db(vhl_model_entry.get(), vhl_no_entry.get(), price_entry.get(), v_type.get()))
    button_submit.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

# all transaction info displayerd to the admin
def trn_info(startNum, endNum):
    global admin_frame, label

    admin_frame.grid_forget()
    label.grid_forget()

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    label = Label(admin_window, text='Transaction Details', bg='white', fg='#2c3e50', padx=20, pady=20, font=headFont)
    label.grid(row=2, column=1, columnspan=11, padx=50, pady=20)

    admin_frame = Frame(admin_window, padx=5, pady=20, bg='#7efff5', highlightthickness=2, highlightbackground = "blue", highlightcolor= "blue" )
    admin_frame.grid(row=3, column=0, columnspan=13, padx=10)

    b = []

    cur.execute("SELECT * FROM transactions")
    counter = cur.fetchall()

    cur.execute("SELECT * FROM view_table")
    a = cur.fetchmany(endNum)

    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    headers = ['Sl No.', 'ID', 'First Name', 'Last Name', 'DL No.', 'Date & Time', 'Hours', 'Mins.', 'Total', 'Return Time', 'Vehicle No.','Vehicle Model', 'Vehicle Type']
    val = [5, 5, 12, 12, 18, 18, 5, 5, 5, 12, 12, 11, 11]

    table(headers, b, val, startNum, admin_frame, 2, 2)

    if startNum <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, bg='white', state='disabled')
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='normal', bg='white', command=lambda : trn_info(startNum-5, startNum-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if endNum >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, state='disabled', bg='white')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, bg='white', command= lambda: trn_info(endNum+1, endNum+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)

    con.commit()
    con.close()

# Search for particular vehicle's transactions
def search_by_v_no(search_key, startNum, endNum):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, padx=5, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=10)

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    b = []

    cur.execute(f"SELECT * FROM transactions WHERE vehicle_no=?", (search_key, ))
    counter = cur.fetchall()

    cur.execute("SELECT * FROM view_table WHERE vehicle_no=?", (search_key, ))
    a = cur.fetchmany(endNum)

    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    headers = ['Sl No.', 'ID', 'First Name', 'Last Name', 'DL No.', 'Date & Time', 'Hours', 'Mins.', 'Total', 'Return Time', 'Vehicle No.','Vehicle Model', 'Vehicle Type']
    val = [5, 5, 12, 12, 18, 18, 5, 5, 5, 12, 12, 11, 11]

    table(headers, b, val, startNum, admin_frame, 2, 2)

    if startNum <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='normal', command=lambda : search_by_v_no(search_key, startNum-5, startNum-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if endNum >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: search_by_v_no(search_key, endNum+1, endNum+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    con.commit()
    con.close()

# Search a particular customer's transactions
def search_by_dl_no(search_key, startNum, endNum):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, padx=5, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=10)

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    b = []

    cur.execute(f"SELECT * FROM transactions WHERE dl_no=?", (search_key, ))
    counter = cur.fetchall()

    cur.execute("SELECT * FROM view_table WHERE dl_no=?", (search_key, ))
    a = cur.fetchmany(endNum)
    
    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    headers = ['Sl No.', 'ID', 'First Name', 'Last Name', 'DL No.', 'Date & Time', 'Hours', 'Mins.', 'Total', 'Return Time', 'Vehicle No.','Vehicle Model', 'Vehicle Type']
    val = [5, 5, 12, 12, 18, 18, 5, 5, 5, 12, 12, 11, 11]

    table(headers, b, val, startNum, admin_frame, 2, 2)

    if startNum <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='normal', command=lambda : search_by_dl_no(search_key, startNum-5, startNum-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if endNum >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: search_by_dl_no(search_key, endNum+1, endNum+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    con.commit()
    con.close()

# delete a particular transaction OR a vehicle info OR customer info from the database
def delete_db(var, del_key):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    if del_key == '':
        messagebox.showwarning('INDEX ERROR', 'Enter the transaction ID you want to delete.')
    else:
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        if var == 't':
            cur.execute("DELETE FROM transactions WHERE transaction_id=?",(del_key,))
            con.commit()
            con.close()
        elif var == 'v':
            cur.execute("DELETE FROM vehicles WHERE vehicle_no=?",(del_key,))
            con.commit()
            con.close()
        if var == 'c':
            cur.execute("DELETE FROM customers WHERE dl_no=?",(del_key,))
            cur.execute("DELETE FROM customer_phone WHERE dl_no=?",(del_key,))
            cur.execute("DELETE FROM user WHERE dl_no=?",(del_key,))
            con.commit()
            con.close()

# frontend to delete or search a any info
def del_and_src():
    option_frame = Frame(admin_window, borderwidth=4, padx=5, bg='#7efff5', highlightthickness=2, highlightbackground = "red", highlightcolor= "red")
    option_frame.grid(row=1, column=0, columnspan=13, padx=10, pady=10, sticky=W)

    search_frame = Frame(admin_window, borderwidth=4, padx=5, pady=2, bg='#7efff5', highlightthickness=2, highlightbackground = "red", highlightcolor= "red")
    search_frame.grid(row=1, column=0, columnspan=13, padx=(1130,0), pady=10, sticky=W)

    # Delete Transaction
    frame_1 = Frame(option_frame, padx=20, bg='#7efff5')
    frame_1.pack(side='left', padx=20)
    frame_2 = Frame(option_frame, padx=20, bg='#7efff5')
    frame_2.pack(side='left', padx=20)
    frame_3 = Frame(option_frame, padx=20, bg='#7efff5')
    frame_3.pack(side='left', padx=20)

    label = Label(frame_1, text='Delete Transaction Info', font=('Bold', 15), bg='#7efff5')
    label.config(underline=1)
    label.pack(padx=20, pady=10)

    label = Label(frame_1, text='Enter ID:', padx=10, font=('Bold', 20), fg='#2f3640', bg='#7efff5')
    label.pack(padx=20, pady=10)

    delete_t_input = Entry(frame_1, borderwidth=0, width=12, highlightthickness=2)
    delete_t_input.config(highlightbackground = "red", highlightcolor= "red", font=('bold', 20), relief=FLAT)
    delete_t_input.pack(padx=10, pady=10)

    del_btn = Button(frame_1, image=delete, borderwidth=0, bg='#7efff5', relief=FLAT, command=lambda: delete_db('t', delete_t_input.get()))
    del_btn.pack(padx=20, pady=(10,15))

    # Delete Vehicle
    label = Label(frame_2, text='Delete Vehicle Info', bg='#7efff5', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    label = Label(frame_2, text='Enter Vehicle No:', bg='#7efff5', padx=10, font=('Bold', 20), fg='#2f3640')
    label.pack(padx=10, pady=10)

    delete_v_input = Entry(frame_2, font=('bold', 20), borderwidth=0, width=12, highlightthickness=2)
    delete_v_input.config(highlightbackground = "red", highlightcolor= "red", font=('bold', 20), relief=FLAT)
    delete_v_input.pack(padx=20, pady=10)

    del_btn = Button(frame_2, image=delete, borderwidth=0, bg='#7efff5', relief=FLAT, command=lambda: delete_db('v',delete_v_input.get()))
    del_btn.pack(padx=20, pady=(10,15))

    # Delete Customer
    label = Label(frame_3, text='Delete Customer Info', bg='#7efff5', font=('Helvetica', 15))
    label.pack(padx=20, pady=10)

    label = Label(frame_3, text='Enter Customer DL No:', bg='#7efff5', padx=10, font=('Helvetica', 20), fg='#2f3640')
    label.pack(padx=10, pady=10)

    delete_c_input = Entry(frame_3, font=('bold', 20), borderwidth=0, width=12, highlightthickness=2)
    delete_c_input.config(highlightbackground = "red", highlightcolor= "red", font=('bold', 20), relief=FLAT)
    delete_c_input.pack(padx=20, pady=10)

    del_btn = Button(frame_3, image=delete, borderwidth=0, bg='#7efff5', relief=FLAT, command=lambda: delete_db('c',delete_c_input.get()))
    del_btn.config(font=("Helvetica", 15))
    del_btn.pack(padx=20, pady=(10,15))

    # Search Transaction
    label = Label(search_frame, text='Search Transaction By', bg='#7efff5', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    search_v_frame = Frame(search_frame, padx=20, bg='#7efff5')
    search_v_frame.pack(side='left', padx=20)

    search_dl_frame = Frame(search_frame, padx=20, bg='#7efff5')
    search_dl_frame.pack(side='left', padx=20)

    v_label = Label(search_v_frame, text='Vehicle No:', bg='#7efff5', padx=10, font=('Bold', 20), fg='#2f3640')
    v_label.pack(padx=20, pady=10)

    v_input = Entry(search_v_frame, borderwidth=0, width=18, font=('bold', 20), highlightthickness=2)
    v_input.config(highlightbackground = "red", highlightcolor= "red", font=('bold', 20), relief=FLAT)
    v_input.pack(padx=10, pady=10)

    search_btn_2 = Button(search_v_frame, image=search, bg='#7efff5', borderwidth=2, relief=FLAT, command=lambda:search_by_v_no(v_input.get(), 1, 5))
    search_btn_2.config(font=("Helvetica", 15))
    search_btn_2.pack(padx=20, pady=10)

    # Circle image label
    label = Label(search_frame, image=img1, padx=20, pady=20, bg='#7efff5', fg='white')
    label.place(x=340, y=80)
    label = Label(search_frame, text='OR', bg='#7efff5', font=('bold', 15))
    label.place(x=353, y=97)

    dl_label = Label(search_dl_frame, text='DL No:', bg='#7efff5', padx=10, font=('Bold', 20), fg='#2f3640')
    dl_label.pack(padx=20, pady=10)  

    dl_input = Entry(search_dl_frame, borderwidth=0, width=18, highlightthickness=2, font=('bold', 20))
    dl_input.config(highlightbackground = "red", highlightcolor= "red", font=('bold', 20), relief=FLAT)
    dl_input.pack(padx=10, pady=10)

    search_btn_3 = Button(search_dl_frame, image=search, bg='#7efff5', borderwidth=0, relief=FLAT, command=lambda:search_by_dl_no(dl_input.get(), 1, 5))
    search_btn_3.config(font=("Helvetica", 15))
    search_btn_3.pack(padx=20, pady=10)

# Display vehicle info
def display_vhl(s, num):
    global admin_frame, label

    admin_frame.grid_forget()
    label.grid_forget()

    label = Label(admin_window, text='Vehicle Details', bg='white', fg='#2c3e50', padx=20, pady=20, font=headFont)
    label.grid(row=2, column=1, columnspan=11, padx=50, pady=20)

    admin_frame = Frame(admin_window, padx=100, pady=30, bg='#7efff5', highlightthickness=2, highlightbackground = "blue", highlightcolor= "blue" )
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    b = []

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM vehicles")
    counter = cur.fetchall()

    cur.execute("SELECT * FROM vehicles")
    a = cur.fetchmany(num)

    for i in range(s-1,num):   
        if i == len(a):    
            break
        else:
            b.append(a[i])
    

    headers = ['Index No.','Vehicle Model', 'Vehicle No.', 'Price/hr', 'Vehicle Type']
    val = [10, 18, 18, 10, 18]

    for j in range(len(headers)):
        e = Entry(admin_frame, width=val[j], borderwidth=2, bg="#7f8c8d", fg='white', highlightthickness=2)
        e.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        e.grid(row=1, column=j, padx=5, pady=2)
        e.insert(END, headers[j])
    
    for i in range(len(b)):
        if b[i][-1] == 0:
            bg_color = '#e74c3c'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'

        for j in range(len(headers)):
            if j == 0:
                e = Entry(admin_frame, width=10, fg=fg_color, bg=bg_color, borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=5, pady=2)
                e.insert(END, i+s)
            else:
                e = Entry(admin_frame, width=val[j], fg=fg_color, bg=bg_color, borderwidth=2, highlightthickness=2)
                e.config(highlightbackground = "red", highlightcolor= "red", font=myFont, relief=FLAT)
                e.grid(row=i+2, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])

    if s <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, state='disabled', bg='white', relief=FLAT)
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)    
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, relief=FLAT, state='normal', bg='white', command=lambda : display_vhl(s-10, s-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if num >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), padx=10, relief=FLAT, bg='white', state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, bg='white', command= lambda: display_vhl(num+1, num+10))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)

# Display customers info
def display_ctr(s, num):
    global admin_frame, label
    val=0

    admin_frame.grid_forget()
    label.grid_forget()

    label = Label(admin_window, text='Customer\'s Details', bg='white', fg='#2c3e50', padx=20, pady=20, font=headFont)
    label.grid(row=2, column=1, columnspan=11, padx=50, pady=20) 

    admin_frame = Frame(admin_window, borderwidth=4, padx=50, pady=20, bg='#7efff5', highlightthickness=2, highlightbackground = "blue", highlightcolor= "blue" )
    admin_frame.grid(row=3, column=0, columnspan=13, padx=20)

    b = []
    name_ar = []
    d = []

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM customers")
    counter = cur.fetchall()

    cur.execute("SELECT * FROM customers")
    a = cur.fetchmany(num)

    for i in range(len(a)):
        a[i] = list(a[i])

    c = []
    cur.execute("SELECT DISTINCT dl_no FROM customer_phone")
    count = cur.fetchall()

    cur.execute("SELECT * FROM  customer_phone")
    all_no = cur.fetchall()

    for i in range(len(all_no)):
        all_no[i] = list(all_no[i])

    val=0
    f = all_no[-1][-1]
    l = all_no[-2][-1]

    # def phone_num(i, value):
    #     if i < value:
    #         if all_no[i-val][-1] == all_no[i+1-val][-1] :
    #             ph_ar = [all_no[i-val][0], all_no[i+1-val][0]]
    #             ph = ', '.join(ph_ar)       
    #             all_no[i-val][0] = ph        
    #             c.append(all_no[i-val])
    #             all_no.remove(all_no[i-val])
    #             all_no.remove(all_no[i-val])
    #             val+=1
    #         else:
    #             c.append(all_no[i-val])
    #             all_no.remove(all_no[i-val])
    #             val+=1           
    #     else:
    #         c.append(all_no[i-val])
    #         all_no.remove(all_no[i-val])
    #         val+=1

    for i in range(len(count)):
        if f == l:
            # phone_num(i, len(count))
            if i < len(count):
                if all_no[i-val][-1] == all_no[i+1-val][-1] :
                    ph_ar = [all_no[i-val][0], all_no[i+1-val][0]]
                    ph = ', '.join(ph_ar)       
                    all_no[i-val][0] = ph        
                    c.append(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    val+=1
                else:
                    c.append(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    val+=1               
            else:
                c.append(all_no[i-val])
                all_no.remove(all_no[i-val])
                val+=1

        else:
            # phone_num(i, (len(count)-1))
            if i < len(count)-1:
                if all_no[i-val][-1] == all_no[i+1-val][-1] :
                    ph_ar = [all_no[i-val][0], all_no[i+1-val][0]]
                    ph = ', '.join(ph_ar)       
                    all_no[i-val][0] = ph        
                    c.append(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    val+=1
                else:
                    c.append(all_no[i-val])
                    all_no.remove(all_no[i-val])
                    val+=1
                
            else:
                c.append(all_no[i-val])
                all_no.remove(all_no[i-val])
                val+=1

    cur.execute("SELECT username, role FROM user")
    name = cur.fetchall()

    for i in range(len(name)):
        if name[i][1] == 'user':
            name_ar.append(name[i][0])

    for i in range(s-1,num):   
        if i == len(a):    
            break
        else:
            b.append(a[i])
            d.append(name_ar[i])
    
    for i in range(len(b)):
        b[i].insert(5, c[i+s-1][0])
        b[i].insert(6, d[i])

    headers = ['Index No.','First Name', 'Last Name', 'Age', 'DL No.', 'Gender', 'Phone No.', 'Username']
    val = [10, 18, 18, 10, 20, 10, 25, 10]

    table(headers, b, val, s, admin_frame, 5, 2)

    if s <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, state='disabled', bg='white', relief=FLAT)
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)    
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, relief=FLAT, state='normal', bg='white', command=lambda : display_ctr(s-5, s-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if num >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), padx=10, relief=FLAT, state='disabled', bg='white')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, bg='white', command= lambda: display_ctr(num+1, num+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)

# Display particular users transactions
def user_view(person, dl_no):
    user_win = Toplevel(root)
    user_win.title('User Transactions')

    label = Label(user_win, text=f'Transactions of {person}', font=myFont)
    label.pack(pady=20)

    user_frame = Frame(user_win, bg='#7efff5', padx=10, pady=10)
    user_frame.pack(padx=20, pady=20)

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT transaction_id, date_time, hours, minutes, amount, vehicle_no, return_time FROM transactions WHERE dl_no=?", (dl_no, ))
    a = cur.fetchall()

    headers = ['Index No.', 'ID', 'Date&Time', 'Hours', 'Minutes', 'Amount', 'Vehicle No.', 'Return Time']
    val = [10, 10, 25, 10, 10, 10, 15, 15]

    table(headers, a, val, 1, user_frame, 5, 5)

    user_win.mainloop()


def update_db(atr, u_value, key, tab):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    
    if tab == 'vehicle_no':
        cur.execute(f"UPDATE vehicles SET {atr}=? WHERE {tab}=?", (u_value, key))
    elif tab == 'dl_no':
        cur.execute(f"UPDATE customers SET {atr}=? WHERE {tab}=?", (u_value, key))

    con.commit()
    con.close()

# update customer or vehicle info
def update_values(atr, tab):
    if tab == 'vehicle_no':
        label = Label(update_win, text="Enter Vehicle No.", font=myFont, padx=40, pady=5)
        label.grid(row=3, column=2, padx=10, pady=10)

        v_entry = Entry(update_win, width=15, borderwidth=2, highlightthickness=2)
        v_entry.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        v_entry.grid(row=3, column=3, padx=10, pady=10)

        label = Label(update_win, text="Enter Value:", font=myFont, padx=40, pady=5)
        label.grid(row=4, column=2)

        value_entry = Entry(update_win, width=15, borderwidth=2, highlightthickness=2)
        value_entry.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        value_entry.grid(row=4, column=3, padx=10, pady=10)

        button = Button(update_win, image=update_img, relief=FLAT, command=lambda: update_db(atr, value_entry.get(), v_entry.get(), tab))
        button.grid(row=5, column=2, columnspan=5, padx=20, pady=20)

    elif tab == 'dl_no':
        label = Label(update_win, text="Enter Customer DL No.", font=myFont, padx=5, pady=5)
        label.grid(row=3, column=2, padx=10, pady=10)

        c_entry = Entry(update_win, width=15, borderwidth=2, highlightthickness=2)
        c_entry.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        c_entry.grid(row=3, column=3, padx=10, pady=10)

        label = Label(update_win, text="Enter Value:", font=myFont, padx=40, pady=5)
        label.grid(row=4, column=2, padx=10, pady=10)

        value_entry = Entry(update_win, width=15, borderwidth=2, highlightthickness=2)
        value_entry.config(highlightbackground = "#900C3F", highlightcolor= "#900C3F", font=myFont, relief=FLAT)
        value_entry.grid(row=4, column=3, padx=10, pady=10)

        button = Button(update_win, image=update_img, relief=FLAT, command=lambda: update_db(atr, value_entry.get(), c_entry.get(), tab))
        button.grid(row=5, column=2, columnspan=5, padx=20, pady=20)

# update info in database
def update():
    global update_win
    update_win = Toplevel(root)
    update_win.title("Update Window")

    def upadte_info(info):
        update_frame = Frame(update_win, padx=100)
        update_frame.grid(row=2, column=0, columnspan=5)
        
        label = Label(update_frame, text="Select Category:", font=('bold', 30))
        label.grid(row=2, column=0, columnspan=5)

        select = StringVar()

        if info == 'vehicle':
            Radiobutton(update_frame, text="Vehicle No.", variable=select, value='vehicle_no', font=('bold', 15), command=lambda:update_values('vehicle_no','vehicle_no')).grid(row=3, column=1, padx=10, pady=10)
            Radiobutton(update_frame, text="Vehicle Model", variable=select, value='vehicle_model', font=('bold', 15), command=lambda:update_values('vehicle_model','vehicle_no')).grid(row=3, column=1, padx=10, pady=10)
            Radiobutton(update_frame, text="Price/Hr", variable=select, value='price', font=('bold', 15), command=lambda:update_values('price_hrs','vehicle_no')).grid(row=3, column=2, padx=10, pady=10)
            Radiobutton(update_frame, text="Vehicle Type", variable=select, value='type', font=('bold', 15), command=lambda:update_values('vehicle_type','vehicle_no')).grid(row=3, column=3, padx=10, pady=10)
        elif info == 'customer':
            Radiobutton(update_frame, text="First Name", variable=select, value='f_name', font=('bold', 15), command=lambda:update_values('first_name','dl_no')).grid(row=3, column=0, padx=10, pady=10)
            Radiobutton(update_frame, text="Last Name", variable=select, value='l_name', font=('bold', 15), command=lambda:update_values('last_name','dl_no')).grid(row=3, column=1, padx=10, pady=10)
            Radiobutton(update_frame, text="Age", variable=select, value='age', font=('bold', 15), command=lambda:update_values('age','dl_no')).grid(row=3, column=2, padx=10, pady=10)

    label = Label(update_win, text="What do you want to update?", font=('bold', 25)).grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    up = StringVar()

    Radiobutton(update_win, text="Vehicle Info", variable=up, value='vehicle', font=('bold', 15), command=lambda:upadte_info('vehicle')).grid(row=1, column=2, padx=10, pady=10)
    Radiobutton(update_win, text="Customer Info", variable=up, value='customer', font=('bold', 15), command=lambda:upadte_info('customer')).grid(row=1, column=3, padx=10, pady=10)

# admin's window
def access():
    global admin_window, admin_frame, label

    admin_window = Toplevel(root)
    admin_window.title('Admin Window')
    admin_window.state('zoomed')
    admin_window['bg'] = 'white'

    admin_frame = LabelFrame(admin_window, padx=0, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13)

    label = Label(admin_window, bg='white')
    label.grid(row=2, column=2, columnspan=11, padx=30, pady=20)

    # NAVBAR
    topframe = Frame(admin_window, bg="#4bcffa", padx=140)
    topframe.grid(row=0, column=0, columnspan=15, padx=10, pady=(5,0))

    delete_all_btn = Button(topframe, text="Delete All", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=delete_all)
    delete_all_btn.pack(side="left", padx=30)

    change_btn = Button(topframe, text="Username & Password", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=change)
    change_btn.pack(side="left", padx=30)

    add_vehicle_btn = Button(topframe, text="Add Vehicles", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=add_vehicle)
    add_vehicle_btn.pack(side="left", padx=30)

    vehicle_btn = Button(topframe, text="Vehicles Info", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command= lambda: display_vhl(1,10))
    vehicle_btn.pack(side="left", padx=30)

    customers_btn = Button(topframe, text="Customers Info", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=lambda:display_ctr(1, 5))
    customers_btn.pack(side="left", padx=30)

    vehicle_btn = Button(topframe, text="Transactions Info", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=lambda:trn_info(1, 5))
    vehicle_btn.pack(side="left", padx=30)

    vehicle_btn = Button(topframe, text="Update", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=update)
    vehicle_btn.pack(side="left", padx=30)

    del_and_src()
    
    admin_window.mainloop()

# check username and password
def check(username, pwd):
        con = sqlite3.connect('main.db')
        cur = con.cursor()

        cur.execute("SELECT username,role, dl_no FROM user WHERE username=? AND password=?", (username, pwd))
        a = cur.fetchone()

        if a:
            if a[1] == 'admin':
                access()
            elif a[1] == 'user':
                user_view(username, a[2])

        else:
            messagebox.showerror("INFO","Wrong username or password")

        con.commit()
        con.close()

# frontend to check username and password
def admin():
    global log
    log = Toplevel(root)
    log.title("Login Window")

    frame = LabelFrame(log, text="Frame...", borderwidth=4, padx=10,pady=10)
    frame.grid(row=0, column=1, columnspan=2, padx=75,pady=20)

    user_label = Label(frame, text="Username", padx=20, pady=10, font=('bold', 15))
    pwd_label = Label(frame, text="Password", padx=20, pady=10, font=('bold', 15))

    user_label.grid(row=0, column=0)
    pwd_label.grid(row=1, column=0, padx=20)

    user_input = Entry(frame, borderwidth=2)
    pwd_input = Entry(frame, show="*", borderwidth=2)

    user_input.config(font=('bold', 15))
    pwd_input.config(font=('bold', 15))

    user_input.grid(row=0, column=1)
    pwd_input.grid(row=1, column=1, padx=20)


    button = Button(frame, text='Login', padx=10, pady=10, width=12, bg='#0ABDE3', fg='white', font=myFont, command=lambda:check(user_input.get(), pwd_input.get()))
    button.grid(row=2, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)


    log.mainloop()

# --------------------------------- ADMIN WINDOW END ------------------------------------

# display available vehicles
def display(startNum, endNum):
    global available_frame, forward_btn, back_btn

    available_frame.grid_forget()

    available_frame = Frame(root, borderwidth=0, padx=40, pady=20, bg='#7efff5', relief=FLAT)
    available_frame.grid(row=3, column=4, columnspan=7, padx=(20,60), pady=10, sticky=NE)

    b = []

    con = sqlite3.connect('main.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM vehicles WHERE available=1")
    counter = cur.fetchall()

    cur.execute("SELECT * FROM vehicles WHERE available=1")
    a = cur.fetchmany(endNum)

    for i in range(startNum-1,endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])
    

    headers = ['Index No.','Vehicle Model', 'Vehicle No.', 'Price/hr', 'Vehicle Type']
    val = [10, 18, 18, 10, 18]

    table(headers, b, val, startNum, available_frame, 5, 5)

    if startNum <= 1:
        back_btn = Button(available_frame, image=bck, bg='#7efff5', padx=10, state='disabled', relief=FLAT)
        back_btn.grid(row=0, column=0, padx=10, pady=(20, 40), sticky=W)
    else:
        back_btn = Button(available_frame, image=bck, bg='#7efff5', padx=10, relief=FLAT, state='normal', command=lambda : display(startNum-10, startNum-1))
        back_btn.grid(row=0, column=0, padx=10, pady=(20, 40), sticky=W)

    if endNum >= len(counter):
            forward_btn = Button(available_frame, image=fwd, bg='#7efff5', padx=10, relief=FLAT, state='disabled')
            forward_btn.grid(row=0, column=4, padx=10, pady=(20, 40), sticky=E)
    else:
        forward_btn = Button(available_frame, image=fwd, bg='#7efff5', relief=FLAT, padx=10, command= lambda: display(endNum+1, endNum+10))
        forward_btn.grid(row=0, column=4, padx=10, pady=(20, 40), sticky=E)

    con.commit()
    con.close()

display(1, 10)

# clock function
def clock():
    hour = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am_pm = time.strftime("%p")

    dayNum = time.strftime("%d")
    month = time.strftime("%b")
    year = time.strftime("%Y")
    day = time.strftime("%A")

    date_label.config(text= dayNum +' '+ month +' '+ year +'   '+ day)

    time_label.config(text= hour +':'+ min +':'+ sec +' '+ am_pm)
    time_label.after(1000, clock)

clr = ['#f1c40f','#f39c12','#0A79DF','#2ecc71','#2c3e50','#c0392b','#22a6b3','#f6e58d']

def color():
    num1 = random.randint(0,7)
    c1 = clr[num1]
    num2 = random.randint(0,7)
    c2 = clr[num2]
    available_frame['bg']=c1
    add_customer_frame['bg'] = c1
    booking_frame['bg'] = c1
    return_frame['bg'] = c1
    forward_btn['bg']=c1
    back_btn['bg']=c1
    
    # HEADING LABEL
    head_label = Label(root, text="Vehicle Rental Management System", bg=c2, fg="white", width=50, padx=28,pady=10)
    head_label.config(font=("Bold",47))
    head_label.grid(row=0,column=0,columnspan=8,padx=5,pady=5)

#******************************************************************** FRONT-END ******************************************************************************
# HEADING LABEL
head_label = Label(root, text="Vehicle Rental Management System",background="#002f6c",fg="white",width=50,padx=28,pady=10)
head_label.config(font=("Bold",47))
head_label.grid(row=0,column=0,columnspan=8,padx=5,pady=5)

# TIME frame
topframe = Frame(root, bg="#01579b", padx=46)
topframe.grid(row=1, column=0, columnspan=13, padx=5)

date_label = Label(topframe, text='', font=("bold", 18), fg="white", bg="#01579b", pady=5, relief=FLAT)
date_label.pack(side="left", padx=(0,330), anchor=W)

title = Button(topframe, text='RENT-IT', font=myFont, fg="white", bg="#01579b", pady=5, relief=FLAT, command=color)
title.pack(side="left", padx=330, anchor=W)

time_label = Label(topframe, text='', font=("bold", 18), fg="white", bg="#01579b", pady=5, relief=FLAT)
time_label.pack(side="left", padx=(330,0), anchor=E)

clock()

# NAVBAR frame
topframe = Frame(root, bg="#4bcffa", padx=250)
topframe.grid(row=2, column=0, columnspan=8, padx=5, pady=5,sticky=N)

add_customer_btn = Button(topframe, text="Add Customer", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=customer_info)
add_customer_btn.pack(side="left", padx=60)

book_vehicle_btn = Button(topframe, text="Book Vehicle", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=booking_info)
book_vehicle_btn.pack(side="left", padx=60)

return_btn = Button(topframe, text="Return Vehicle", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=return_vehicle)
return_btn.pack(side="left", padx=60)

available_vehicle_btn = Button(topframe, text="Available Vehicles", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=lambda: display(1, 10))
available_vehicle_btn.pack(side="left", padx=60)

login_btn = Button(topframe, text="Login", font=("bold", 18), fg="white", bg="#4bcffa", relief=FLAT, command=admin)
login_btn.pack(side="left", padx=60)

add_label = Label(topframe, image=add_cust, bg="#4bcffa")
add_label.place(x=20, y=0)
book_label = Label(topframe, image=booking, bg="#4bcffa")
book_label.place(x=318, y=0)
return_label = Label(topframe, image=return2, bg="#4bcffa")
return_label.place(x=600, y=0)
login_label = Label(topframe, image=login, bg="#4bcffa")
login_label.place(x=1230, y=0)

root.mainloop()
