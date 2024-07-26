print("Welcome to my computer quiz!")

playing = input("Would you like to play? (Yes/No) ")

score = 0

if playing.lower() != "yes":
  quit()

print("Okay great, let's play!")

#first question
answer = input("1) What does CPU stand for? (2 Points) ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 2

else:
  print("Incorrect! The correct answer is central processing unit")

#second question
answer = input("2) When was the first computer invented? (1 Point) ")
if answer.lower() == "1833":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is 1833.")

#thrid question
answer = input("3) What is the most popular computer language? (1 Point) ")
if answer.lower() == "javascript":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is javascript.")

#fourth question
answer = input("4) Are computers smart? Yes or No? (1 Point) ")
if answer.lower() == "yes":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is yes.")

#fift question
answer = input(
    "5) Is there a shift button on a computer? Yes or No? (1 Point) ")
if answer.lower() == "yes":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is yes.")

#sixth question
answer = input("6) What does RAM stand for? (2 Points) ")
if answer.lower() == "random access memory":
  print("Correct!")
  score += 2

else:
  print("Incorrect! The correct answer is random access memory. (1 Point) ")

#seventh question
answer = input("7) Can computers walk? Yes or No? (1 Point) ")
if answer.lower() == "no":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is no.")

#eighth question
answer = input("8) Can computers get viruses? Yes or No (1 Point) ")
if answer.lower() == "yes":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is yes.")

#ninth question
answer = input("9) Are computers used all around the world? (1 Point) ")
if answer.lower() == "yes":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is yes.")

#tenth question
answer = input("10) This quiz is great! True or False? (1 Point) ")
if answer.lower() == "true":
  print("Correct!")
  score += 1

else:
  print("Incorrect! The correct answer is true.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 12) * 100) + "%.")
