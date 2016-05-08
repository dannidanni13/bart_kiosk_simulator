original_bill_amount = int(raw_input("How much is the bill not including tip? ")) #this prints the first 
tip_percentage = .18
num_people_at_dinner = 1
tip_amount = tip_percentage * original_bill_amount

def calculate_tip():# prompts for: How much do you want to leave for the tip? and 18% question
	what_to_tip = raw_input("Is 18 okay? Y or N? ")
	if what_to_tip == "N":
		global tip_percentage
		tip_percentage = float(raw_input("How much do you want to leave for the tip? "))
	return tip_percentage * original_bill_amount

def total_bill ():
	global original_bill_amount
	original_bill_amount = original_bill_amount + tip_amount
	return original_bill_amount

def prompt_user(): #this prompts how many diners/did you dine alone
	Dine_alone = raw_input("Did you dine alone ? Y or N? ") 
	if Dine_alone == "N":
		global num_people_at_dinner
		num_people_at_dinner = int(raw_input("How many people were at dinner? ")) 
		# above should only prompt when N -
	return num_people_at_dinner

print prompt_user()

def main(): #not i'm doing this right. it kind of works but i don't think it is right
	if num_people_at_dinner < 1:
		print "the amount per person is ", original_bill_amount / num_people_at_dinner
	print "original bill amount is ", original_bill_amount
	print "your tip amount is ", calculate_tip()
	print "your total bill is ", total_bill()

if __name__ == '__main__':
   main()

# Hannah - I've made comments on where I'm stuck.
# I'm not sure what the raw input values are printing after I enter them when I'm returning not printing in the function
# I know the main is not right but I'm not sure what to do
# Also, when i enter N for dine_alone and a int for the number of # of people, and a different value for tip the math doesn't work
# I think that's due to the order

