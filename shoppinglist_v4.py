shopping_list = ['jam', 'butter']
new_item = '0'
del_item = "0"

def add_item():
	global new_item
	new_item = raw_input('enter your new item: ')
	new_item = new_item.lower()
	if new_item not in shopping_list:
		shopping_list.append(new_item)
		print "your shopping list is ", alphabetical_items()
	else:
		print "item already in list. "

def alphabetical_items():
	shopping_list.sort()
	return shopping_list	

def remove_item(): # won't break - need to fix
	global del_item
	del_item = raw_input('enter an item you want to remove from your list: ')
	del_item = del_item.lower() 
	if del_item not in shopping_list:
		shopping_list.remove(del_item)
		print "%s has been removed. Here is the updated list. " % (del_item), alphabetical_items()
	else:
		print 'item not on list'

def menu ():
	print "0 - Main Menu "
	print "1 - Show Current List "
	print "2 - Add an Item to your shopping list "
	print "3 - Remove an item from your shopping list "
	print "4 - Exit() "
	selection = int(raw_input("Choose a menu option. "))
	return selection

def main():
	selection = menu()
	
	while (True):	
		if selection == 0:	
			selection = menu() 
		elif selection == 1:
			print alphabetical_items()
			seletion = 0
		elif selection == 2:
			add_item()
			selection = 0
		elif selection == 3:
			remove_item()
			selection = 0
		elif selection == 4: 
			selection = 0


if __name__ == '__main__':
	main()


# add_item("Milk")
# add_item("yogurt")
# add_item("butter")
# add_item("jam")
# alphabetical_items()
# remove_item("pasta")