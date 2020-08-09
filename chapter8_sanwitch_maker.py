#
#     Using inputMenu() for a bread type: wheat, white, or sourdough.
#     Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
#     Using inputYesNo() to ask if they want cheese.
#     If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
#     Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
#     Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
#
# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
# inputMenu(choices, prompt='_default', default=None, blank=False, timeout=None, limit=None, strip=None, allowRegexes=None, blockRegexes=None,
# applyFunc=None, postValidateApplyFunc=None, numbered=False, lettered=False, caseSensitive=False)

import pyinputplus as pyip

bread_type = ["wheat", "white", "sourdough"]
meat_type = ["chicken", "turkey", "ham", "tofu"]
cheese_type = ["cheddar", "Swiss", "mozzarella"]
souces_vegs_type = ["mayo", "mustard", "lettuce", "tomato"]
price =\
	{"wheat": 5,
	 "white": 6,
	 "sourdough": 4,
	 "chicken": 10,
	 "turkey": 15,
	 "ham": 20,
	 "tofu": 10,
	 "cheddar": 10,
	 "Swiss": 10,
	 "mozzarella": 6,
	 "mayo": 3,
	 "mustard": 3,
	 "lettuce": 5,
	 "tomato": 3
	 }


def sandwitch_calculator():
	print("Hello, what sandwich would you like to have today?\n")
	bread = pyip.inputMenu(bread_type, default="white", numbered=True)
	meat = pyip.inputMenu(meat_type, default="chicken", numbered=True)
	if pyip.inputYesNo(prompt="Would you like to have some cheese?\n") == "yes":
		cheese = pyip.inputMenu(cheese_type, default="cheddar", numbered=True)
	else:
		cheese = ""
	additions = []
	while True:
		if pyip.inputYesNo(prompt="Would you like to have some additions?\n") == "yes":
			additions.append(pyip.inputMenu(souces_vegs_type, default="mayo", numbered=True))
		else:
			break
	tmp = [bread, meat, cheese]
	tmp.extend(additions)
	return tmp


sum = 0
for item in (sandwitch_calculator()):
	print("item: ", item, "cost: ", price[item] / 10)
	sum += price[item]
print("Total cost is: ", sum / 10)