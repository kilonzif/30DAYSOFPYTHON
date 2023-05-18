'''
write a function in python that takes 
a list of numbers and returns the sum of the given numbers. 
'''


def addList(aList):
    sum=0
    for item in aList:
        sum +=item 
    
    return sum

if __name__ == 'main':
    alist = [23,3,4,6,5]
    print(addList(alist))

    