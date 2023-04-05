filename = input("Enter a File Name : ")

try:
    with open(filename)as file:
        char_count = 0
        word_count = 0
        line_count = 0

        for line in file:
            line_count += 1
            # Strip Whitespace and Count Characters
            char_count += len(line.strip())
            # Split line into Words and Count them
            words = line.split()
            word_count += len(words)
        print("Character Count : ", char_count)
        print("Words Count : ", word_count)
        print("Line Count : ", line_count)
except FileNotFoundError:
    print(f"Error: {filename} not Found.!")
