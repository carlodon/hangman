import random

def hangman(word):
	wrong = 0
	stages = ["",
			  "__________		",
			  "|	  |		",
			  "|	  |		",
			  "|	  0		",
			  "|	/ | \	",
			  "|	 / \ 	",
			  "|			"
			 ]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome in execution!")
	while wrong < len(stages) - 1:
		print("\n")
		msg = "Input letter: "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0: e]))
		if "__" not in board:
			print("You win! Было загадано слово: {}.".format(word))
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0: wrong]))
		print("You lose! Было загадано слово: {}.".format(word))


words = ['путешествие', 'macbook', 'кот', 'собака']
hangman(random.choice(words))
