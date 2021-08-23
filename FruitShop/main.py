from fruit import Fruit
import change as c
import search as s
import fruitshop as f

def main_menu():
	print("1. Add fruit")
	print("2. Add cart details")
	print("3. Delete fruit")
	print("4. Display all fruit")
	print("5. Display cart")
	print("6. Search fruits")
	print("7. change fruit name and rate")
	print("8. exit")
while True:
	main_menu()
	ch = int(input("Enter your choice: "))
	if ch == 1:
		#add fruit
		f.add_fruit()
	elif ch == 2:
		#Add to cart
		#add_cart()
		f.add_to_cart()
	elif ch == 3:
		#Delete fruit by serial_no
		#delete_fruits()
		f.delete_fruitbyName()
	elif ch == 4:
		#Display all fruit
		f.display_allfruit()
	elif ch == 5:
		#Display cart fruits
		f.display_cart()
	elif ch == 6:
		#Search fruit
		s.search_fruit()

	elif ch== 7:
		#Change a fruit name and rate in the list
		c.change_fruit()
	elif ch == 8:
		#Exit
		break;
	else:
		print("Invalid Choice")
