# Poker-dice
It's a program named poker_dice.py that simulates the roll of 5 dice, at most three times, as described
at http://en.wikipedia.org/wiki/Poker_dice as well as a given number of rolls of the 5 dice to evaluate the probabilities of the various hands.  
• What is input from the keyboard is displayed in red; what is black is output by the program.  
• The hands are displayed in the order Ace, King, Queen, Jack, 10 and 9.  
• All dice can be kept by inputting either all, or All, or the current hand in any order.  
• No die is kept by inputting nothing.  
• We have control over what is randomly generated by using the seed() function at the prompt.  
• To roll a die, we use randint(0, 5) with 0, 1, 2, 3, 4 and 5 corresponding to Ace, King, Queen, Jack, 10 and 9, respectively.  
:  
$ python3  
...  
>>> from random import seed  
>>> import poker_dice  
>>> seed(0)  
>>> poker_dice.play()  
The roll is: Ace Queen Jack Jack 10  
It is a One pair  
Which dice do you want to keep for the second roll? all  
Ok, done.  
>>> poker_dice.play()  
The roll is: Queen Queen Jack Jack Jack  
It is a Full house  
Which dice do you want to keep for the second roll? All  
Ok, done.  
>>> poker_dice.play()  
The roll is: King King Queen 10 10  
It is a Two pair  
Which dice do you want to keep for the second roll? King 10 Queen King 10  
Ok, done.  
>>> poker_dice.play()  
The roll is: Ace King Queen 10 10  
It is a One pair  
Which dice do you want to keep for the second roll? 10 11  
That is not possible, try again!  
Which dice do you want to keep for the second roll? ace  
That is not possible, try again!  
Which dice do you want to keep for the second roll? 10 10  
The roll is: King 10 10 10 9  
It is a Three of a kind  
Which dice do you want to keep for the third roll? all  
Ok, done.  
>>> poker_dice.play()  
The roll is: Ace Ace Queen 9 9  
It is a Two pair  
Which dice do you want to keep for the second roll? Ace  
The roll is: Ace Ace Queen Jack 10  
It is a One pair  
Which dice do you want to keep for the third roll? Ace  
The roll is: Ace Queen Queen Jack 10  
It is a One pair  
>>> seed(2)  
>>> poker_dice.play()  
The roll is: Ace Ace Ace King Queen  
It is a Three of a kind  
Which dice do you want to keep for the second roll? Ace Ace Ace  
The roll is: Ace Ace Ace 9 9  
It is a Full house  
Which dice do you want to keep for the third roll? all  
Ok, done.  
>>> poker_dice.play()  
The roll is: King Queen Queen 10 10  
It is a Two pair  
Which dice do you want to keep for the second roll?  
The roll is: Ace King Jack 10 9  
It is a Bust  
Which dice do you want to keep for the third roll?  
The roll is: Queen Jack 10 9 9  
It is a One pair  
>>> seed(10)  
>>> poker_dice.play()  
The roll is: Ace Jack Jack 10 10  
It is a Two pair  
Which dice do you want to keep for the second roll? Jack 10 Jack 10  
The roll is: Ace Jack Jack 10 10  
It is a Two pair  
Which dice do you want to keep for the third roll? Jack 10 Jack 10  
The roll is: King Jack Jack 10 10  
It is a Two pair  
>>> seed(20)  
>>> poker_dice.play()  
The roll is: King Queen 9 9 9  
It is a Three of a kind  
Which dice do you want to keep for the second roll? 9 King 9 9  
The roll is: King 9 9 9 9  
It is a Four of a kind  
Which dice do you want to keep for the third roll? 9 9 9 9  
The roll is: Ace 9 9 9 9  
It is a Four of a kind  
>>> seed(0)  
>>> poker_dice.simulate(10)  
Five of a kind : 0.00%  
Four of a kind : 0.00%  
Full house : 10.00%  
Straight : 0.00%  
Three of a kind: 0.00%  
Two pair : 20.00%  
One pair : 60.00%  
>>> poker_dice.simulate(100)  
Five of a kind : 0.00%  
Four of a kind : 0.00%  
Full house : 3.00%  
Straight : 4.00%  
Three of a kind: 14.00%  
Two pair : 28.00%  
One pair : 45.00%  
>>> poker_dice.simulate(1000)  
Five of a kind : 0.10%  
Four of a kind : 2.50%  
Full house : 3.80%  
Straight : 3.40%  
Three of a kind: 17.20%  
Two pair : 20.60%  
One pair : 46.30%  
>>> poker_dice.simulate(10000)  
Five of a kind : 0.08%  
Four of a kind : 1.99%  
Full house : 3.93%  
Straight : 3.33%  
Three of a kind: 14.88%  
Two pair : 23.02%  
One pair : 46.58%  
>>> poker_dice.simulate(100000)  
Five of a kind : 0.08%  
Four of a kind : 1.94%  
Full house : 3.85%  
Straight : 3.17%  
Three of a kind: 15.47%  
Two pair : 23.02%  
One pair : 46.31%  
