#Program to print alphabetic letters in patterns of your choice
def pattern():

    choice = input("Enter the capital letter you want to print a pattern of-")

    ch=input("Enter the choice of character for the pattern: ")

    if choice == 'A':
        pattern_A = ""
        for row in range(0, 7):
            for col in range(0, 13):
                if ((col == 5 and row == 0) or ((col == 4 or col == 6) and (row == 1)) or (
                        (col == 3 or col == 7) and row == 2) or ((col > 1 and col < 9) and (row == 3)) or (
                        col == 1 or col == 9) and (row == 4) or (col == 0 or col == 10) and (row == 5)):
                    pattern_A = pattern_A + ch
                else:
                    pattern_A = pattern_A + " "
            pattern_A = pattern_A + "\n"
        print(pattern_A)


    elif choice == 'B':
        pattern_B = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if (col == 0) or ((row == 0 or row == 3 or row == 6) and col < 5) or (
                        row == 1 and col == 5 or (row == 2 and col == 5) or ((row == 4 or row == 5) and (col == 5))):
                    pattern_B = pattern_B + ch
                else:
                    pattern_B = pattern_B + " "
            pattern_B = pattern_B + "\n"
        print(pattern_B)


    elif choice =='C':
        for row in range(0, 8):
            for col in range(0, 7):
                if ((col == 0 and (row > 0 and row < 6) or (col > 2 and (row == 0 or row == 6)))):
                    print(ch, end=" ")
                else:
                    print(end=" ")
            print()
    elif choice =='D':
        for row in range(0, 7):
            for col in range(0, 7):
                if ((col == 0) or (
                        (col > 0 and col < 3) and (row == 0 or row == 6) or (col == 6 and (row > 1 and row < 5)) or (
                        col == 5 and (row == 1 or row == 5)))):
                    print(ch, end=" ")
                else:
                    print(end=" ")
            print()

    elif choice =='E':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((col == 0) or (row == 0 or row == 3 or row == 6 and col > 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)

    elif choice == 'F':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((col == 0) or (row == 0 or row == 3 and col > 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'G':
        for row in range(0, 8):
            for col in range(0, 9):
                if ((col == 0 and (row > 0 and row < 6) or (col > 2 and col < 7 and (row == 0)) or (
                        col == 6 and (row == 5 or row == 4)) or (col > 1 and col < 5 and row == 6)) or (
                        row == 4 and col == 5 or (col == 7 and row == 6) or (row == 5 and col == 8))):
                    print(ch, end=" ")
                else:
                    print(end=" ")
            print()
    elif choice == 'H':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 8):
                if ((col == 0 or col == 7) or (col > 0 and row == 3)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'I':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 8):
                if ((col > 2 and col < 6) and (row == 0 or row == 6) or (col == 4 and (row > 0 or row < 6))):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'J':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 8):
                if ((col > 1 and col < 7) and (row == 0) or (col == 4 and (row > 0 or row < 6)) or (
                        col > 0 and col < 4 and row == 6) or (col == 0 and (row == 5))):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'K':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 8):
                if ((col == 0) or (col == 1 and (row == 3)) or (col == 2 and (row == 2 or row == 4)) or (
                        col == 4 and (row == 1 or row == 5)) or (col == 6 and (row == 0 or row == 6))):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'L':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((col == 0) or (row == 6 and col > 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'M':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 13):
                if (col == 0 or col == 12) or (
                        (row == col) and (col > 0) or (row == 5 and col == 7) or (row == 4 and col == 8) or (
                        row == 3 and col == 9) or (row == 2 and col == 10) or (row == 1 and col == 11)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'N':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if (col == 0 or col == 6) or ((row == col) and (col > 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'O':
        for row in range(0, 9):
            for col in range(0, 13):
                if ((col == 0 or col == 11) and (row == 4) or (col == 3 or col == 8) and (row == 1 or row == 7) or (
                        col == 1 or col == 10) and (row == 2 or row == 6) or (row == 0 or row == 8) and (col == 6)):
                    print(ch, end=" ")
                else:
                    print(end=" ")
            print()
    elif choice == 'P':
        pattern_P = ""
        for row in range(0, 7):
            for col in range(0, 13):
                if (col == 0) or ((row == 0 or row == 3) and col < 5) or (
                        row == 1 and col == 5 or (row == 2 and col == 5)):
                    pattern_P = pattern_P + ch
                else:
                    pattern_P = pattern_P + " "
            pattern_P = pattern_P + "\n"
        print(pattern_P)
    elif choice == 'Q':
        for row in range(0, 9):
            for col in range(0, 13):
                if ((col == 0 or col == 11) and (row == 4) or (col == 3 or col == 8) and (row == 1 or row == 7) or (
                        col == 1 or col == 10) and (row == 2 or row == 6) or (row == 0 or row == 8) and (col == 6) or (
                        col == 10 and row == 8) or (col == 6 and row == 6)):
                    print(ch, end=" ")
                else:
                    print(end=" ")
            print()
    elif choice == 'R':
        pattern_R = ""
        for row in range(0, 7):
            for col in range(0, 13):
                if (col == 0) or ((row == 0 or row == 3) and col < 4) or (
                        row == 1 and col == 4 or (row == 2 and col == 4) or (col == 2 and row == 4) or (
                        col == 3 and row == 5) or (col == 4 and row == 6)):
                    pattern_R = pattern_R + ch
                else:
                    pattern_R = pattern_R + " "
            pattern_R = pattern_R + "\n"
        print(pattern_R)
    elif choice == 'S':
        for row in range(9):
            for col in range(7):
                if (((row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or (
                        col == 0 and (row > 0 and row < 3)) or (col == 6 and (row == 4 or row == 5))):
                    print(ch, end=" ")
                else:
                    print(end=" ")

            print()
    elif choice == 'T':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 10):
                if ((row == 0 and col > 0) or (col == 5 and row > 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'U':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if (col == 0 and row < 6 or col == 6 and row < 6) or (row == 6 and (col > 0 and col < 6)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'V':
        pattern = ""
        for row in range(0, 6):
            for col in range(0, 18):
                if ((row == col) and (col > 0) or (row == 3 and col == 7) or (row == 4 and col == 6) or (
                        row == 2 and col == 8) or (row == 1 and col == 9)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'W':
        pattern = ""
        for row in range(0, 6):
            for col in range(0, 18):
                if ((row == col) and (col > 0) or (row == 3 and col == 7) or (row == 4 and col == 6) or (
                        row == 2 and col == 8) or (row == 1 and col == 9) or (row == 2 and col == 10) or (
                        row == 3 and col == 11) or (row == 4 and col == 12) or (row == 5 and col == 13) or (
                        row == 4 and col == 14) or (row == 3 and col == 15) or (row == 2 and col == 16) or (
                        row == 1 and col == 17)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)


    elif choice == 'X':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((row == col) or (col == 0 and row == 6) or (col == 1 and row == 5) or (col == 2 and row == 4) or (
                        col == 4 and row == 2) or (col == 5 and row == 1) or (col == 6 and row == 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'Y':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((col == 0 and row == 0) or (col == 1 and row == 1) or (col == 2 and row == 2) or (
                        col == 3 and row == 3) or (col == 0 and row == 6) or (col == 1 and row == 5) or (
                        col == 2 and row == 4) or (col == 4 and row == 2) or (col == 5 and row == 1) or (
                        col == 6 and row == 0)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)
    elif choice == 'Z':
        pattern = ""
        for row in range(0, 7):
            for col in range(0, 7):
                if ((row == 0 and col > 0) or (col > 0 and row == 6) or (col == 5 and row == 1) or (
                        col == 4 and row == 2) or (col == 3 and row == 3) or (col == 2 and row == 4) or (
                        col == 1 and row == 5)):
                    pattern = pattern + ch
                else:
                    pattern = pattern + " "
            pattern = pattern + "\n"
        print(pattern)


pattern()


