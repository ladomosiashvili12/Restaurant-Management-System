import sqlite3
import re



'''მომხმარებლების ცხრილი სადაც ინახება მათი სარეგისტრაციო ინფორმაცია'''
conn = sqlite3.connect('customers.db')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# cursor.execute('''create table if not exists customers(
#                id integer primary key autoincrement,
#                username Nvarchar(50),
#                phone varchar(50),
#                email varchar(100),
#                password varchar(50)
#                )''')
# conn.commit()


# gift_card-ის დამატება
# cursor.execute('''ALTER TABLE customers ADD COLUMN gift_card INTEGER DEFAULT 0''')
# conn.commit()


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
            return"❌ ეს ნომერი უკვე დარეგისტრირებულია"
            # return False

        cursor.execute("""
            INSERT INTO customers (username, phone, email, password)
            VALUES (?, ?, ?, ?)
        """, (self.username, self.phone, self.email, self.password))
        conn.commit()
        # print("✅ მონაცემები შენახულია ბაზაში!")
        return True


        # ამოწმებს ყველაფერს თუ ყველაფერი სწორია იძახებს save_to_db მეთოდს 
    def checkR(self):
        if not self.email:
            return ""
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
        
        result = self.save_to_db()
        if result is True:
            return  "✅ წარმატებით შეხვედით"
        else:
            return result


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
            return "✅მომხმარებელი წარმატებით შევიდა"
        else:
            return "❌ პაროლი ან მომხმარებელი არასწორია"


        



'''მენეჯერის ვერიფიკაცია mail=manager123@res.mng.ge და password=manager1234'''
class verification:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
    
    def checker(self):
        if self.mail == "manager123@res.mng.ge" and self.password == "manager1234":
            return True
        else:
            return False
    



#  მენიუს შექმნის ნაწილი  #

conn1 = sqlite3.connect('menu.db') # db3; sqlite, sqlite3
conn1.row_factory = sqlite3.Row

cursor1 = conn1.cursor()


# cursor1.execute('''create table if not exists menu(
#                id integer primary key AUTOINCREMENT,
#                product_name Nvarchar(100),
#                price float 
#                )''')
# conn1.commit()


# menu_lst = [
#     # წყალი / WATER
#     ("წყალი 0.5ლ/ Borjomi 0.5L", 1.0),
#     ("ბორჯომი 1ლ / Borjomi 1L", 2.0),

#     # სასმელები / SOFT DRINKS
#     ("კოკა-კოლა 1ლ / Coca-Cola 1L", 3.5),
#     ("კოკა-კოლა 0.5ლ / Coca-Cola 0.5L", 2.0),
#     ("ლიმონათი / Lemonade", 2.0),

#     # ცხელი სასმელები / HOT DRINKS
#     ("ყავა ესპრესო / Espresso", 4.0),
#     ("ყავა კაპუჩინო / Cappuccino", 6.0),
#     ("ყავა ლატე / Latte", 7.0),
#     ("ამერიკანო / Americano", 5.0),

#     # ლუდი / BEER
#     ("ლუდი ნატახტარი 0.5ლ / Natakhtari Beer 0.5L", 4.5),
#     ("ლუდი ზედაზენი 0.5ლ / Zedazeni Beer 0.5L", 4.0),
#     ("ლუდი ჰაინეკენი 0.5ლ / Heineken 0.33L", 5.0),

#     # ღვინო / WINE
#     ("ღვინო წითელი 1ლ/ Red Wine (glass) 1L", 8.5),
#     ("ღვინო თეთრი 1ლ/ White Wine (glass) 1L", 8.5),
#     # აპეტაიზერი / APPETIZER
#     ("ყველი იმერული / Imeruli Cheese", 9.0),
#     ("გუდის ყველი / Guda Cheese", 19.0),
#     ("სულგუნი / Sulguni Cheese", 12.0),
#     ("ქართული ყველის დაფა / Georgian Cheese Board", 45.0),
#     ("მწნილის ასორტი / Assorted pickle veggies", 14.0),
#     ("ზეთისხილი / Olives", 8.0),
#     ("ბადრიჯანი ნიგვზით / Eggplant with walnuts", 8.0),

#     # სალათები / SALADS
#     ("კიტრი-პომიდვრის სალათი / Cucumber&Tomato Salad", 10.0),
#     ("ქათმის სალათი / Chicken Salad", 14.0),
#     ("ბერძნული სალათი / Greek Salad", 18.0),
#     ("ცეზარი / Caesar Salad", 23.0),
#     ("მწვანე სალათი / Green Salad", 20.0),

#     # წვნიანები / SOUPS
#     ("სოკოს კრემ-სუპი / Mashroom Cream-Soup", 16.0),
#     ("სოკოს სუპი / Mashroom Soup", 14.0),
#     ("ჩიხირთმა / Chikhirtma", 13.0),

#     # ძირითადი კერძები / MAIN DISHES
#     ("სოკო კეცზე / Mashrooms on Ketsi", 16.0),
#     ("შემწვარი წიწილა / Roasted Chicken", 25.0),
#     ("შქმერული / 'Shkmeruli'", 30.0),
#     ("ოჯახური (ღორის) / 'Ojakhuri' (with pork)", 17.0),
#     ("სოკოს ოჯახური / 'Ojakhuri' with mushrooms", 15.0),
#     ("ოსტრი / 'Ostri' (spicy beef stew)", 21.0),
#     ("ჩაქონდრილი / 'Chakondrili' with savory", 25.0),
#     ("ქათმის ფრთები / Chicken Wings", 18.0),
#     ("კოტლეტი / Cutlets", 13.0),
#     ("მწვადი ღორის / Pork Barbecue", 18.0),
#     ("ქაბაბი / Kebab", 19.0),
#     ("კალმახი / Trout", 15.0),

#     # ცომეული / BAKED GOODS
#     ("ხაჭაპური იმერული / Khachapuri 'Imeruli'", 19.0),
#     ("ლობიანი / Lobiani", 17.0),
#     ("კუბდარი /'Kubdari'", 23.0),
#     ("პიცა პეპერონი / Pizza Pepperoni", 25.0),
#     ("პიცა მარგარიტა / Pizza Margarita", 27.0),
#     ("მჭადი / Mchadi", 2.0),
#     ("პური / Bread", 2.0),

#     # გარნირი / GARNISH
#     ("კარტოფილი ფრი / French Fries", 7.0),
#     ("კარტოფილი მექსიკურად / Mexican Potatoes", 13.0),

#     # სოუსები / SAUCES
#     ("აჯიკა / Adjika", 5.0),
#     ("საწებელი / Tomato sauce", 3.0),
#     ("მაიონეზი / Mayonnaise", 3.0),
#     ("ტყემალი / Tkemali Sauce", 3.0),

#     # დესერტი / DESSERTS
#     ("ბლინი ბანანით და შოკოლადით / Pancake with Banana&Chocolate", 15.0),
#     ("ბლინი ნიგვზის ფანტელებით / Pancake with Walnut Flocks", 15.0),
#     ("ბლინი ჯემით / Pancake with Jam", 10.0),
#     ("სეზონური ხილის ასორტი / Assorted Seasonal Fruits", 22.0),
#     ("ნაყინი / Ice Cream", 6.0)

# ]


# cursor1.executemany('''insert into menu(product_name, price)
#                    values(?, ?)''', menu_lst)


# conn1.commit()

'''ძირითადი მენიუ'''
# def get_menu():
#     cursor1.execute('SELECT * FROM menu')
#     items = cursor1.fetchall()
#     return [(item['product_name'], item['price']) for item in items]


'''სასაჩუქრე ბარათები თუ აქვს'''
def check_gift_card(login):
    # მომხმარებლის id-ს ვიღებთ
    cursor.execute("SELECT id, gift_card FROM customers WHERE email=? OR username=?", (login, login))
    user = cursor.fetchone()
    
    if not user:
        return False
    
    # რომელი ნომრის წევრია
    cursor.execute("SELECT id FROM customers ORDER BY id")
    all_ids = [row['id'] for row in cursor.fetchall()]
    position = all_ids.index(user['id']) + 1
    
    # ყოველ მე-15 წევრს gift_card მიენიჭება
    if position % 15 == 0 and user['gift_card'] == 0:
        cursor.execute("UPDATE customers SET gift_card=1 WHERE id=?", (user['id'],))
        conn.commit()
    
    return user['gift_card'] == 1


def get_menu(login=None):
    cursor1.execute('SELECT * FROM menu')
    items = cursor1.fetchall()
    
    discount = False
    if login:
        discount = check_gift_card(login)
    
    result = []
    for item in items:
        price = item['price']
        if discount:
            price = round(price * 0.8, 2)  # 20% ფასდაკლება
        result.append((item['product_name'], price))
    
    return result, discount

# print(gift_card())



