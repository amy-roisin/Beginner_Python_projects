# Give the 8-Ball a name and a question

name = "Amy"
question = ""


#import and code for randomisation of numbers

import random

random_number = random.randint(1,16)


#outputs

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Absolutely not."
elif random_number == 11:
  answer = "The odds are in your favour."
elif random_number == 12:
  answer = "It is a possibility."
elif random_number == 13:
  answer = "It's your lucky day."
elif random_number == 14:
  answer = "Possibility within the next year"
elif random_number == 15:
  answer = "If I told you, I'd have to kill you."
elif random_number == 16:
  answer = "I can't tell you, they're listening."
else:
  answer = "Error"


# Conditions

if len(question) == 0:
  print("If I were to provide a fortune without a question, the very fabric of reality would be at risk!")
elif name == "":
  print(question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks " + question)
  print("Magic 8-Ball's answer: " + answer)