line_number = 0
with open("logs.txt", "r") as file:
    for each_line in file:
        line_numer= line_number + 1
        if "password" in each_line:
            print(each_line)
            print("The line number is: ", line_number)


'''
create fine called line counter.py
copy and paste song lyricsinto a lyrics.txt file
write a program that outputs the total number of lines'''