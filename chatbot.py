def chatbot ():
    print("hi,i am chatbot how can i help you today?")
    while True:
        user_input = input("you:")
        if user_input.lower()== "bye":
            print("chatbot: bye! have a great day!")
            break
        elif user_input.lower()=="hello":
            print("chatbot: hello there! how are you doing today?")
        elif user_input.lower()=="how are you":
            print("chatbot: i'am doing great! thanks for asking!how about you?")
        else:
            print("chatbot: sorry, i didn't understand what you said, can you please rephrase?")

chatbot()



def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I·was·created·in·{0}.".format(birth_year))
    
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))

def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')

def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()

greet('Sbot', '2021') # change it as you need
remind_name()
guess_age()
count()
test()
end()