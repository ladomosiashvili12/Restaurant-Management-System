import sqlite3

conn = sqlite3.connect('menu.db') # db3; sqlite, sqlite3
conn.row_factory = sqlite3.Row

cursor = conn.cursor()


cursor.execute('''create table if not exists menu(
               id integer primary key AUTOINCREMENT,
               product_name Nvarchar(100),
               price float 
               )''')


menu_lst = [
    # აპეტაიზერი / APPETIZER
    ("ყველი იმერული / Imeruli Cheese", 9.0),
    ("გუდის ყველი / Guda Cheese", 19.0),
    ("სულგუნი / Sulguni Cheese", 12.0),
    ("ქართული ყველის დაფა / Georgian Cheese Board", 45.0),
    ("მწნილის ასორტი / Assorted pickle veggies", 14.0),
    ("ზეთისხილი / Olives", 8.0),
    ("ბადრიჯანი ნიგვზით / Eggplant with walnuts", 8.0),

    # სალათები / SALADS
    ("კიტრი-პომიდვრის სალათი / Cucumber&Tomato Salad", 10.0),
    ("ქათმის სალათი / Chicken Salad", 14.0),
    ("ბერძნული სალათი / Greek Salad", 18.0),
    ("ცეზარი / Caesar Salad", 23.0),
    ("მწვანე სალათი / Green Salad", 20.0),

    # წვნიანები / SOUPS
    ("სოკოს კრემ-სუპი / Mashroom Cream-Soup", 16.0),
    ("სოკოს სუპი / Mashroom Soup", 14.0),
    ("ჩიხირთმა / Chikhirtma", 13.0),

    # ძირითადი კერძები / MAIN DISHES
    ("სოკო კეცზე / Mashrooms on Ketsi", 16.0),
    ("შემწვარი წიწილა / Roasted Chicken", 25.0),
    ("შქმერული / 'Shkmeruli'", 30.0),
    ("ოჯახური (ღორის) / 'Ojakhuri' (with pork)", 17.0),
    ("სოკოს ოჯახური / 'Ojakhuri' with mushrooms", 15.0),
    ("ოსტრი / 'Ostri' (spicy beef stew)", 21.0),
    ("ჩაქონდრილი / 'Chakondrili' with savory", 25.0),
    ("ქათმის ფრთები / Chicken Wings", 18.0),
    ("კოტლეტი / Cutlets", 13.0),
    ("მწვადი ღორის / Pork Barbecue", 18.0),
    ("ქაბაბი / Kebab", 19.0),
    ("კალმახი / Trout", 15.0),

    # ცომეული / BAKED GOODS
    ("ხაჭაპური იმერული / Khachapuri 'Imeruli'", 19.0),
    ("ლობიანი / Lobiani", 17.0),
    ("კუბდარი /'Kubdari'", 23.0),
    ("პიცა პეპერონი / Pizza Pepperoni", 25.0),
    ("პიცა მარგარიტა / Pizza Margarita", 27.0),
    ("მჭადი / Mchadi", 2.0),
    ("პური / Bread", 2.0),

    # გარნირი / GARNISH
    ("კარტოფილი ფრი / French Fries", 7.0),
    ("კარტოფილი მექსიკურად / Mexican Potatoes", 13.0),

    # სოუსები / SAUCES
    ("აჯიკა / Adjika", 5.0),
    ("საწებელი / Tomato sauce", 3.0),
    ("მაიონეზი / Mayonnaise", 3.0),
    ("ტყემალი / Tkemali Sauce", 3.0),

    # დესერტი / DESSERTS
    ("ბლინი ბანანით და შოკოლადით / Pancake with Banana&Chocolate", 15.0),
    ("ბლინი ნიგვზის ფანტელებით / Pancake with Walnut Flocks", 15.0),
    ("ბლინი ჯემით / Pancake with Jam", 10.0),
    ("სეზონური ხილის ასორტი / Assorted Seasonal Fruits", 22.0),
    ("ნაყინი / Ice Cream", 6.0)

]


cursor.executemany('''insert into menu(product_name, price, image_path)
                   values(?, ?, ?)''', menu_lst)



# conn.commit()
# conn.close()

def get_menu():
    conn = sqlite3.connect("menu.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM menu").fetchall()

    conn.close()
    return data

