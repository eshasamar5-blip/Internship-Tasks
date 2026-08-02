
import math

while True:
    operation = input("CHOOSE  (+,-,/,*,sin,cos) or type  'end'  to exit:")
    if operation=="end":
        print ("Shutting down...")
        break
    if operation in ["+","-","*","/"]:
        a=float(input("ENTER FIRST NUMBER:"))
        b=float(input("ENTER SECOND NUMBER:"))
        if operation =="+":
            print ("Result", a+b)
        elif operation =="-":
            print ("result:", a-b)
        elif operation =="*":
            print ("result:", a*b)
        elif operation =="/":
            if b==0:
                print ("SYNTAX Error")
            else:
                print ("result:", a/b)

    elif operation == "sin":
        angle=float(input("ENTER ANGLE"))
        unit=input("DEGREE OR RADIANS d/r :")
        if unit=="d":
            angle=math.radians(angle)
        print ("Result:", math.sin(angle))
    elif operation == "cos":
        angle = float (input("ENTER ANGLE:"))
        unit=input("DEGREE OR RADIANS d/r:")
        if unit==" d":
            angle=math.radians(angle)
        print ("Result:", math.cos(angle))
    else:
        print ("INVALID operation")
