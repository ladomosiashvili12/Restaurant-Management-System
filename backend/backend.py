import sqlite3
import re



# '''მომხმარებლების ცხრილი სადაც ინახება მათი სარეგისტრაციო ინფორმაცია'''
conn = sqlite3.connect('customers.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute('''create table if not exists customers(
               id integer primary key autoincrement,
               username Nvarchar(50),
               phone varchar(50),
               email varchar(100),
               password varchar(50)
               )''')
conn.commit()


'''ეს კლასსი ამოწმებს მომხმარებელთა რეგისტრაციას და ინფორმაციას'''
class customerR:
    def __init__(self, username,  phone, email, password):
        self.username = username
        self.phone = phone
        self.email = email
        self.password = password
        self.pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z_-]+(?:\.[a-zA-Z_-]+)*\.[a-zA-Z]+$"
        self.has_digit = False
        self.has_upper = False
        self.has_special = False
        self.check_mail = False
        self.number = False

    def save_to_db(self):
        cursor.execute("SELECT * FROM customers WHERE email = ?", (self.email,))
        if cursor.fetchone():
            return "❌ ეს მეილი უკვე რეგისტრირებულია!"
            # return False

        cursor.execute("SELECT * FROM customers WHERE username = ?", (self.username,))
        if cursor.fetchone():
            return "❌ ეს მომხმარებლის სახელი უკვე დაკავებულია!"
            # return False
        
        cursor.execute("select * from customers Where phone = ?", (self.phone,))
        if cursor.fetchone():
            return"❌ ეს ნომერი უკვე დარეგისტრრირებულია"
            # return False

        cursor.execute("""
            INSERT INTO customers (username, phone, email, password)
            VALUES (?, ?, ?, ?)
        """, (self.username, self.phone, self.email, self.password))
        conn.commit()
        # print("✅ მონაცემები შენახულია ბაზაში!")
        return True

    def checkR(self):
        if re.match(self.pattern, self.email):
            self.check_mail = True
        
        if not self.check_mail:
            return "❌ მეილი არასწორია"

        if len(self.password) < 8:
            return "❌ პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო"
    
        for char in self.password:
            if char.isdigit():
                self.has_digit = True
            elif char.isupper():
                self.has_upper = True
            elif not char.isalnum():
                self.has_special = True

    
        if not self.has_digit:
            return "❌ პაროლი უნდა შეიცავდეს მინიმუმ ერთ რიცხვს!"

        if not self.has_upper:
            return "❌ პაროლი უნდა შეიცავდეს მინიმუმ ერთ დიდ ასოს!"
    
        if not self.has_special:
            return "❌ პაროლი უნდა შეიცავდეს მინიმუმ ერთ სიმბოლოს (!, @, #, $, და ა.შ.)!"

        if len(self.phone) == 9 and self.phone.isdigit():
            self.number = True

        if not self.number:
            return "❌ ტელეფონის ნომერი არასწორია"
        

        if self.has_digit and self.has_upper and self.has_special and self.check_mail and self.number and self.save_to_db():
            self.save_to_db()
            return "✅ წარმატებით შეხვედით"
            

        

# C1 = customerR("ლადო", '123456789', "lado123@gmail.com","Ladomosk123!")
# C1.checkR()

# C2 = customerR("მათე", "987654321", "mate123@gmail.com", "Mateber123!")
# C2.checker()

# C3 = customerR("lado", "12345", "lado123@gm1.com", "lado123")
# C3.checker()

# C1 = customerR("ლადო", '123456789', "lado123@gmail.com","Ladomosk123!")
# C1.checker()


'''მომხმარებლების ავტორიზაცია თუ უკვე გავლილი აქვს რეგისტრაცია'''

class customerV:
    def __init__(self, login, password):
        if "@" in login:               #ნახულობს მეილით შედის თუ სახელით
            self.username = None
            self.email = login
        else:
            self.username = login
            self.email = None
        self.password = password
        self.ver_email = {}  # დარეგისტრირებული მეილები
        self.ver_name = {}  # დარეგისტრირებული სახელები


         #ამოწმებს მომხმარებელს შეყავს თუ არა სწორი მონაცემები და აბრუნებს შესაბამის ინფორმაციას
    def checkV(self):
        cursor.execute("SELECT email, username, password FROM customers")
        rows = cursor.fetchall()

        for row in rows:
            self.ver_email[row['email']] = row['password']
            self.ver_name[row['username']] = row['password']

        if self.email:
            correct_password = self.ver_email.get(self.email)
        else:
            correct_password = self.ver_name.get(self.username)

        if correct_password and correct_password == self.password:
            print("✅მომხმარებელი წარმატებით შევიდა")
        else:
            print("❌ პაროლი ან მომხმარებელი არასწორია")

C1 = customerV("ლადო", "Ladomosk123!")
C1.checkV()

C = customerV("lado123@gmail.com", "Ladomosk123!")
C.checkV()

C2 = customerV("მათე", "Mateber123!")
C2.checkV()
        


        




'''მენეჯერის ვერიფიკაცია mail=manager123@res.mng.ge და password=manager1234'''
# class verification:
#     def __init__(self, mail, password):
#         self.mail = mail
#         self.password = password
    
#     def checker(self):
#         if self.mail == "manager123@res.mng.ge" and self.password == "manager1234":
#             return True
#         else:
#             return False
    