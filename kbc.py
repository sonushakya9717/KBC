z=0
while True:
	question_list = [
		"How many continents are there?",

		"What is the capital of India?",

		"NG mei kaun se course padhaya jaata hai?"
	]
	options_list = [

		["1.Four", "2.Nine", "3.Seven", "4.Eight"],

		["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],

		["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
	]
	solution_list = [3, 4, 1]
	a=0
	x=0
	l=[
		["3.Seven", "4.Eight"],
		["3.Chennai", "4.Delhi" ],
		["1.Software Engineering", "2.Counseling"]
	]
	for i in question_list:
		print (question_list[a],"\n")
		for j in options_list[a]:
			print (j,"\n")
		if x==0:
			k=int(input("Enter 1 for lifeline: "))
			if k==1:
				print (l[a])
				x+=1
		b=int(input("Enter your answer: "))
		if b==solution_list[a]:
			print("\nyour answer is correct")
		else:
			print ("\nyour answer is wrong")
			print ("\nyou are out of the game")
			break
		a+=1
	if z==0:
		user=input("\nDo you want to try again?  ")

		if user=="no":
			break
		else:
			z+=1
	else:
		break