line_counter = 0
empty_line_counter = 0
section_label_counter = 0

with open("lyrics.txt", "r") as file: 
    for every_line in file: 
        if every_line == "":
            every_line_counter = every_line_counter + 1

        elif every_line.startswith("["):
            section_label_counter = section_label_counter + 1

        else: 
            line_counter = line_counter + 1

    print("The Total Lines: ", line_counter)
    print("The total EMPTY lines: ", empty_line_counter)
    print(" The total section labels: ", section_label_counter)

    