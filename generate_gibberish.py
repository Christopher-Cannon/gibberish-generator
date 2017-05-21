import random

def generate_text(lpl, para_count):
    return_text = ""

    for x in range(para_count):
        para_length = random.randint(2, 9)

        return_text += generate_para(lpl, para_length) + "\n\n"

    return return_text

def generate_para(lpl, lines):
    para_text = ""

    for x in range(lines):
        para_text += generate_line(lpl)

        if(x < (lines - 1)):
            para_text += '\n'
        else:
            while(para_text[len(para_text) - 1] == " "):
                para_text = para_text[0:len(para_text) - 2]

            l_pos = para_text[len(para_text) - 1]

            if(l_pos != ".") and (l_pos != ",") and (l_pos != "!") and (l_pos != "?") and (l_pos != ":"):
                para_text += "."

    return para_text

def generate_line(lpl):
    line_to_write = ""

    while(len(line_to_write) < lpl):
        line_to_write += generate_word()

    return line_to_write

def let_type(word, pos):
    global letters
    l_let = ""

    for x in letters[0]:
        if(word[pos] == x):
            return "vowel"

    if(l_let == ""):
        return "consonant"

def generate_word():
    global letters
    word, lst, l_let, sl_let, punct = "", 0, "", "", ".,!?:"
    word_length = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]
    length = random.choice(word_length)
    add_punct = random.random()

    for x in range(length):
        if(len(word) > 1):
            l_let = let_type(word, -1)
            sl_let = let_type(word, -2)

            if(l_let == sl_let):
                if(l_let == "vowel"):
                    lst = 1
                    letter = letters[lst][random.randint(0, len(letters[lst]) - 1)]
                elif(l_let == "consonant"):
                    lst = 0
                    letter = letters[lst][random.randint(0, len(letters[lst]) - 1)]
            else:
                lst = random.randint(0, 1)
                letter = letters[lst][random.randint(0, len(letters[lst]) - 1)]
        else:
            lst = random.randint(0, 1)
            letter = letters[lst][random.randint(0, len(letters[lst]) - 1)]

        word += letter

    if((add_punct > 0.78) and (length != 1) and (length != 2)):
        word += punct[random.randint(0, len(punct) - 1)]

    return word + " "

def letter_frequency():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    v_freq, c_freq = "", ""

    for v in vowels:
        v_freq += v * random.randint(7, 11)

    for c in consonants:
        c_freq += c * random.randint(2, 5)

    return [v_freq, c_freq]

def main():
    lpl = int(input("How many letters per line?\t-> "))
    para_count = int(input("How many paragraphs to create?\t-> "))
    doc_name = str(input("Please name the document:\t-> "))

    with open(doc_name + ".txt", "wt") as out_file:
        out_file.write(generate_text(lpl, para_count))

    print("Done")

letters = letter_frequency()

main()
