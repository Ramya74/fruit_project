from frdict import fruits
from fruit import Fruit
#fruits = {} #Empty dictionary
cartitems = []


def add_fruit():
	#Add fruit
	serial_no = input("Enter serial No: ")
	name = input("Enter name: ")
	rate = int(input("Enter rate: "))
	imp_from = input("Enter place imported from: ")
	imp_date = input("Enter date when it is imported: ")
	buy_price = input("Enter buy price: ")
	temp ={
		"name":name,
		"rate":rate,
		"imp_from":imp_from,
		"imp_date":imp_date,
		"buy_price":buy_price
		}
	fruits[serial_no] = temp

def add_cart():
	#Add to cart
	#serial_no = int(input("\tEnter serial no."))
	for serial in fruits.keys():
		print(f"press {serial} for add to cart")
	cartitems.append(fruits[input('enter serial_no to add on cart : ')])
	
	print(' added Fruit in the cart ')
	#for i in fruits.keys():
	#if serial_no in fruits.keys():
	#	cartitems[serial_no] = []
				
def delete_fruit():
	#Delete fruit by serial_no
	serial_no = input("Enter serial no: ")
	if serial_no not in fruits.keys():
		print("\tWrong serial no")
	else:
		del fruits[serial_no]

def delete_fruitbyName():
	#delete fruit by name
	name = input("Enter fruit name: ")
	serial_no = input("Enter serial no: ")
	flag = False
	if serial_no in fruits.keys():
		for i in fruits.values():
			if i['name'] == name:
				flag = True
				#del fruits[serial_no]
	else:	
		print("name not found")
	if flag == True:
		del fruits[serial_no]
def display_allfruit():
	#Display all fruit
	#for serial,fruit in fruits.items():
	#	print(f"{serial} | {fruit['name']}")
	for serial,fruit in fruits.items():
		print(f"\t {fruit['name']} | {fruit['rate']} | {fruit['imp_from']} | {fruit['imp_date']}| {fruit['buy_price']}")
		
def display_cart():
	#Display cart fruits
	print(cartitems)
	

def cart_menu():
	print("\t 1. Add to Cart")
	print("\t 2. Display Cart")
	print("\t 3. Delete From cart")
	print("\t 4. Display Bill")
	print("\t 5. Exit")

def addto_cart():
	i = int(input("\t\tEnter the fruitid to add"))
	if i in fruits.keys():
		cartitems.append(i)
	else:
		print("\tInvalid ID")

def display_cartitems():
	#Display cart fruits
	print(cartitems)
	
def delete_from_cart():
	#display_cartitems()
	serial_no = int(input("\t\tEnter the serialno to delete from cart: "))
	for serial in fruits.keys():
		print(f"press {serial} for delete from cart")
	cartitems.remove(fruits[input('enter serial_no to delete from cart : ')])
	
	print(' delete Fruit in the cart ')
	
def print_bill():
	serial_no = int(input("\t\tEnter the serialno for bill: "))
	for serial in cartitems:
		print(cartitems)
		
		#print(f"{cartitems[-1]}")
			

def add_to_cart():
	while True:		
		cart_menu()
		choice = int(input("\tEnter the choice: "))
		if choice == 1:
			add_cart()
		elif choice == 2:
			display_cart()
		elif choice == 3:
			delete_from_cart()
		elif choice == 4:
			print_bill()
		elif choice == 5:
			break
		#else:
			#print("\tInvalid Choice")


