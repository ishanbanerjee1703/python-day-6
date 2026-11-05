'''what should the functions be: 
quit function
select random quesiton
display question
display answer
'''
import random

flashcards = [
    {"question" : "What is Scotland's national animal", "answer" : "Mythical Unicorn"},
    {"question" : "How long was the shorted warever bewteen Britain and Zanzibar?", "answer" : "38-42 minutes"},
    {"question" : "What did ancient romans use as detergent?", "answer" : "Stale Human Urine"}
]


'''
task: say goodbye
input: none
side effect: prints goodbye message to terminal
return: none
'''
def quit_app():
    print("bye bye I guess, you're probably gonna fail but bye")


'''
task: choose and retrieve random element in flashcards list
input: flashcards list
side effect: 
return: the flashcards (dictionary)
'''
def get_random_question(cards):
    random_question = random.choice(cards)
    return random_question

'''
task: display the question
input: question card
side effect:  print question text to terminal
return: none
'''
def show_question(card):
    question = card["question"]
    print("Question:", question)


'''
task: display the answer
input: question car
side effect: print the answer to terminal
return: none
'''
def show_answer(card):
    answer = card["answer"]
    print("Answer:", answer)


def main():
    while True: 
        card = get_random_question(flashcards)
        show_question(card)

        user_choice = input("Would you like to see the answer, or quit?: ")
        if user_choice == "See the Answer" or user_choice == "see the answer":
            show_answer(card)  

        elif user_choice == "Quit" or user_choice == "quit":
            quit_app()
            break


main() 