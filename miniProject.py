# 1. Fonksiyon Tanımları
# Parametre alan boş bir fonksiyon
def greet_user(username):
    print(f"Welcome, {username}!")

# Parametre alan işlevsel bir fonksiyon
def add_product(name, quantity, price):
    product = {'name': name, 'quantity': quantity, 'price': price}
    products.append(product)
    print(f"Product {name} added successfully.")

# Depolanan ürünleri gösteren bir fonksiyon
def display_products():
    print("Products in the warehouse:")
    for product in products:
        print(f"{product['name']}: {product['quantity']} units, Price: {product['price']}")

# 2. Fonksiyonların Kullanımı
# Kullanıcıyı selamla
greet_user("Abdulrezak")

# Ürün ekle
products = []  # Ürünleri depolamak için bir liste
add_product("Apple", 100, 1.5)
add_product("Banana", 50, 1)

# Depolanan ürünleri göster
display_products()

# 3. Döngü kullanarak depolanan ürünleri göster
def display_products():
    print("Products in the warehouse:")
    print("=" * 30)
    for product in products:
        print(f"{product['name']}: {product['quantity']} units, Price: {product['price']}")

# 4. Ürünleri depolamak için bir liste kullanın ve listeler için en az 4 yöntem kullanın
products = []

# Eleman ekleme
def add_product(name, quantity, price):
    product = {'name': name, 'quantity': quantity, 'price': price}
    products.append(product)
    print(f"Product {name} added successfully.")

# Eleman çıkarma
def remove_product(name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            print(f"Product {name} removed successfully.")
            return
    print(f"Product {name} not found.")

# Listeyi güncelleme
def update_product(name, new_quantity, new_price):
    for product in products:
        if product['name'] == name:
            product['quantity'] = new_quantity
            product['price'] = new_price
            print(f"Product {name} updated successfully.")
            return
    print(f"Product {name} not found.")

# Elemanlara erişim
def get_product(name):
    for product in products:
        if product['name'] == name:
            return product
    return None

# Deneme ürünleri ekleme
add_product("Apple", 100, 1.5)
add_product("Banana", 50, 1)

# Döngü kullanarak depolanan ürünleri göster
display_products()

# Ürün çıkarma
remove_product("Apple")

# Ürün güncelleme
update_product("Banana", 60, 1.2)

# Değişikliklerden sonra depolanan ürünleri göster
display_products()

# 5. En az dört string yöntemi kullanın
example_string = "hello world"

# Harfleri büyük harflere dönüştürme
upper_case = example_string.upper()
print("Upper case:", upper_case)

# Stringleri birleştirme
new_string = example_string + ", welcome!"
print("Joined strings:", new_string)

# Stringleri bölme
split_string = example_string.split(" ")
print("Split string:", split_string)

# Bir stringde metin arama
if "world" in example_string:
    print("Found 'world' in the string.")
else:
    print("Not found.")

print("=" * 30)

# 6. Dosya kavramını kullanma
# Depo verilerini bir dosyada saklama
def store_data(filename):
    try:
        with open(filename, 'w') as file:
            for product in products:
                file.write(f"{product['name']},{product['quantity']},{product['price']}\n")
        print("Data stored successfully.")
    except Exception as e:
        print("An error occurred while storing data:", e)

# Depo verilerini dosyadan geri yükleme
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, quantity, price = line.strip().split(",")
                add_product(name, int(quantity), float(price))
        print("Data loaded successfully.")
    except Exception as e:
        print("An error occurred while loading data:", e)

# Depo verilerini saklama
store_data("products.txt")

# Başka ürünler ekleme
add_product("Orange", 75, 2)
add_product("Grapes", 30, 3)

# Depo verilerini geri yükleme
load_data("products.txt")

# Geri yüklenen ürünleri göster
display_products()

import re

# 7. Düzenli ifadeler kullanarak arama fonksiyonu ekleyin
def search_product(pattern):
    found_products = []
    for product in products:
        if re.search(pattern, product['name'], re.IGNORECASE):
            found_products.append(product)
    return found_products

# İsminde "apple" kelimesi olan ürünleri arama
search_result = search_product("apple")
if search_result:
    print("Search results:")
    for product in search_result:
        print(f"Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")
else:
    print("No matching products found.")

# 8. Nihai program çıktısı
print("\nFinal Warehouse Inventory:")
display_products()
