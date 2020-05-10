pos = -1


def searchNo(list, no):
    for i in range(len(list)):
        if list[i] == no:
            globals()['pos'] = i
            return True
    return False


list = [5, 1, 8, 12, 4, 6, 9, 2, 10]
no = int(input('Enter no to Search in List: '))

if searchNo(list, no):
    print(no, 'Found in List at Position ', pos + 1)
else:
    print(no, 'Not Found in List')

