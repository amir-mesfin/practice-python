questions = (
    "how many element are in the periodic table? : ",
    "which animal lays the largest eggs? :",
    "what is the most abundant gas in the earth's atmosphere? :",
    "how many bones are n the human body? :",
    "which plant in the solar system is hottest? :",
    
    # NEW QUESTIONS
    "What is the largest planet in our solar system? :",
    "Who painted the Mona Lisa? :",
    "What is the capital city of Japan? :",
    "Which ocean is the largest? :",
    "What is the hardest natural substance? :",
    "How many continents are there on Earth? :",
    "Which country invented paper? :",
    "What is the boiling point of water at sea level? :",
    "Which metal is liquid at room temperature? :",
    "Which part of the plant conducts photosynthesis? :"
)

options = (
    ("A, 116", "B, 117", "C, 118", "D, 119"), 
    ("A, whale", "B, crocodile", "C, Elephant", "D, Ostrich"),
    ("A, Nitrogen", "B, oxygen", "C, carbon", "D, hydrogen"),
    ("A, 206", "B, 207", "C, 208", "D, 209"),
    ("A, Mercury", "B, venus", "C, earth", "D, mars"),

    # NEW OPTIONS
    ("A, Earth", "B, Jupiter", "C, Saturn", "D, Neptune"),
    ("A, Vincent Van Gogh", "B, Picasso", "C, Leonardo da Vinci", "D, Michelangelo"),
    ("A, Tokyo", "B, Osaka", "C, Kyoto", "D, Seoul"),
    ("A, Indian", "B, Atlantic", "C, Pacific", "D, Arctic"),
    ("A, Gold", "B, Iron", "C, Diamond", "D, Silver"),
    ("A, 5", "B, 6", "C, 7", "D, 8"),
    ("A, China", "B, Egypt", "C, India", "D, Greece"),
    ("A, 50°C", "B, 100°C", "C, 150°C", "D, 200°C"),
    ("A, Mercury", "B, Iron", "C, Silver", "D, Copper"),
    ("A, Roots", "B, Stem", "C, Flowers", "D, Leaves")
)


answer = (
    "C", "D", "A", "A", "B",

    # NEW ANSWERS
    "B",
    "C",
    "A",
    "C",
    "C",
    "C",
    "A",
    "B",
    "A",
    "D"
)


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

