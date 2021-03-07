import sqlite3

#Connect to a database
con = sqlite3.connect('main.db')
cur = con.cursor()

#Create VEHICLES table
cur.execute("""CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_model text,
    vehicle_no text PRIMARY KEY,
    price_hrs integer,
    vehicle_type text,
    available integer DEFAULT 1
) """)


#Create RENTED table
cur.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name text,
    last_name text,
    age integer,
    dl_no text PRIMARY KEY,
    gender text
) """)


#Create BOOKED table
cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
    date_time text,
    hours integer,
    minutes integer,
    amount int,
    vehicle_no text,
    dl_no text,
    vehicle_returned integer,
    transaction_id text PRIMARY KEY,
    FOREIGN KEY(vehicle_no) REFERENCES vehicles(vehicle_no)
    ON UPDATE CASCADE,
    FOREIGN KEY(dl_no) REFERENCES customers(dl_no)
    ON UPDATE CASCADE
) """)


#Create USER table
cur.execute("""CREATE TABLE IF NOT EXISTS user (
    username text PRIMARY KEY,
    password text,
    role text,
    dl_no text,
    FOREIGN KEY (dl_no) REFERENCES customers(dl_no)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) """)

con.commit()

# cur.execute("ALTER TABLE transactions ADD return_time text")
# con.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS customer_phone(
    phone_no text ,
    dl_no text,
    PRIMARY KEY (phone_no, dl_no),
    FOREIGN KEY (dl_no) REFERENCES customers(dl_no)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    )""")


cur.execute("""CREATE VIEW IF NOT EXISTS view_table
        AS 
        SELECT t.transaction_id, c.first_name, c.last_name, t.dl_no, t.date_time, t.hours, t.minutes, t.amount, t.return_time, v.vehicle_no, v.vehicle_model, v.vehicle_type 
                        FROM transactions t, vehicles v, customers c
                        WHERE t.dl_no=c.dl_no AND t.vehicle_no=v.vehicle_no""")


con.commit()
con.close()