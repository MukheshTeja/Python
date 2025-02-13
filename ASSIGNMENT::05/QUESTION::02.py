#halloween party
t=int(input("enter the number of test cases::>"))
print("enter the number to calc the no.of horizontal and vertical pieces")
for i in range(t):
    number=int(input("::>"))
    if number % 2==0:
        num_of_pieces= (number//2)**2
        print(num_of_pieces)
    else:
        test=int(number/2)
        test_1=number-test
        num_of_pieces=test*test_1
        print(num_of_pieces)
        
            
        
