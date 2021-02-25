# Fiboanacci
# TODO: HW: Rewrite code, which will return only needed element of Fib sequence

elements = int(input("How many elements? "))

element1, element2 = 0, 1
count = 0

if elements <= 0:
   print("Please enter a positive integer")
elif elements == 1:
   print("Fibonacci sequence upto",elements,":")
   print(element1)
else:
   print("Fibonacci sequence:")
   while count < elements:
       print(element1)
       elementh = element1 + element2
       element1 = element2
       element2 = elementh
       count = count + 1