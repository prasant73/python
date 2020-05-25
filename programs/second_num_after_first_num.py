import random

def frequency(l, f_num, s_num):
    print(l, f_num, s_num, sep = "\n")
    # write code here
    return "Working..."

def list_dec(num, start, end):
    l = []
    for _ in range(num):
        l.append(random.randint(start, end))
    return l

def main():
    print
    (
        frequency(
            list_dec(
                int(input("Enter the number of numbers you want in list : ")),
                int(input("Enter beginning : ")),
                int(input("Enter end : "))
            ),  
        int(input("Enter first number : ")),
        int(input("Enter second number"))
        )
    )
print(__name__)
if __name__ == "__main__":
    main()