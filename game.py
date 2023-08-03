#Create a python quiz game 
print('Welcome to Mypython Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=4

if answer.lower()=='yes':
    answer=input('Question 1: What is your Favourite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2: Do you like programming in Python? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: What is the name of your favourite website for learning Python?')
    if answer.lower()=='Mosh ':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
   
    answer=input('Question 4: What is your favourite Python framework?')
    if answer.lower()=='Flask ':
        score += 1
        print('correct')
    else:
        print('Wrong answer :(')

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
