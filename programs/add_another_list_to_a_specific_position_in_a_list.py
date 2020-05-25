from inputs import list_input
from second_num_after_first_num import *

def adding_list_at_specific_place(l1, l2, pos):
    for i in range(len(l1)) : 
        if i == pos-1:
            for j in range(len(l2)):
                l1[i] = l2[j]
                l1[i+1] = l2[j+1]
print(__name__)
def main():
    l1 = list_input(int(input("Enter size of l1 : ")))
    l2 = list_input(int(input("Enter size of l2 : ")))

    print(adding_list_at_specific_place(l1, l2, pos = int(input("Enter the position you wan to input : "))))
print(__name__)
if __name__ == "__main__":
    main()