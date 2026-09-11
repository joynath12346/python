""""

Write a function that takes 3 integer inputs from user and
outputs absolute values of these integers without using any
library functions.
  
Sample Input:
-100
234
-350

Sample Output:
100
234
350

""""

for i in range(3):
    
    x = int(input())

    if x < 0:
        x = x * -1
    
    print(x)
