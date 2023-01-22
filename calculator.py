def calculator():
        
        print("Give your two values")
        num1= float(input ("First Number: "))
        num2= float(input ("Second Number: "))
        oper= input ("Do you want to divide, multiply, add, or subtract: ")

        if oper.lower() == 'divide':
                if num2 != 0:
                        print (num1 / num2);
                else:
                        print ("Cant Divide by Zero");
                        calculator();

        elif oper.lower() == 'multiply':
                print (num1 * num2)
        elif oper.lower() == 'add':
                print (num1 + num2)
        elif oper.lower() == 'subtract':
                print (num1 - num2)
        else:
                print ("That is not an option... please try again");
                calculator();
calculator();