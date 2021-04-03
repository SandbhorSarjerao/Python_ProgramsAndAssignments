
'''
1. () Paranthesis
2. ** Exponetial Operator
3. Bitwiswe Complement, Unary Minus
4. *    /  %    //
5. +    -
6. <<   >>  Shift Operator
7. &
8. ^
9. |
10. > >= < <= == !=
11. = += -+
12. is, is not
13. in, not in
14. logical not
15. logical and
16. logical or
'''

'''
@. Which of the following is valid python operator precedence order ?
A) 
Parenthesis
Exponents
Unary Positive, Negative and Not
Addition and Subtraction
Multiplication and Division
And

B)   ==> Correct Answer
Parenthesis
Exponents
Unary Positive, Negative and Not
Multiplication and Division
Addition and Subtraction
And

C)
Exponents
Unary Positive, Negative and Not
Multiplication and Division
Addition and Subtraction
And
Parenthesis
'''
print(10+20*3)      # 10+(20*3)
print('Multiplicaiton: ', 2 * '20' + '20')         # '202020'

result = (2*(3+4)**2-(3**3)*3) # = (2(*(7)**2-(27)*3) = 2*49-27*3 = 98-81 = 17
print('Result :', result)

a, b, c, d = 5, 3, 9, 7
result1 = a - b * c + d     # = 5-3*9+7 = 5-(3)*9+7 = 5+(-27+7) = 5+(-20) = -15
print('Result :', result1)

lst = [7, 8, 9]
b = lst[:]
print(b is lst)
print(b == lst)