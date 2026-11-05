#challenge 1: logger.py
# write a program that asks user for their name and then adds it to a guest_list.txt file

def main():
    users_name = input("What is your name: ")
    with open("guest_list.txt", "a") as file: 
        file.write(users_name + "\n")

main()
