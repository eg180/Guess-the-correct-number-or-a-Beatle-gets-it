

import random



beatles = ["Ringo", "John", "Paul", "George"]




computernumber = random.randint(1,50) # this is the number the computer guesses


guesses = 4

player = input('Enter your name: ')

print('The year is 1969. For each wrong guess, a member of the Beatles gets it.')

myGuess = int(input('Think of a number between 1 and 50. What number am I thinking of, ' + player + '?: '))


while myGuess != computernumber and guesses > 1:
	
	if myGuess < computernumber:
		guesses = guesses - 1
		victim = random.choice(beatles)
		print(victim + ' is dead.')
		beatles.remove(victim)
		print('Your remaining siblings are', beatles)
		print('Guess higher than ', myGuess, '. You have ', guesses, 'chances remaining.')


		
	elif myGuess > computernumber:
		guesses = guesses - 1
		victim = random.choice(beatles)
		print(victim + ' is dead.')
		beatles.remove(victim)
		print('Your remaining siblings are', beatles)
		print('Guess lower than', myGuess, '. You have ', guesses, 'chances remaining.')
	
	myGuess = int(input('Guess again: '))


if myGuess == computernumber:
	print('YOU WIN, ' + player + '! You won with', (4 - guesses), 'guesses!')
else:
	print('YOU LOSE! The answer was', computernumber)
	print("Not a good way to rewrite history.")




