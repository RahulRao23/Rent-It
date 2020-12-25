from tkinter import * 
from tkinter import messagebox
import datetime
import time
import sqlite3
from faker import Faker

root = Tk()
root.state('zoomed')

img1 = PhotoImage(file='circle2.png')
fwd = PhotoImage(file='fwd.png')
bck = PhotoImage(file='bck.png')

#Connect to a database
con = sqlite3.connect('test.db')
cur = con.cursor()

#Create VEHICLES table
cur.execute("""CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_model text,
    vehicle_no text PRIMARY KEY,
    price_hrs integer,
    vehicle_type text,
    available integer DEFAULT 1
) """)

con.commit()


#Create RENTED table
cur.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name text,
    last_name text,
    age integer,
    phone_no text,
    dl_no text PRIMARY KEY,
    gender text
) """)

con.commit()

#Create BOOKED table
cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
    date_time text,
    hours integer,
    minutes integer,
    amount int,
    vehicle_no text,
    dl_no text,
    vehicle_returned integer,
    FOREIGN KEY(vehicle_no) REFERENCES vehicles(vehicle_no)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY(dl_no) REFERENCES customers(dl_no)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) """)

con.commit()

#Create MAINTAINER table
cur.execute("""CREATE TABLE IF NOT EXISTS maintainer (
    username text PRIMARY KEY,
    password text
) """)

con.commit()

con.close()

# ****************************************** FRAMES *************************************************
# CUSTOMER FRAME
add_customer_frame = LabelFrame(root, text='Add Customer...', borderwidth=5)
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
def customer_db(f_name, l_name, age, ph_no, dl_no, gen):
    first_name = f_name
    last_name = l_name
    age = age
    phone_no = ph_no
    dl_number = dl_no
    gender = gen

    values = [first_name, last_name, age, phone_no, dl_number, gender]

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("INSERT INTO customers(first_name, last_name, age, phone_no, dl_no, gender) VALUES (?, ?, ?, ?, ?, ?)", values)

    con.commit()

    # cur.execute("SELECT * FROM customers")
    # a = cur.fetchall()
    
    # for i in range(len(a)):
    #     print(a[i])

    # con.commit()

    con.close()


def customer_info():
    add_customer_btn['state'] = 'disabled'
    book_vehicle_btn['state'] = 'normal'
    return_btn['state'] = 'normal'

    booking_frame.grid_forget()
    return_frame.grid_forget()

    global add_customer_frame

    add_customer_frame = LabelFrame(root, text='Add Customer...', borderwidth=5, padx=20, pady=20)
    add_customer_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #first name widget
    first_name_label = Label(add_customer_frame,text="First Name", padx=5, pady=5, width=15, anchor=W)
    first_name_label.config(font=("Bold",15))
    first_name_label.grid(row=0,column=0, padx=15, pady=15, sticky=W)

    first_name_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    first_name_entry.config(font=8)
    first_name_entry.grid(row=0,column=1, padx=15,sticky=E)

    #last name widget
    last_name_label = Label(add_customer_frame,text="Last Name", padx=5, pady=5, width=15, anchor=W)
    last_name_label.config(font=("Bold",15))
    last_name_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    last_name_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    last_name_entry.config(font=8)
    last_name_entry.grid(row=1,column=1, padx=15,sticky=E)

    #age widget
    age_label = Label(add_customer_frame,text="Age",padx=5, pady=5, width=15, anchor=W)
    age_label.config(font=("Bold",15))
    age_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    age_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    age_entry.config(font=8)
    age_entry.grid(row=2,column=1, padx=15,sticky=E)

    #phone number widget
    phone_no_label = Label(add_customer_frame,text="Phone No", padx=5, pady=5, width=15, anchor=W)
    phone_no_label.config(font=("Bold",15))
    phone_no_label.grid(row=3,column=0, padx=15, pady=15, sticky=W)

    phone_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    phone_entry.config(font=8)
    phone_entry.grid(row=3,column=1, padx=15,sticky=E)

    #DL number widget
    dl_no_label = Label(add_customer_frame,text="DL Number", padx=5, pady=5, width=15, anchor=W)
    dl_no_label.config(font=("Bold",15))
    dl_no_label.grid(row=4,column=0, padx=15, pady=15, sticky=W)

    dl_no_entry = Entry(add_customer_frame,borderwidth=3,width=15)
    dl_no_entry.config(font=8)
    dl_no_entry.grid(row=4,column=1, padx=15,sticky=E)

    #gender number widget
    gender_label = Label(add_customer_frame,text="Gender", padx=5, pady=5, width=12, anchor=W)
    gender_label.config(font=("Bold",15))
    gender_label.grid(row=5,column=0, padx=15, pady=15, sticky=W)

    frame_2 = LabelFrame(add_customer_frame)
    frame_2.grid(row=5, column=1, columnspan=3)

    r = StringVar()

    Radiobutton(add_customer_frame, text="Male", variable=r, value="M", font=("Bold",12)).place(x=200, y=350)
    Radiobutton(add_customer_frame, text="Female", variable=r, value="F", font=("Bold",12)).place(x=265, y=350)
    Radiobutton(add_customer_frame, text="Others", variable=r, value="Other", font=("Bold",12)).place(x=350, y=350)

    button_submit = Button(add_customer_frame,text="Submit",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED, command=lambda: customer_db(first_name_entry.get(), last_name_entry.get(), age_entry.get(), phone_entry.get(), dl_no_entry.get(), r.get()))
    button_submit.config(font=("Helvetica", 15))
    button_submit.grid(row=6, column=0, columnspan=3, padx=20, pady=20)

# ------------------- ADD INFO END ---------------------


# -------------------- BOOKING INFO ----------------------
def available_vehicles(vehicle):
    global available_frame

    available_frame.grid_forget()

    available_frame = LabelFrame(root, text='vehicles available', borderwidth=4, padx=20, pady=20)
    available_frame.grid(row=2, rowspan=3, column=2, columnspan=7, padx=(0,60), pady=40, sticky=NE)

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM vehicles WHERE vehicle_type = ? AND available=1", (vehicle, ))
    a = cur.fetchall()

    headers = ['Index','Vehicle Model', 'Vehicle No.', 'Price/hr']

    for j in range(4):
        if j == 0 :
            e = Entry(available_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=20, pady=5)
            e.insert(END, headers[j])
        if j in [1,2]:
            e = Entry(available_frame, width=20, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=20, pady=5)
            e.insert(END, headers[j])
        else:
            e = Entry(available_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=20, pady=5)
            e.insert(END, headers[j])

    for i in range(len(a)):
        for j in range(len(headers)):
            if j == 0:
                e = Entry(available_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=10, pady=5)
                e.insert(END, i+1)
            elif j in [1,2]:
                e = Entry(available_frame, width=20, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=10, pady=5)
                e.insert(END, a[i][j-1])
            else:
                e = Entry(available_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=10, pady=5)
                e.insert(END, a[i][j-1])

    con.commit()


def book_db(hour, minute, vehicle_no, dl_no):
    vehicle_id = vehicle_no
    dl_number = dl_no

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

        con = sqlite3.connect('test.db')
        cur = con.cursor()

        cur.execute("SELECT * FROM transactions")
        num = cur.fetchall()

        if len(num) == 0:
            tran_id = 1000
        else:
            tran_id = int(num[len(num)-1][7]) + 1
            
        tran_id = str(tran_id)

        cur.execute("UPDATE vehicles SET available=0 WHERE vehicle_no = ?", (vehicle_id, ))

        cur.execute("INSERT INTO transactions (date_time, hours, minutes, amount, vehicle_no, dl_no, vehicle_returned, transaction_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (dateTime, hour, minute, 0, vehicle_id, dl_number, 0, tran_id))

        con.commit()


def booking_info():
    global booking_frame

    add_customer_btn['state'] = 'normal'
    book_vehicle_btn['state'] = 'disabled'
    return_btn['state'] = 'normal'

    add_customer_frame.grid_forget()
    return_frame.grid_forget()

    booking_frame = LabelFrame(root, text='Book Vehicle...', borderwidth=5, padx=50, pady=20)
    booking_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    # vehicle widget
    vehicle_label = Label(booking_frame,text="Vehicle", padx=5, pady=5, anchor=W)
    vehicle_label.config(font=("Bold",25))
    vehicle_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

    v_type = StringVar()

    Radiobutton(booking_frame, text="Bike", variable=v_type, value='bike', font=('bold', 17)).place(x=155, y=25)
    Radiobutton(booking_frame, text="Scooter", variable=v_type, value='scooter', font=('bold', 17)).place(x=240, y=25)
    Radiobutton(booking_frame, text="Car", variable=v_type, value='car', font=('bold', 17)).place(x=360, y=25)

    serach_btn = Button(booking_frame, text="Search", padx=32, pady=9, fg="white", background="#2ecc72", borderwidth=2, relief=RAISED, command=lambda: available_vehicles(v_type.get()))
    serach_btn.config(font=("Helvetica", 10))
    serach_btn.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

    # dl_no widget
    dl_no_label = Label(booking_frame,text="DL No.", padx=5, pady=5, anchor=W)
    dl_no_label.config(font=("Bold",25))
    dl_no_label.grid(row=2, column=0, padx=15, pady=15, sticky=W)

    dl_no = Entry(booking_frame, borderwidth=3, width=15)
    dl_no.config(font=8)
    dl_no.grid(row=2, column=1, padx=15, pady=15, sticky=E)

    # duration widget
    duration_label = Label(booking_frame,text="Duration", padx=5, pady=5, anchor=W)
    duration_label.config(font=("Bold",25))
    duration_label.grid(row=3, column=0, padx=15, pady=15, sticky=W)

    # Hours Entry
    hour_list = [0, 1, 2, 3, 4]

    hour_val = IntVar()

    hour_menu = OptionMenu(booking_frame, hour_val, *hour_list)
    hour_menu.grid(row=3, column=1, padx=15, pady=15, sticky=W)
    hour_val.set(hour_list[0])

    hrs_label = Label(booking_frame,text="hrs")
    hrs_label.config(font=("Bold",15))
    hrs_label.place(x=277, y=275)

    # Minutes Entry
    min_val = IntVar()

    min_menu = OptionMenu(booking_frame, min_val, 0, 30)
    min_menu.place(x=330, y=270)
    min_val.set(hour_list[0])

    min_label = Label(booking_frame, text="mins")
    min_label.config(font=("Bold",15))
    min_label.place(x=385, y=272) 
 

    #vehicle_no widget
    vehicle_no_label = Label(booking_frame,text="Vehicle No.", padx=5, pady=5, anchor=W)
    vehicle_no_label.config(font=("Bold",25))
    vehicle_no_label.grid(row=4, column=0, padx=15, pady=15, sticky=W)

    vehicle_no_entry = Entry(booking_frame,borderwidth=3,width=15)
    vehicle_no_entry.config(font=8)
    vehicle_no_entry.grid(row=4, column=1, padx=15, pady=15, sticky=E)

    add_customer = Button(booking_frame, text="Book Vehicle", padx=32, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda: book_db(hour_val.get(), min_val.get(), vehicle_no_entry.get(), dl_no.get()))
    add_customer.config(font=("Helvetica", 15))
    add_customer.grid(row=5, column=0, columnspan=3, padx=20, pady=20)

# --------------------- BOOKING INFO END ----------------------


# --------------------- RETURN INFO -------------------------

def return_db(vehicle_no_etr):
    vehicle_no = vehicle_no_etr

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    #To get current time
    t = time.localtime()   
    time2 = str(t[3])+':'+str(t[4])+':'+str(t[5])
    
    cal2 = time2.split(':')

    cur.execute("SELECT date_time FROM transactions WHERE vehicle_no=? AND vehicle_returned=?", (vehicle_no, 0))
    date_time = cur.fetchone()
    date_time1 = list(date_time)
    
    t = [subl.split() for subl in date_time1] 
    time1 = t[0][1]
    cal1 = time1.split(':')
    
    h_time = int(cal2[0]) - int(cal1[0])
    m_time = int(cal2[1]) - int(cal1[1])
    m_time = m_time / 60
    total_time = h_time + m_time 
    
    cur.execute(f"SELECT {total_time}*price_hrs FROM vehicles WHERE vehicle_no=?", (vehicle_no, ))
    amount = cur.fetchone()

    total = int(amount[0])

    cur.execute("UPDATE vehicles SET available=1 WHERE vehicle_no = ?", (vehicle_no, ))

    cur.execute("UPDATE transactions SET vehicle_returned=1, amount=?, return_time=? WHERE vehicle_no=?", (total, time2, vehicle_no, ))

    amount_label = Label(return_frame, text='Total Rent:', font=('Bold', 20), padx=30, pady=30, fg="#2ecc72")
    amount_label.grid(row=3, column=0, columnspan=3, padx=20, pady=30)

    amount_label = Label(return_frame, text=total, font=('Bold', 25), padx=30, pady=30)
    amount_label.grid(row=3, column=0, columnspan=3, padx=20, pady=30)

    con.commit()


def return_vehicle():
    global return_frame 

    add_customer_btn['state'] = 'normal'
    book_vehicle_btn['state'] = 'normal'
    return_btn['state'] = 'disabled'

    add_customer_frame.grid_forget()
    booking_frame.grid_forget()

    return_frame = LabelFrame(root, text='Return Vehicle...', borderwidth=4)
    return_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    #vehicle_no widget
    vehicle_no_label = Label(return_frame,text="Vehicle No.", padx=5, pady=5, anchor=W)
    vehicle_no_label.config(font=("Bold",25))
    vehicle_no_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

    vehicle_no_etr = Entry(return_frame,borderwidth=3,width=20)
    vehicle_no_etr.config(font=10)
    vehicle_no_etr.grid(row=0, column=1, padx=20, pady=20, sticky=E)

    confirm_return = Button(return_frame, text="Return Vehicle", padx=32, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda: return_db(vehicle_no_etr.get()))
    confirm_return.config(font=("Helvetica", 15))
    confirm_return.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
    

# --------------------- RETURN INFO END -------------------------



# ---------------------- ADMIN WINDOW ------------------------

def delete_all():
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    a = messagebox.askyesno('DELETE ALL', 'Are you sure you want to delete all transactions?')

    if a:
        cur.execute("DELETE FROM transactions")

    con.commit()
    con.close()


def change():
    change_window = Toplevel(root)

    frame = LabelFrame(change_window, text="Frame...", borderwidth=4, padx=10,pady=10)
    frame.grid(row=0, column=1, columnspan=2, padx=75,pady=20)

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM maintainer")
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
                    cur.execute("UPDATE maintainer SET username=?",(new_user, ))
                    con.commit()
                    con.close()
                    change_window.destroy()
                else:
                    messagebox.showerror("INFO","Wrong username or password")
            elif val == 'password':
                new_pwd = new_pwd_input.get()
                if username == user[0][0] and old_pwd == user[0][1]:
                    cur.execute("UPDATE maintainer SET password=?",(new_pwd, ))
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

            button = Button(frame,text="Change", padx=10, pady=10, width=12, bg='#0ABDE3', fg='white', font=('system', 20), command=lambda: check(val))
            button.grid(row=4, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)
        else:
            new_pwd_label = Label(frame, text="New Password", padx=20, pady=10, font=('bold', 15))
            new_pwd_label.grid(row=3, column=0, padx=(30,20))
            
            new_pwd_input = Entry(frame, borderwidth=2)   
            new_pwd_input.config(font=('bold', 15)) 
            new_pwd_input.grid(row=3, column=1, padx=20)

            button = Button(frame,text="Change", padx=10, pady=10, width=12, bg='#0ABDE3', fg='white', font=('system', 20), command=lambda: check(val))
            button.grid(row=4, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)

    chn = StringVar()

    Radiobutton(frame, text="Username", variable=chn, value='username', font=('bold', 14), command=lambda: entry('username')).place(x=75, y=130)
    Radiobutton(frame, text="Password", variable=chn, value='password', font=('bold', 14), command=lambda: entry('password')).place(x=225, y=130)


    con.commit()


def vhl_db(v_model, v_no, price, v_type):
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("INSERT INTO vehicles (vehicle_model, vehicle_no, price_hrs, vehicle_type, available) VALUES (?, ?, ?, ?, ?)", (v_model, v_no, price, v_type, 1))

    con.commit()
    con.close()


def add_vehicle():
    add_vhl_win = Toplevel(root)

    add_vhl_frame = LabelFrame(add_vhl_win, text='Add Vehicle...', borderwidth=5, padx=20, pady=20)
    add_vhl_frame.grid(row=2, column=0, columnspan=4, padx=20, pady=40, sticky=N)

    # vehicle model widget
    vhl_model_label = Label(add_vhl_frame,text="Vehicle Model", padx=5, pady=5, width=15, anchor=W)
    vhl_model_label.config(font=("Bold",15))
    vhl_model_label.grid(row=0,column=0, padx=15, pady=15, sticky=W)

    vhl_model_entry = Entry(add_vhl_frame,borderwidth=3,width=15)
    vhl_model_entry.config(font=8)
    vhl_model_entry.grid(row=0,column=1, padx=15,sticky=E)

    # vehicle no. widget
    vhl_no_label = Label(add_vhl_frame,text="Vehicle No.", padx=5, pady=5, width=15, anchor=W)
    vhl_no_label.config(font=("Bold",15))
    vhl_no_label.grid(row=1,column=0, padx=15, pady=15, sticky=W)

    vhl_no_entry = Entry(add_vhl_frame,borderwidth=3,width=15)
    vhl_no_entry.config(font=8)
    vhl_no_entry.grid(row=1,column=1, padx=15,sticky=E)

    # price/hr widget
    price_label = Label(add_vhl_frame,text="Price/hr",padx=5, pady=5, width=15, anchor=W)
    price_label.config(font=("Bold",15))
    price_label.grid(row=2,column=0, padx=15, pady=15, sticky=W)

    price_entry = Entry(add_vhl_frame,borderwidth=3,width=15)
    price_entry.config(font=8)
    price_entry.grid(row=2,column=1, padx=15,sticky=E)

    # vehicle type widget
    vehicle_label = Label(add_vhl_frame,text="Vehicle Type", padx=5, pady=5, width=15, anchor=W)
    vehicle_label.config(font=("Bold",15))
    vehicle_label.grid(row=3, column=0, padx=15, pady=15, sticky=W)

    v_type = StringVar()

    Radiobutton(add_vhl_frame, text="Bike", variable=v_type, value='bike', font=('bold', 14)).place(x=155, y=220)
    Radiobutton(add_vhl_frame, text="Scooter", variable=v_type, value='scooter', font=('bold', 14)).place(x=240, y=220)
    Radiobutton(add_vhl_frame, text="Car", variable=v_type, value='car', font=('bold', 14)).place(x=360, y=220)

    button_submit = Button(add_vhl_frame,text="Add Vehicle",padx=32,pady=9,fg="white",background="#0ABDE3",borderwidth=2,relief=RAISED, command=lambda: vhl_db(vhl_model_entry.get(), vhl_no_entry.get(), price_entry.get(), v_type.get()))
    button_submit.config(font=("Helvetica", 15))
    button_submit.grid(row=4, column=0, columnspan=3, padx=20, pady=20)


def print_trn(counter, b, idx):
    headers = ['Sl No.', 'ID', 'First Name', 'Last Name', 'DL No.', 'Date & Time', 'Hours', 'Mins.', 'Total', 'Return Time', 'Vehicle No.','Vehicle Model', 'Vehicle Type']

    for j in range(13):
        if j == 0:
            e = Entry(admin_frame, width=5, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])
        elif j in [1,6,7,8]:
            e = Entry(admin_frame, width=5, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])
        elif j in [2,3,9,10]:
            e = Entry(admin_frame, width=12, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])
        elif j == 4:
            e = Entry(admin_frame, width=18, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])
        elif j in [11,12]:
            e = Entry(admin_frame, width=11, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])
        else:
            e = Entry(admin_frame, width=20, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=0, column=j, padx=5, pady=2)
            e.insert(END, headers[j])

    for i in range(len(b)):
        for j in range(13):
            if j == 0:
                e = Entry(admin_frame, width=5, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, i+idx)
            elif j in [1,6,7,8]:
                e = Entry(admin_frame, width=5, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])
            elif j in [2,3,9,10]:
                e = Entry(admin_frame, width=12, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])
            elif j == 4:
                e = Entry(admin_frame, width=18, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])
            elif j in [11,12]:
                e = Entry(admin_frame, width=11, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])
            else:
                e = Entry(admin_frame, width=20, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+1, column=j, padx=5, pady=2)
                e.insert(END, b[i][j-1])


def trn_info(startNum, endNum):
    global admin_frame

    admin_frame.grid_forget()

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    admin_frame = LabelFrame(admin_window, padx=5, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    b = []

    cur.execute("SELECT * FROM transactions")
    counter = cur.fetchall()

    cur.execute(f"""SELECT t.transaction_id, c.first_name, c.last_name, t.dl_no, t.date_time, t.hours, t.minutes, t.amount, t.return_time, v.vehicle_no, v.vehicle_model, v.vehicle_type 
                    FROM transactions t, vehicles v, customers c
                    WHERE t.dl_no=c.dl_no AND t.vehicle_no=v.vehicle_no""")
    a = cur.fetchmany(endNum)

    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    print_trn(counter, b, startNum)

    if startNum <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), relief=FLAT, padx=10, state='normal', command=lambda : trn_info(startNum-5, startNum-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if endNum >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: trn_info(endNum+1, endNum+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)

    con.commit()
    con.close()


def delete_db(var, del_key):
        if del_key == '':
            messagebox.showwarning('INDEX ERROR', 'Enter the transaction ID you want to delete.')
        else:
            con = sqlite3.connect('test.db')
            cur = con.cursor()
            if var == 't':
                cur.execute("DELETE FROM transactions WHERE transaction_id=?",(del_key,))
                con.commit()
                con.close()
            elif var == 'v':
                cur.execute("DELETE FROM vehicles WHERE vehicle_no=?",(del_key,))
                con.commit()
                con.close()
            if var == 't':
                cur.execute("DELETE FROM customers WHERE dl_no=?",(del_key,))
                con.commit()
                con.close()


def search_by_v_no(search_key, startNum, endNum):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, padx=5, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    b = []

    cur.execute(f"SELECT * FROM transactions WHERE vehicle_no=?", (search_key, ))
    counter = cur.fetchall()

    cur.execute(f"""SELECT t.transaction_id, c.first_name, c.last_name, t.dl_no, t.date_time, t.hours, t.minutes, t.amount, t.return_time, v.vehicle_no, v.vehicle_model, v.vehicle_type 
                        FROM transactions t, vehicles v, customers c
                        WHERE t.dl_no=c.dl_no AND t.vehicle_no=v.vehicle_no AND t.vehicle_no=?""", (search_key, ))
    a = cur.fetchmany(endNum)
    
    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    print_trn(counter, b, startNum)

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

    # else:
    #     cur.execute(f"""SELECT t.transaction_id, c.first_name, c.last_name, t.dl_no, t.date_time, t.hours, t.minutes, t.amount, t.return_time, v.vehicle_no, v.vehicle_model, v.vehicle_type 
    #                         FROM transactions t, vehicles v, customers c
    #                         WHERE t.dl_no=c.dl_no AND t.vehicle_no=v.vehicle_no AND t.dl_no=?""",(search_key, ))
    #     a = cur.fetchall()
    #     for i in range(len(a)):
    #         print(a[i])
    #     con.commit()
    #     con.close()


def search_by_dl_no(search_key, startNum, endNum):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, padx=5, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    b = []

    cur.execute(f"SELECT * FROM transactions WHERE dl_no=?", (search_key, ))
    counter = cur.fetchall()

    cur.execute(f"""SELECT t.transaction_id, c.first_name, c.last_name, t.dl_no, t.date_time, t.hours, t.minutes, t.amount, t.return_time, v.vehicle_no, v.vehicle_model, v.vehicle_type 
                        FROM transactions t, vehicles v, customers c
                        WHERE t.dl_no=c.dl_no AND t.vehicle_no=v.vehicle_no AND t.dl_no=?""", (search_key, ))
    a = cur.fetchmany(endNum)
    
    for i in range(startNum-1, endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])

    print_trn(counter, b, startNum)

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


def del_and_src():

    option_frame = LabelFrame(admin_window, text='Delete Transaction...', borderwidth=4, padx=10)
    option_frame.grid(row=1, column=0, columnspan=13, padx=20, pady=10, sticky=W)

    search_frame = LabelFrame(admin_window, text='Search...', borderwidth=4, padx=10)
    search_frame.grid(row=1, column=0, columnspan=13, padx=(1130,0), pady=10, sticky=W)

    # Delete Transaction
    frame_1 = Frame(option_frame, padx=20)
    frame_1.pack(side='left', padx=20)
    frame_2 = Frame(option_frame, padx=20)
    frame_2.pack(side='left', padx=20)
    frame_3 = Frame(option_frame, padx=20)
    frame_3.pack(side='left', padx=20)

    label = Label(frame_1, text='Delete Transaction Info', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    label = Label(frame_1, text='Enter ID:', padx=10, font=('Bold', 20), fg='#2f3640')
    label.pack(padx=20, pady=10)

    delete_t_input = Entry(frame_1, font=('bold', 20), borderwidth=0, width=12)
    delete_t_input.pack(padx=10, pady=10)

    del_btn = Button(frame_1, text="Delete", padx=20, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda: delete_db('t',delete_t_input.get()))
    del_btn.config(font=("Helvetica", 15))
    del_btn.pack(padx=20, pady=10)

    # Delete Vehicle
    label = Label(frame_2, text='Delete Vehicle Info', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    label = Label(frame_2, text='Enter Vehicle No:', padx=10, font=('Bold', 20), fg='#2f3640')
    label.pack(padx=10, pady=10)

    delete_v_input = Entry(frame_2, font=('bold', 20), borderwidth=0, width=12)
    delete_v_input.pack(padx=20, pady=10)

    del_btn = Button(frame_2, text="Delete", padx=20, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda: delete_db('v',delete_v_input.get()))
    del_btn.config(font=("Helvetica", 15))
    del_btn.pack(padx=20, pady=10)

    # Delete Customer
    label = Label(frame_3, text='Delete Customer Info', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    label = Label(frame_3, text='Enter Customer DL No:', padx=10, font=('Bold', 20), fg='#2f3640')
    label.pack(padx=10, pady=10)

    delete_c_input = Entry(frame_3, font=('bold', 20), borderwidth=0, width=12)
    delete_c_input.pack(padx=20, pady=10)

    del_btn = Button(frame_3, text="Delete", padx=20, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda: delete_db('c',delete_c_input.get()))
    del_btn.config(font=("Helvetica", 15))
    del_btn.pack(padx=20, pady=10)

    # Search Transaction
    label = Label(search_frame, text='Search Transaction By', font=('Bold', 15))
    label.pack(padx=20, pady=10)

    search_v_frame = Frame(search_frame, padx=20)
    search_v_frame.pack(side='left', padx=20)

    search_dl_frame = Frame(search_frame, padx=20)
    search_dl_frame.pack(side='left', padx=20)

    v_label = Label(search_v_frame, text='Vehicle No:', padx=10, font=('Bold', 20), fg='#2f3640')
    v_label.pack(padx=20, pady=10)

    v_input = Entry(search_v_frame, borderwidth=0, width=18, font=('bold', 20))
    v_input.pack(padx=10, pady=10)

    search_btn_2 = Button(search_v_frame, text="Search", padx=20, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda:search_by_v_no(v_input.get(), 1, 5))
    search_btn_2.config(font=("Helvetica", 15))
    search_btn_2.pack(padx=20, pady=10)

    # Circle image label
    label = Label(search_frame, image=img1, padx=20, pady=20, fg='white')
    label.place(x=340, y=80)
    label = Label(search_frame, text='OR', font=('bold', 15))
    label.place(x=353, y=97)

    dl_label = Label(search_dl_frame, text='DL No:', padx=10, font=('Bold', 20), fg='#2f3640')
    dl_label.pack(padx=20, pady=10)  

    dl_input = Entry(search_dl_frame, borderwidth=0, width=18, font=('bold', 20))
    dl_input.pack(padx=10, pady=10)

    search_btn_3 = Button(search_dl_frame, text="Search", padx=20, pady=9, fg="white", background="#0ABDE3", borderwidth=2, relief=RAISED, command=lambda:search_by_dl_no(dl_input.get(), 1, 5))
    search_btn_3.config(font=("Helvetica", 15))
    search_btn_3.pack(padx=20, pady=10)


def display_vhl(s, num):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, text='vehicles Info...', font=("bold", 15), borderwidth=4, padx=100, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    b = []

    con = sqlite3.connect('test.db')
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

    for j in range(5):
        if j == 0:
                e = Entry(admin_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
                e.grid(row=1, column=j, padx=10, pady=10)
                e.insert(END, headers[j])
        elif j in [1,2,4]:
            e = Entry(admin_frame, width=18, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=10, pady=10)
            e.insert(END, headers[j])
        else:
            e = Entry(admin_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=10, pady=10)
            e.insert(END, headers[j])

    for i in range(len(b)):
        if b[i][-1] == 0:
            bg_color = '#e74c3c'
            fg_color = 'white'
        else:
            bg_color = 'white'
            fg_color = 'black'

        for j in range(5):
            if j == 0:
                e = Entry(admin_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'), fg=fg_color, bg=bg_color)
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, i+s)
            elif j in [1,2,4]:
                e = Entry(admin_frame, width=18, borderwidth=2, font=('Arial', 16, 'bold'), fg=fg_color, bg=bg_color)
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, b[i][j-1])
            else:
                e = Entry(admin_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'), fg=fg_color, bg=bg_color)
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, b[i][j-1])

    if s <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, state='disabled', relief=FLAT)
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)    
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, relief=FLAT, state='normal', command=lambda : display_vhl(s-10, s-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if num >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), padx=10, relief=FLAT, state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: display_vhl(num+1, num+10))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)


def display_ctr(s, num):
    global admin_frame

    admin_frame.grid_forget()

    admin_frame = LabelFrame(admin_window, text='Customers Info...', font=("bold", 15), borderwidth=4, padx=100, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13, padx=50)

    b = []

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM customers")
    counter = cur.fetchall()

    cur.execute("SELECT * FROM customers")
    a = cur.fetchmany(num)

    for i in range(s-1,num):   
        if i == len(a):    
            break
        else:
            b.append(a[i])
    

    headers = ['Index No.','First Name', 'Last Name', 'Age', 'Phone No.', 'DL No.', 'Gender']

    for j in range(7):
        if j == 0:
                e = Entry(admin_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
                e.grid(row=1, column=j, padx=10, pady=10)
                e.insert(END, headers[j])
        elif j in [1,2,4]:
            e = Entry(admin_frame, width=18, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=10, pady=10)
            e.insert(END, headers[j])
        elif j == 5:
            e = Entry(admin_frame, width=20, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=10, pady=10)
            e.insert(END, headers[j])
        else:
            e = Entry(admin_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=10, pady=10)
            e.insert(END, headers[j])

    for i in range(len(b)):
        for j in range(7):
            if j == 0:
                e = Entry(admin_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, i+s)
            elif j in [1,2,4]:
                e = Entry(admin_frame, width=18, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, b[i][j-1])
            elif j == 5:
                e = Entry(admin_frame, width=20, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, b[i][j-1])
            else:
                e = Entry(admin_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=10, pady=5)
                e.insert(END, b[i][j-1])

    if s <= 1:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, state='disabled', relief=FLAT)
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)    
    else:
        back_btn = Button(admin_window, image=bck, font=('bold', 30), padx=10, relief=FLAT, state='normal', command=lambda : display_ctr(s-5, s-1))
        back_btn.grid(row=2, column=1, padx=(50,0), pady=20, sticky=W)

    if num >= len(counter):
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), padx=10, relief=FLAT, state='disabled')
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)
    else:
        forward_btn = Button(admin_window, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: display_ctr(num+1, num+5))
        forward_btn.grid(row=2, column=11, padx=(0,50), pady=20, sticky=E)


def access():
    global admin_window, admin_frame

    admin_window = Toplevel(root)
    admin_window.state('zoomed')

    admin_frame = LabelFrame(admin_window, padx=0, pady=20)
    admin_frame.grid(row=3, column=0, columnspan=13)

    # NAVBAR
    topframe = Frame(admin_window, bg="#2ecc72", padx=220)
    topframe.grid(row=0, column=0, columnspan=15, padx=10, pady=(5,0))

    delete_all_btn = Button(topframe, text="Delete All", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=delete_all)
    delete_all_btn.pack(side="left", padx=30)

    change_btn = Button(topframe, text="Username & Password", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=change)
    change_btn.pack(side="left", padx=30)

    add_vehicle_btn = Button(topframe, text="Add Vehicles", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=add_vehicle)
    add_vehicle_btn.pack(side="left", padx=30)

    vehicle_btn = Button(topframe, text="Vehicles Info", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command= lambda: display_vhl(1,10))
    vehicle_btn.pack(side="left", padx=30)

    customers_btn = Button(topframe, text="Customers Info", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=lambda:display_ctr(1, 5))
    customers_btn.pack(side="left", padx=30)

    vehicle_btn = Button(topframe, text="Transactions Info", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=lambda:trn_info(1, 5))
    vehicle_btn.pack(side="left", padx=30)

    del_and_src()
    #trn_info(1, 5)
    
    admin_window.mainloop()


def admin():
    global log
    log = Tk()

    frame = LabelFrame(log, text="Frame...", borderwidth=4, padx=10,pady=10)
    frame.grid(row=0, column=1, columnspan=2, padx=75,pady=20)

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM maintainer")
    user = cur.fetchall()

    user_label = Label(frame, text="Username", padx=20, pady=10, font=('bold', 15))
    pwd_label = Label(frame, text="Password", padx=20, pady=10, font=('bold', 15))

    user_label.grid(row=0, column=0)
    pwd_label.grid(row=1, column=0, padx=20)

    user_input = Entry(frame, borderwidth=2)
    pwd_input = Entry(frame, borderwidth=2)

    user_input.config(font=('bold', 15))
    pwd_input.config(font=('bold', 15))

    user_input.grid(row=0, column=1)
    pwd_input.grid(row=1, column=1, padx=20)


    def check():
        username = user_input.get()
        pwd = pwd_input.get()

        if username == user[0][0] and pwd == user[0][1]:
            access()              
        else:
            messagebox.showerror("INFO","Wrong username or password")
            log.destroy()


    button = Button(frame,text="Login", padx=10, pady=10, width=12, bg='#0ABDE3', fg='white', font=('system', 20), command=check)
    button.grid(row=2, column=0, columnspan=2, padx=20, pady=30, sticky=W+E)

    con.commit()
    con.close()

    log.mainloop()

# --------------------------------- ADMIN WINDOW END ------------------------------------


def display(startNum, endNum):
    global available_frame

    available_frame.grid_forget()

    available_frame = LabelFrame(root, text='vehicles available', borderwidth=4, padx=40, pady=20)
    available_frame.grid(row=3, column=4, columnspan=7, padx=(20,60), pady=20, sticky=NE)

    b = []

    con = sqlite3.connect('test.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM vehicles WHERE available=1")
    counter = cur.fetchall()

    cur.execute(f"SELECT rowid,* FROM vehicles WHERE available=1")
    a = cur.fetchmany(endNum)

    for i in range(startNum-1,endNum):   
        if i == len(a):    
            break
        else:
            b.append(a[i])
    

    headers = ['Index No.','Vehicle Model', 'Vehicle No.', 'Price/hr', 'Vehicle Type']

    for j in range(5):
        if j == 0:
                e = Entry(available_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
                e.grid(row=1, column=j, padx=5, pady=10)
                e.insert(END, headers[j])
        elif j in [1,2,4]:
            e = Entry(available_frame, width=18, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=5, pady=10)
            e.insert(END, headers[j])
        else:
            e = Entry(available_frame, width=10, borderwidth=2, bg="lightblue", font=('Arial', 16, 'bold'))
            e.grid(row=1, column=j, padx=5, pady=10)
            e.insert(END, headers[j])

    for i in range(len(b)):
        for j in range(5):
            if j == 0:
                e = Entry(available_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=5, pady=5)
                e.insert(END, i+startNum)
            elif j in [1,2,4]:
                e = Entry(available_frame, width=18, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=5, pady=5)
                e.insert(END, b[i][j])
            else:
                e = Entry(available_frame, width=10, borderwidth=2, font=('Arial', 16, 'bold'))
                e.grid(row=i+2, column=j, padx=5, pady=5)
                e.insert(END, b[i][j])

    if startNum <= 1:
        back_btn = Button(available_frame, image=bck, font=('bold', 30), padx=10, state='disabled', relief=FLAT)
        back_btn.grid(row=0, column=0, padx=10, pady=(20, 40), sticky=W)
    else:
        back_btn = Button(available_frame, image=bck, font=('bold', 30), padx=10, relief=FLAT, state='normal', command=lambda : display(startNum-10, startNum-1))
        back_btn.grid(row=0, column=0, padx=10, pady=(20, 40), sticky=W)

    if endNum >= len(counter):
            forward_btn = Button(available_frame, image=fwd, font=('bold', 30), padx=10, relief=FLAT, state='disabled')
            forward_btn.grid(row=0, column=4, padx=10, pady=(20, 40), sticky=E)
    else:
        forward_btn = Button(available_frame, image=fwd, font=('bold', 30), relief=FLAT, padx=10, command= lambda: display(endNum+1, endNum+10))
        forward_btn.grid(row=0, column=4, padx=10, pady=(20, 40), sticky=E)

    con.commit()

display(1, 10)

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


#******************************************************************** FRONT-END ******************************************************************************
# HEADING LABEL
head_label = Label(root, text="Vehicle Rental Management System",background="#0A79DF",fg="white",width=50,padx=28,pady=10)
head_label.config(font=("Bold",47))
head_label.grid(row=0,column=0,columnspan=8,padx=5,pady=5)

#time frame
topframe = Frame(root, bg="#00b894", padx=60)
topframe.grid(row=1, column=0, columnspan=13, padx=5)

date_label = Label(topframe, text='', font=("bold", 18), fg="#6D214F", bg="#00b894", pady=5, relief=FLAT)
date_label.pack(side="left", padx=(0,330), anchor=W)

title = Label(topframe, text='RENT-IT', font=("helvetica", 18), fg="white", bg="#00b894", pady=5, relief=FLAT)
title.pack(side="left", padx=330, anchor=W)

time_label = Label(topframe, text='', font=("bold", 18), fg="#6D214F", bg="#00b894", pady=5, relief=FLAT)
time_label.pack(side="left", padx=(330,0), anchor=E)

clock()

# NAVBAR
topframe = Frame(root, bg="#2ecc72", padx=400)
topframe.grid(row=2, column=0, columnspan=8, padx=5, pady=5,sticky=N)

add_customer_btn = Button(topframe, text="Add Customer", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=customer_info)
add_customer_btn.pack(side="left", padx=30)

book_vehicle_btn = Button(topframe, text="Book Vehicle", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=booking_info)
book_vehicle_btn.pack(side="left", padx=30)

return_btn = Button(topframe, text="Return Vehicle", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=return_vehicle)
return_btn.pack(side="left", padx=30)

available_vehicle_btn = Button(topframe, text="Available Vehicles", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=lambda: display(1, 10, 1))
available_vehicle_btn.pack(side="left", padx=30)

login_btn = Button(topframe, text="Login", font=("bold", 18), fg="white", bg="#2ecc72", relief=FLAT, command=access)
login_btn.pack(side="left", padx=30)


root.mainloop()
