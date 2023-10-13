#sum of the list
#let the list be a
a=[8,2,3,0,7]
print(sum(a))

#reverse a string
#let the string be x
x="1,2,3,4,a,b,c,d"
x="1,2,3,4,a,b,c,d"[::-1]
print (x)

#multiples of numbers in a list
myList=[8,2,3,-1,7]
myList=[8*2*3*-1*7]
print(myList)

#print even numbers from the list
def numbers(even_numbers):
    even= [] 
    for x in even_numbers:
                if x%2==0:
                 even.append(x)
    print(f"even numbers are {even}")
numbers([1,2,3,4,5,6,7,8,9])

        
    


