# choose a random element from a list
from random import seed
from random import choice
# seed random number generator
seed(1)
# prepare a sequence
sequence = ["ali","bahram","sara","mahdi"]
print(sequence)
# make choices from the sequence
for i in range(1):
	selection = choice(sequence)
	print(selection)