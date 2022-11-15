product_list = []
Courier_list = []

def products_order():
    with open('products123.txt', 'r') as f:
        for line in f.readlines():
            product_list.append(line.strip("\n"))
            print()


def create_product():
    new_product = input("add new product: ")
    product_list.append(new_product)
    print(product_list)

def update_product():
     for i in enumerate(product_list):
            print(i)
            idx_product = int(input("Product index that needs to be changed: "))
            upd_product = input("Put in updated product")
            product_list[idx_product] = upd_product
            print(product_list)
def delete_product():
    for i in enumerate(product_list):
        print(i)
    index_p = int(input( " choose index that needs to be deleted: "))
    del product_list[index_p]
    print(product_list)



def courier_order():
    with open('people.txt', 'r') as f:
        for line in f.readlines():
            Courier_list.append(line.strip("\n"))
        


def create_courier():
    new_product = input("add new courier: ")
    Courier_list.append(new_product)
    print(Courier_list)

def update_courier():
     for i in enumerate(Courier_list):
            print(i)
            idx_product = int(input("courier index that needs to be changed: "))
            upd_product = input("Put in updated courier")
            Courier_list[idx_product] = upd_product
            print(Courier_list)
def delete_courier():
    for i in enumerate(Courier_list):
        print(i)
    index_p = int(input( " choose index that needs to be deleted: "))
    del Courier_list[index_p]
    print(Courier_list)
    
def close_save_product():
    with open('products123.txt','w') as f:
        for x in product_list:
            f.write(f'{x}\n') 

def close_save_people():
    with open('people.txt','w') as f:
        for x in Courier_list:
            f.write(f'{x}\n') 



