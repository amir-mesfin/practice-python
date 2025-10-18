questions =("how many element are in the periodic table? : ",
            "which animal lays the largest eggs? :",
            "what is the most abundant gas in the earth's atmosphere? :",
            "how many bones are n the human body? :",
            "which plant in the solar system is hottest? :")

options = (("A, 116", "B, 117", "C, 118", "D, 119"), 
           ("A, whale", "B, crocodile", "C, Elephant", "D, Ostrich"),
           ("A, Nitrogen", "B, oxygen", "C, carbon", "D, hydrogen"),
           ("A, 206", "B, 207", "C, 208", "D, 209"),
           ("A, Mercury", "B, venus", "C, earth", "D, mars")
           )

answer = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0


for  question in questions:
  print("-----------------------------------------")
  print(f"{question_num+1}__{question}")
  
  for option in options[question_num]:
    print(option)
  
  guess = input("Enter (A, B, C, D) : ").upper()
  guesses.append(guess)
  if guess == answer[question_num] :
    score += 1
    print("CORRECT")
  else :
    print("INCORRECT")
    print(f"{answer[question_num]} is  the correct answer ")
  
  question_num +=1


print()
print("******************************************")  
print("                   RESULT                 ")  
print("******************************************") 

print("answer : ", end=" ") 

for answer in answer:
  print(answer, end=" ")
  
print()

print("Guess  : ",end = " ")

for guess in guesses :
  print(guess, end = " ")
  
print()

score = int((score / len(questions)) * 100 )

print(f"    Your score is : {score}% ")

print("******************************************") 

