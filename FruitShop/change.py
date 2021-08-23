from frdict import fruits
from fruit import Fruit

def change_fruit_fun():
	#Change a fruit name and rate in the list
	serial_no = input("\tEnter serial no.")
	if serial_no not in fruits.keys():
		print("\tWrong serial no")
	else:
		fruits[serial_no]['name'] = input("\tEnter new name: ")
		fruits[serial_no]['rate'] = input("\tEnter new rate: ")
		
def change_fruit():
		#Change a fruit detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change rate ")
	print("\t Enter 3 for change imp_from ")
	print("\t Enter 4 for change imp_date ")
	print("\t Enter 5 for change buy_price ")

	choice = int(input("\tEnter the choice which u want to change: "))
	serial_no = input("\tEnter serial no: ")
	if choice == 1:
		fruits[serial_no]['name'] = input("\tEnter new name: ")
	elif choice == 2:
		fruits[serial_no]['rate'] = input("\tEnter new rate: ")
	elif choice == 3:
		fruits[serial_no]['imp_from'] = input("\tEnter new imp_from: ")
	elif choice == 4:
		fruits[serial_no]['imp_date'] = input("\tEnter new imp_date: ")
	elif choice == 4:
		fruits[serial_no]['buy_price'] = input("\tEnter new buy_price: ")

