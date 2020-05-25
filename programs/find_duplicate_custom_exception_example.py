import freq_char
# from Exceptions import DuplicateElementFound

class Error(Exception):
   pass

class DuplicateElementFound(Error):
   pass


def find_dup(l):
    ret_list = []
    for i in range(len(l)):
        try:
            if l[i] not in ret_list:
                ret_list.append(l[i])
            else:
                raise DuplicateElementFound
        # except DuplicateElementFound:
        #     print("Duplicate found, Exception Handled at index {}".format(i))
        except NameError:
            pass
    return ret_list


def main():
    try:
        n = int(input("enter the number of inputs you want to give : "))
    except Exception as e:
        print(e, "Exception Handled")

    print(__name__)

    input_array = []

    for i in range(n):
        try:
            input_array.append(int(input("Enter number {} : ".format(i+1))))
        except Exception as e:
            print(e, "Exception Handled")
            
    print(find_dup(input_array))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)