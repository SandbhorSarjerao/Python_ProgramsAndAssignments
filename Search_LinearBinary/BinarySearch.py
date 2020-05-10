pos = -1

def searchNo(list, no):
    l, u = 0, len(list)-1
    for i in range(len(list)):
        mid = (l+u) // 2
        if list[mid] == no:
            globals() ['pos'] = i
            return True
        else:
            if list[mid] < no:
                l = mid+1
            else:
                u = mid-1


lst = [9, 5, 7, 3, 4, 6, 10, 8, 2, 1]
list = sorted(lst)      # list = [1,2,3,4,5,6,7,8,9,10]
no = int(input('Enter no to Search in List: '))

if searchNo(list, no):
    print(no, 'Found at Postion: ', pos-1)
else:
    print(no, 'Not Found in List')