'''2- Problem Statement :Make a Grocery List for supermarket shopping withname,price and quantity; if the list already contains anitemthen only update the price and quantity it shouldnotappend the item name again. Ask the user his/her budgetinitially and minus the budget after adding a newitem inthe list. If budgets go zero/0 then no more itemscouldbe bought and if some money left and users add itemsgreater than budget left then inform “over price”or anyother message. After the list is made any money leftin
the budget it should show an item within the budget fromthe list made.VALIDATION is a must'''


while True: 
	try:

		budget = float(input("Enter Your budget : ")) 
		
	except ValueError: 
		print("PRINT NUMBER AS INPUT") 
		continue
	else: 
		break
product_dic={}
while True: 
	try: 
		choice = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 

	except ValueError: 
		print("\nERROR: Choose only from 1 or 2 ") 
		continue
	else:
		if choice == 1 and budget > 0:
			product_name = input("Enter product : ")
			product_quantity = input("Enter quantity : ")
			product_price = float(input("Enter Price: "))
			if product_price > budget:

				print("\nover price")
				continue

			else:

				if product_name in product_dic:

					budget += product_dic[product_name][1]
					budget -= product_price
					product_dic[product_name][1] = product_price
					product_dic[product_name][0] = product_quantity



				else:
					product_dic[product_name] = list()
					product_dic[product_name].append(product_quantity)
					product_dic[product_name].append(product_price)
					budget -= product_price

				print("\nAmount left", budget)

		elif budget <= 0 and choice!=2:
			print("\nNO BUDGET")
		else:
			break
	

print("\nAmount left : Rs.", budget) 

for i in product_dic:
    if budget == product_dic[i][1]: 
    	
    	print("\nAmount left can buy you a", i)

print("\n\n\nGROCERY LIST") 

for i in product_dic: 
	print(i, product_dic[i][0], product_dic[i][1])
