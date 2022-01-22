#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")
#name = input("Enter Your Name: ")
#age= input("Enter Your Age: ")
#print("Hello " + name + "! You are " + age + " years old! ")
#num1 = input("Enter a number : ")
#num2 = input("Enter another number : ")
#result= float(num1) + float(num2)
#print(result)
#color = input("Enter a color: ")
#plural_noun= input("Enter a plural noun: ")
#celebrity = input("Enter a name of celebrity: ")
#print("Roses are "+ color)
#print("Violets are " + plural_noun)
#print("I love " + celebrity)
#Lists
#friends = ["Soumya", "Oscar", "Leena", "Richard", "Toby"]
#friends[1]= "Nick"
#print(friends[1:3])
#List Functions
#lucky_numbers= [1,2,3,4,5,6,7]
#friends = ["Soumya", "Oscar", "Soumya", "Leena", "Richard", "Toby"]
#friends.extend(lucky_numbers)
#friends.append("Wharton")
#friends.insert(1,"Dextro")
#friends.remove("Leena")
#friends.clear()
#friends.pop()
#print(friends.index("Toby"))
#print(friends.count("Soumya"))
#friends.sort()
#print(friends)
#lucky_numbers.reverse()
#print(lucky_numbers)
#friends2 = friends.copy()
#print(friends2)
#TUPLES, which is immutable unlike Lists
#coordinates = (4,5)
#print(coordinates[0])
#Functions
#def say_hi(name , age):
 #   print("Hello " + name + "! You are " + age + " years old")
#print("Top")
#say_hi("Mike", "35")
#print("Bottom")
#Return Statement
#def cube(num):
#    return num*num*num

#result= cube(4)
#print(result)
#is_male = False
#is_tall = False
#if is_male and is_tall:
 #   print("You are a male or tall or both")
#elif is_male and not(is_tall):
 #   print("You are a short male")
#elif not(is_male) and is_tall:
 #   print("You are not male but are tall")
#else:
 #   print("You are neither male nor tall")
#If statements and comparisons
#def max_num(num1,num2,num3):
 #   if num1>=num2 and num1>=num3:
  #      return num1
   # elif num2>=num1 and num2>=num3:
    #    return num2
    #else:
     #   return num3

#print(max_num(30,4,5))
#Building a better calculator:
#num1= float(input("Enter the first number: "))
#op= input("Enter the operator: ")
#num2=float(input("Enter the second number: "))
#if op== "+":
 #   print(num1+num2)
#elif op== "-":
 #   print(num1-num2)
#elif op== "*":
 #   print(num1*num2)
#elif op== "/":
 #   print(num1/num2)
#else:
 #   print("Invalid operator")
#Dictionaries:
#monthlyConversions = {
 #   "Jan": "January",
  #  "Feb": "February"
#}

#print(monthlyConversions.get("Feb", "Not a valid key"))
#While Loops
#i=1
#while i<=10:
 #   print(i)
  #  i += 1

#print("Done with loop")
#Building a Guessing Game:
#secret_word = "giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
 #   if guess_count < guess_limit :
  #      guess = input("Enter guess: ")
   #     guess_count += 1
    #else:
     #   out_of_guesses = True
    #if out_of_guesses:

     #   print("Out of guesses, You lose!")
    #else:
     #  print("You win! ")
     #For Loop
#for letter in "Giraffe Academy":
 #    print(letter)
friends= ["Jim", "Karen", "Oliver"]
#for name in friends:
 #   print(friends)
#for index in range(len(friends)):
 #   print(friends[index])
#for index in range(5):
 #   if index ==0:
  #      print("first Iteration")
   # else:
    #    print("Not First")
    #Exponent Fnction
#print(2**3)
#def raise_to_power(base_num, pow_num):
 #   result = 1
  #  for index in range(pow_num):
   #     result = result * base_num
    #return result

#print(raise_to_power(3,4))
#2D lists and Nested Loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#print(number_grid[2][0])
#for row in number_grid:
 #   for col in row:
  #      print(col)
   #Build a Translator
#def translate(phrase):
 #   translation = ""
  #  for letter in phrase:
   #     if letter.lower() in "aeiou":
    #        if letter.isupper():
     #           translation = translation + "G"
      #  else:
      #      translation = translation + letter
#    return translation

#print(translate(input("Enter a phrase: ")))
#COMMENTS
#print("Comments are fun")
# This program is cool
'''sdssjggdsajg
scbdcsaj
shfdj'''
#Try Except
'''try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)'''
#Reading Files
'''employee_file = open("index.html", "w")
#print(employee_file.readable())
for employee in employee_file.readlines():
    print(employee)''''''
    #print(employee_file.readline()[1])
#employee_file.close()
#Writing To Files:
#employee_file.write("<p>This is HTML</p>")
#employee_file.close()'''
#Modules and Pip
#Through this we can get the access of other python files, through the import function
#Classes and Objects
#from student import Student

#student1 = Student("Pam", "Business",4.1,True)
#student2 = Student("Jim", "Business",3.1,False)
#print(student1.name)

#print(student2.gpa)
'''
from Question import Question

question_prompts = [
    "What colour are Apples?\n(a) Red/Green\n(b) Magenta\n (c)Yellow\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n (c)Yellow\n\n",
    "What colour are Strawberries?\n(a) Teal\n(b) Red\n (c)Yellow\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got" + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)'''
#Object Functions
'''from Student1 import Student1
student1 = Student1("Oscar", "Accounting", 3.1)
student2 = Student1("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())
'''
