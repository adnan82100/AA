import menu3
def view_product():
    with open('products123.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def change_product():
    with open('products123.txt', 'r+' ) as f:
        lines = f.readlines()
        for line in enumerate(lines):
            print(line)
            # print(str(line[0]) + '. ' + str(line[1].strip()))

    with open('products123.txt','w') as f:
        product_index = int(input('Product index that you would like to change: '))
        new_product = input('what would you like to change it to: ')
        lines[product_index] = new_product
        f.writelines(lines)
def add_product():
    with open('products123.txt', 'r+') as f:
        lines = f.readlines()
        print(lines)
        products = input("add product: ")
        f.write(products + "\n")

def delete_product():
    with open('products.txt', 'r+') as f:
        pass

change_product()


# .strip("\n")

# f = open('products.txt', 'r')

# print(f.name)

# f.close()