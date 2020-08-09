# Write Your Own Multiplication Quiz
#
# To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. This program will prompt the user
# with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:
#
#     If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
#     The user gets three tries to enter the correct answer before the program moves on to the next question.
#     Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.


def multi_quiz():
	import random
	import pyinputplus
	import time
	score = 0
	for turn in range(10):
		num1 = random.randint(0, 10)
		num2 = random.randint(0, 10)
		print("Turn ", turn, "\n")
		try:
			choice = pyinputplus.inputStr(prompt="%s * %s = ?" % (num1, num2), blockRegexes=[('.*', 'Incorrect!')], allowRegexes=[r"^%s$" % (num1 * num2)], limit=3, timeout=8)
		except pyinputplus.TimeoutException:
			print("Time is up!")
		except pyinputplus.RetryLimitException:
			print("Too many wrong answers!")
		else:
			print("Good job !")
			score += 1
			print(f"Score is {score}")
			time.sleep(1)

multi_quiz()