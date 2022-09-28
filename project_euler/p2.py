# Problem 2
#
# Each new term in the Fibonacci sequence is generated by adding 
# the previous two terms. By starting with 1 and 2, 
# the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
#
class P2:
    # Functions

    # Main
    sum, count = 0, 0
    n1, n2 = 0, 1
    while count < 4000000:
        nth = n1 + n2
        #print(nth)
        if nth % 2 == 0:
            sum += nth
        n1 = n2
        n2 = nth
        count += nth

    print(sum)