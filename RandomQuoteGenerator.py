#import random module
import random

# quotes list
quotes = [
["I believe we are here on the planet Earth to live, grow up and do what we can to make this world a better place for all people to enjoy freedom.", "Rosa Parks" ],
 ["To love oneself is the beginning of a lifelong romance.", "Oscar Wilde"],
["No one can make you feel inferior without your consent.", "Eleanor Roosevelt"],
["To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.", "Ralph Waldo Emerson"],
 ["My mama always said, life is like a box of chocolates. You never know what you're gonna get.", "Forrest Gump"],
 ["To succeed in life, you need three things: a wishbone, a backbone, and a funny bone.", "Reba McEntire"],
 ["Many of life's failures are people who did not realize how close they were to success when they gave up.", "Thomas Edison"],
 ["The two most important days in your life are the day you are born and the day you find out why.", "Mark Twain"]
 ]

# variable to store quotes length - 1
quotesCount = len(quotes) -1

# generate random number based on quotes length
randomNumber = random.randint(0, quotesCount)

# get random quote and author based on randomNumber
randomQuote = quotes[randomNumber][0]
randomQuoteAuthor = quotes[randomNumber][1]

# print random quote
print("Your random quote for the day is the below:")
print(f"{randomQuote} -{randomQuoteAuthor}")
