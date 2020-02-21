#McDuck airline
#Buy function----------------------------------------------------------------
def buy():
	buy_condition = True
	while buy_condition == True:
		print("Choose your destiny")
		print("1) Munich")
		print("2) London")
		print("3) Santiasco")
                print("4) Quit")
		buy_option = int(input())
		buy_condition = False
		if (buy_option == 1):
			b = buy_sub("Munich")
			price = 992 + int(b)
			print("Your ticket is:")
			print("Ticket number = 2356")
			print("Destiny: Munich")
			print("Road Trip Ticket Cost: $992")
			print("Additional service: ")
			if (b == 15):
				print("Additional baggage Cost: $15")
			elif (b == 20):
				print("Special food Cost: $20")
			elif (b == 35):
				print("Additional baggage Cost: $15")
				print("Special food Cost: $20")
			else:
				print("No service")
			print("Total cost: $ {}".format(price))
			return True
		elif (buy_option == 2):
			b = buy_sub("London")
			price = 1023 + int(b)
			print("Your ticket is:")
			print("Ticket number = 4040")
			print("Destiny: London")
			print("Road Trip Ticket Cost: $1023")
			print("Additional service: ")
			if (b == 15):
				print("Additional baggage Cost: $15")
			elif (b == 20):
				print("Special food Cost: $20")
			elif (b == 35):
				print("Additional baggage Cost: $15")
				print("Special food Cost: $20")
			else:
				print("No service")
			print("Total cost: $ {}".format(price))
			return True
		elif (buy_option == 3):
			b = buy_sub("Santiasco")
			price = 210 + int(buy_sub)
			print("Your ticket is:")
			print("Ticket number = 9232")
			print("Destiny: Munich")
			print("Road Trip Ticket Cost: $992")
			print("Additional service: ")
			if (b == 15):
				print("Additional baggage Cost: $15")
			elif (b == 20):
				print("Special food Cost: $20")
			elif (b == 35):
				print("Additional baggage Cost: $15")
				print("Special food Cost: $20")
			else:
				print("No service")
			print("Total cost: $ {}".format(price))
			return True
		elif (buy_option == 4):
			print("Returning to the main menu...")
			return True
		else:
			print("Please choose one of the destinies")
			buy_condition = True

#End of buy function---------------------------------------------------------

#Buy_sub function------------------------------------------------------------
def buy_sub(x):
	buy_sub_condition = True
	service_condition = True
	print("You've chosen {}".format(x))
	while buy_sub_condition == True:
		print("Would you like to add an especial service?")
		while service_condition == True:
			print("1) Add baggage $15")
			print("2) Add special food $20")
			print("3) Both of them	$35")
			print("4) Nothing")
			sub_option = int(input())
			service_condition = False
		if (sub_option == 1):
			return 15
		elif (sub_option == 2):
			return 20
		elif (sub_option == 3):
			return 35
		elif (sub_option == 4):
			return 0
		else:
			print("Please choose one of the current choices")
			service_condition = True
#End of buy_sub function-----------------------------------------------------

#Check-in Function-----------------------------------------------------------
def check_in():
	condition2 = True
	ticket_list = []
	while condition2 == True:
		print("Put your ticket number please:")
		code = input() #this one is a string
		condition2 = False
		if len(code)==4:
			for x in code:
				ticket_list.append(x)
		else:
			print("Invalid code. Syntax Errror")
			condition2 = True
	#1 Step: sum of digits
	num1 = int(ticket_list[0])
	num2 = int(ticket_list[1])
	num3 = int(ticket_list[2])
	num4 = int(ticket_list[3])

	sum = num1+num2+num3+num4

	if (sum%2 == 0):
		if not(sum%5 ==0):
			print("Your ticket is correct!")
			print("Returning to the guest menu...")
		else:
			print("Your ticket number is already registered")
			print("Returning to the guest menu...")

	else:
		print("Your ticket number is invalid")
		print("Returning to the guest menu...")

	return True

	#2 Step: validate again by the number 5
		# if sum of digits is a multiple of 5 then is bad
		# if sum of digits isn't a multiple of 5 then is good
#End of Check_in --------------------------------------------------------------
condition1 = True
#Menu
print("Welcome to McDuck Airlines")
while condition1 == True:
	print("1) Sign as a Guess")
	print("2) Check-in")
	sub_condition1 = int(input())
	condition1 = False
	if (sub_condition1 == 1):
		menu_guest = True
		menu_condition = True
	elif (sub_condition1 == 2):
		condition1 = check_in()
		menu_guest = False
	else:
		condition1 == True
#Menu for guess
	if menu_guest == True:
		print("Welcome to the Guest Menu")
		while menu_condition == True:
			print("Which operation would you like to do?")
			print("1) See flight prices")
			print("2) Buy ticket")
			print("3) Check-in")
			print("4) Quit")
			menu_option = int(input())
			menu_condition = False
			if (menu_option == 1):
				print("Flights available")
				print("--------------------")
				print("1) Munich, Germany | $992 round trip ticket")
				print("2) London, England | $1023 round trip ticket")
				print("3) Santiasco, Chile| $210 round trip ticket")
				print("Returning to the main menu...")
			elif (menu_option == 2):
				menu_condition=buy()
			elif (menu_option == 3):
				menu_condition=check_in()
			elif (menu_option == 4):
				menu_guest == False
	elif menu_guest == False:
		condition1 = True
