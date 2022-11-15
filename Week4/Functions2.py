product_list = []
Courier_list = []
shopping_basket = {}
orders = []
product = {}
courier = {}
orders_list = []
items = []

# def products_order():
#     with open('products123.txt', 'r') as f:
#         for line in f.readlines():
#             product_list.append(line.strip("\n"))
#             print()


def create_product():
    new_product = input("add new product: ")
    new_price = input("add New Price: ")
    product["name"] = new_product
    product["price"] = new_price
    product_list.append(product)
    print(product_list)


def update_product():
    for i in enumerate(product_list):
        print(i)
    idx_product = int(input("Product index that needs to be changed: "))
    upd_product = input("Put in updated product")
    upd_price = input(" Put in price")
    product_list[idx_product]["name"] = upd_product
    product_list[idx_product]["price"] = upd_price
    print(product_list)


def delete_product():
    for i in enumerate(product_list):
        print(i)
    index_p = int(input(" choose index that needs to be deleted: "))
    del product_list[index_p]
    print(product_list)


# def courier_order():
#     with open('people.txt', 'r') as f:
#         for line in f.readlines():
#             Courier_list.append(line.strip("\n"))


def create_courier():
    new_courier = input("add new courier: ")
    new_number = input(" Enter New Number")
    courier["name"] = new_courier
    courier["number"] = new_number
    Courier_list.append(courier)
    print(Courier_list)


def update_courier():
    for i in enumerate(Courier_list):
        print(i)
    idx_courier = int(input("courier index that needs to be changed: "))
    update_courier = input("Put in updated courier")
    update_number = input("Put in updated number")
    Courier_list[idx_courier]["name"] = update_courier
    Courier_list[idx_courier]["number"] = update_number
    print(Courier_list)


def delete_courier():
    for i in enumerate(Courier_list):
        print(i)
    index_p = int(input(" choose index that needs to be deleted: "))
    del Courier_list[index_p]
    print(Courier_list)


# def close_save_product():
#     with open('products123.txt','w') as f:
#         for x in product_list:
#             f.write(f'{x}\n')

# def close_save_courier():
#     with open('people.txt','w') as f:
#         for x in Courier_list:
#             f.write(f'{x}\n')


def order_items_loop():
    exit = int(input("0,To Exit , 1 To Continue"))
    while exit != 0:
        for product in enumerate(product_list):
            print(product)
        item_basket = int(input("Use index to add products,"))
        items.append(item_basket)
        exit = int(input("0,To Exit , 1 To Continue"))
        return items


def create_order():
    customer_name = input("What is your name?: ")
    customer_address = input("what is your address?: ")
    customer_number = input("what is your number?:")
    for people in enumerate(Courier_list):
        print(people)
    couriername = input("Put in courier index: ")
    status = input("whats the status: ")
    items = order_items_loop()
    shopping_basket["customer_name: "] = customer_name
    shopping_basket["customer_address: "] = customer_address
    shopping_basket["customer_phone"] = customer_number
    shopping_basket["courier"] = couriername
    shopping_basket["status"] = status
    shopping_basket["items"] = items
    print(shopping_basket)
    orders_list.append(shopping_basket)


def load_order():
    for order in orders_list:
        print(orders)


def change_order_status():
    for order in enumerate(orders_list):
        print(order)
    change_status = int(
        input(" Choose the index of the order you would like to change")
    )
    update_status = input("what would you like to change Order Status too?")
    orders_list[change_status]["status"] = update_status
    print(orders_list)


def change_order():
    for i in enumerate(orders_list):
        print(i)
    Change_o = int(input("which order would you like to change"))
    print(orders_list[Change_o])
    new_name = input("What is the name?: ")
    new_address = input("what is the address?: ")
    new_status = input("what is the status")
    new_number = input("what is the number")
    for people in enumerate(Courier_list):
        print(people)
    new_courier = input("index of new courier")
    items = order_items_loop()
    Dictionary2 = {
        "Customer Name:": new_name,
        "Customer Address:": new_address,
        "Customer Number:": new_number,
        "courier": new_courier,
        "Status": new_status,
        "items": items,
    }
    orders_list[Change_o] = Dictionary2
    print(orders_list)


def delete_order():
    for order in enumerate(orders_list):
        print(order)
    deleted_order = int(input("Pick the index of the order you want to delete"))
    del orders_list[deleted_order]
    print(orders_list)


import csv


def load_products():
    with open("productss.csv", "r") as file:
        product_reader = csv.DictReader(file)
        for line in product_reader:
            product_list.append(line)


def load_orders():
    with open("order.csv", "r") as orderfile:
        order_reader = csv.DictReader(orderfile)
        for order in order_reader:
            orders_list.append(order)


def load_courier():
    with open("courier.csv", "r") as file:
        courier_reader = csv.DictReader(file)
        for courier in courier_reader:
            # print(courier)
            Courier_list.append(courier)


def save_products():
    with open("productss.csv", "w") as file:
        fields = ["name", "price"]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(product_list)


def save_orders():
    with open("order.csv", "w") as file:
        fields = [
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(orders_list)


def save_courier():
    with open("courier.csv", "w") as file:
        fields = ["name", "number"]
        headers = csv.DictWriter(file, fieldnames=fields)
        headers.writeheader()
        headers.writerows(Courier_list)
