
from frdict import fruits
from fruit import Fruit

def search_fruit():
	#Search fruit
	name = input("Enter name: ")
	rate = int(input("Enter rate: "))
	found = False
	for i in fruits.values():
		if i["name"] == name and i["rate"] == rate: # find name 
			print(f"{i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")
			print("found")
			found = True
			break
		#else:
			#print("not found")
	if found == False :
		print("\tNot found")


def search_fruit_byname():
	#Search fruit
	
	name = input("Enter name: ")
	#rate = input("Enter rate: ")
	found = False
	for i in fruits.values():
		if i["name"] == name:
			print(f"{i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")
			print("found")
			found = True
			break
			
