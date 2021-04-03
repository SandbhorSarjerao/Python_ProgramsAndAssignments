import sys

# > programeName.py 1stParameter 2ndParameter
# > InputParametersFromCommandLine.py 2 3

a = int(sys.argv[1])
b = int(sys.argv[2])
print("Sum is : ", a + b)