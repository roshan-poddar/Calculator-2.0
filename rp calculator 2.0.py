def rp():
    b = input("Enter your name:")
    def rp1():
        print(b+" WELCOME TO RP CALCULATOR 2.0")
        print("""Option provided:
             1.Sum        2.Subtract
             3.Multiply   4.Divide
             5.Sqrt       6.Log
             7.Sin        8.Cos
             9.Tan       10.Degrees
            11.Radians""")
        a = input(b+" Choose your option:")
        if a == "1":
            def sum():
                a = int(input("Enter the number:"))
                b = int(input("Enter the number:"))
                c = a+b
                print("Sum","=",c)
                i =1
                while i <100:
                    f = input("You want to add more number in the resulting value:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        d = int(input("Enter the number:"))
                        
                        e = d+c
                        d = c
                        c = e
                        print("Sum","=",e)
                        i += 1
                    else:
                        break
                
                g = input("You want to reuse our program:")
                if "Yes" in g or "YES" in g or "yes" in g or "Y" in g or "y" in g:
                    rp1()
                else:
                    print("Thank you for using our program")
                        
            sum()
        elif a == "2":
            def sub():
                a = int(input("Enter the number:"))
                b = int(input("Enter the number:"))
                c = a-b
                print("Sub","=",c)
                i =1
                while i <100:
                    f = input("You want to subtract more number in the resulting value:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        d = int(input("Enter the number:"))
                        
                        e = c-d
                        d = c
                        c = e
                        print("Sub","=",e)
                        i += 1
                    else:
                        break
                g = input("You want to reuse our program:")
                if "Yes" in g or "YES" in g or "yes" in g or "Y" in g or "y" in g:
                    rp1()
                else:
                    print("Thank you for using our program")
            sub()
        elif a == "3":
            def multiply():
                a = int(input("Enter the number:"))
                b = int(input("Enter the number:"))
                c = a*b
                print("Multiply","=",c)
                i =1
                while i <100:
                    f = input("You want to multiply more number in the resulting value:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        d = int(input("Enter the number:"))
                        
                        e = c*d
                        d = c
                        c = e
                        print("Multiply","=",e)
                        i += 1
                    else:
                        break
                g = input("You want to reuse our program:")
                if "Yes" in g or "YES" in g or "yes" in g or "Y" in g or "y" in g:
                    rp1()
                else:
                    print("Thank you for using our program")
            multiply()
        elif a == "4":
            def div():
                a = int(input("Enter the number:"))
                b = int(input("Enter the number:"))
                c = a/b
                print("Div","=",c)
                i =1
                while i <100:
                    f = input("You want to divide more number in the resulting value:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        d = int(input("Enter the number:"))
                        
                        e = c/d
                        d = c
                        c = e
                        print("div","=",e)
                        i += 1
                    else:
                        break
                g = input("You want to reuse our program:")
                if "Yes" in g or "YES" in g or "yes" in g or "Y" in g or "y" in g:
                    rp1()
                else:
                    print("Thank you for using our program")
            div()
        elif a == "5":
            def sqrt():
                a = int(input("Enter the number:"))
                from math import sqrt
                b = sqrt(a)
                print("Sqrt","=",b)
                i = 1
                while i <100:
                    f = input("You want sqrt of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = sqrt(b)
                        b = c
                        print("Sqrt","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            sqrt()
        elif a == "6":
            def log():
                a = int(input("Enter the number:"))
                from math import log
                b = log(a)
                print("Log","=",b)
                i = 1
                while i <100:
                    f = input("You want log of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = log(b)
                        b = c
                        print("Log","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            log()
        elif a == "7":
            def sin():
                a = int(input("Enter the number:"))
                from math import sin
                b = sin(a)
                print("Sin","=",b)
                i = 1
                while i <100:
                    f = input("You want sin of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = sin(b)
                        b = c
                        print("Sin","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            sin()
        elif a == "8":
            def cos():
                a = int(input("Enter the number:"))
                from math import cos
                b = cos(a)
                print("Cos","=",b)
                i = 1
                while i <100:
                    f = input("You want Cos of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = cos(b)
                        b = c
                        print("Cos","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            cos()
        elif a == "9":
            def tan():
                a = int(input("Enter the number:"))
                from math import tan
                b = tan(a)
                print("Tan","=",b)
                i = 1
                while i <100:
                    f = input("You want tan of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = tan(b)
                        b = c
                        print("Tan","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            tan()
        elif a == "10":
            def degree():
                a = int(input("Enter the radian:"))
                from math import degrees
                b = degrees(a)
                print("Degree","=",b)
                i = 1
                while i <100:
                    f = input("You want degree of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = degrees(b)
                        b = c
                        print("Degree","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            degree()
        elif a == "11":
            def radian():
                a = int(input("Enter the degree:"))
                from math import radians
                b = radians(a)
                print("Radians","=",b)
                i = 1
                while i <100:
                    f = input("You want radians of resulting vlaue:")
                    if "Yes" in f or "YES" in f or "yes" in f or "Y" in f or "y" in f:
                        c = radians(b)
                        b = c
                        print("Radians","=",c)
                    else:
                        break
                d = input("You want to reuse our program:")
                if "Yes" in d or "YES" in d or "yes" in d or "Y" in d or "y" in d:
                    rp1()
                else:
                    print("Thank you for using our program")
            radian()
        else:
           print(b+" You entered something wrong")
           rp1()
    rp1()
rp()