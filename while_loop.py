# i = 0
# while (i <10):
#     i = i+1
#     print (i)
    
'''the code above is a while loop that prints out 1 to 10. it uses i as a pointer and loops based on whether i is less than 10
on each iteration it increases i by 1 and prints the value for i. the code above can't be used to print 7 to 19 because the stop condition ensures that it doesn't go beyond 10'''

def evens(x: int, y: int):
    for i in range(x,y,2):
        print (i)
        
        
def reverse_evens(x: int, y: int):
    for i in range(y,x,-2):
        print (i)




evens(12,20)
reverse_evens(12,20)