DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

# fare_price = price it costs to travel btw 2 bart stations
# card_value = current value of clipper card using load_card function
# travel function sould compare fare and card parameters and print out if there is enough $
def load_card(bill1,bill5, bill10, bill20):
	num1 = bill1*1
	num5 = bill5*5
	num10 = bill10*10
	num20 = bill20*20
	return num1+num5+num10+num20

clipper_card1 = load_card(2,0,1,0)
clipper_card2 = load_card (1,0,0,0)

def travel_to_destination(fare_price, card_value):
	if (card_value >= fare_price):
		print "Welcome aboard, enjoy your trip!"
	else:
		print "You need more money!"

print travel_to_destination(FRUITVALE_TO_UNION_CITY,clipper_card1)
print travel_to_destination (FRUITVALE_TO_UNION_CITY, clipper_card2)

