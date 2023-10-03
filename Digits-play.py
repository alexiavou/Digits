# -*- coding: utf-8 -*-
"""
Digits and Digits+
Based on the New York Times' game, Digits

Copyright (C) 2023  Alexia Vouloumanos

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
import random



def initS1():
    x = random.randint(51,99)
    if x % 10 == 0:
        x += random.randint(1,9)
        
    digits = []
    y = random.randint(3,4)
    digits.extend(random.sample(range(2,9), y))
    digits.extend(random.sample(range(10,15), (5-y)))
    z = random.randint(1,2)
    if z == 1:
        digits.extend([20])
    if z == 2:
        digits.extend([25])
    digits.sort()
    
    return x, digits


def initS2():
    x = random.randint(101,199)
    if x % 10 == 0:
        x += random.randint(1,9)
        
    digits = []
    digits.extend(random.sample(range(2,9), 3))         
    digits.extend(random.sample(range(10,19), 2))
    digits.extend(random.sample(range(20,25), 1))
    digits.sort()
    
    return x, digits


def initS3():
    x = random.randint(201,299)
    if x % 10 == 0:
        x += random.randint(1,9)
        
    digits = []
    y = random.randint(1,2)
    digits.extend(random.sample(range(2,9), 3))         
    digits.extend(random.sample(range(10,19), y))
    digits.extend(random.sample(range(20,25), (3-y)))
    digits.sort()
    
    return x, digits


def initS4():
    x = random.randint(301,399)
    if x % 10 == 0:
        x += random.randint(1,9)
            
    digits = []
    y = random.randint(1,2)
    digits.extend(random.sample(range(2,9), 3))         
    digits.extend(random.sample(range(10,19), y))
    digits.extend(random.sample(range(20,25), (3-y)))
    digits.sort()

    return x, digits


def initS5():
    x = random.randint(401,499)
    if x % 10 == 0:
        x += random.randint(1,9)
        
    digits = []
    y = random.randint(2,3)
    digits.extend(random.sample(range(2,9), y))         
    digits.extend(random.sample(range(10,19), (4-y)))
    digits.extend(random.sample(range(20,25), 2))
    digits.sort()

    return x, digits


def pointSystem():
    global pts
    pts = 0


#-----------------------------------------------------------------------------#
# Original: +, -, *, /  (addition, subtraction, multiplication, division)

def digitsBase(x, digits, points):
    print(x)
    print("")
    print(digits)
    
    original = digits.copy()
    toggle = 0
    
    while len(digits) > 1:
        try:
            op = input("Operation: ")
            
            length = len(digits)
            if length == 5:
                first = digits.copy()
            elif length == 4:
                second = digits.copy()
            elif length == 3:
                third = digits.copy()
            elif length == 2:
                fourth = digits.copy()
            
            if op.casefold() == "undo":
                length = len(digits)
                if length == 6:
                    print("Nothing to undo")
                    continue
                elif length == 5:
                    digits = original.copy()
                elif length == 4:
                    digits = first.copy()
                elif length == 3:
                    digits = second.copy()
                elif length == 2:
                    digits = third.copy()
                    digits = third.copy()
                elif length == 1:
                    digits = fourth.copy()
                print("")
                print(digits)
                continue
            
            if op.casefold() == "reset":
                digits = original.copy()
                print("")
                print(x)
                print(digits)
                continue
        
            if op.casefold() == "exit":
                toggle = 1
                break
            
            if op.casefold() == "submit":
                global pts
                toggle = 2
                for i in range(len(digits)-1, -1, -1):
                    if abs(x-digits[i]) <= 2:
                        pts = points+2
                        break
                    elif abs(x-digits[i]) <= 5:
                        pts = points+1
                        break
                break
            
            if any(char.isdigit() for char in op):
                if "+" in op:
                    ind = op.index("+")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    digits.append((p+q))
                elif "-" in op:
                    ind = op.index("-")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    if p < q:
                        print("Numbers must be >= 0")
                        continue
                    else:
                        digits.append((p-q))
                elif "*" in op:
                    ind = op.index("*")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    digits.append((p*q))
                elif ("/" in op) and ("^/" not in op):
                    ind = op.index("/")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    if q == 0:
                        print("Division by 0 is undefined")
                        continue
                    if p % q != 0:
                        print("Numbers must be integers")
                        continue
                    else:
                        digits.append((p//q))
                else:
                    print("Please include a valid operator")
                    continue

                if (p in digits) and (q in digits):
                    if digits[(len(digits)-1)] >= 10000:
                        digits.pop()
                        print("Numbers must be less than 10,000")
                        print(digits)
                        continue
                    else:
                        digits.remove(p)
                        digits.remove(q)
                else:
                    digits.pop()
                    print("Please only include numbers from the list")
                    continue
            
                print("")
                print(digits)
    
                if x in digits:
                    pts = points+3
                    break
                
            else:
                print("No numbers entered")
                continue
            
        except ValueError:
            print("Invalid input")
            print(digits)
            
    if 0 <= pts <= 3:
        print("Nice!")
    elif 4 <= pts <= 6:
        print("Great!")
    elif 7 <= pts <= 9:
        print("Amazing!")
    elif 10 <= pts <= 12:
        print("Wow!")
    elif 13 <= pts <= 15:
        print("You're a genius!")
    
    if toggle != 0:
        print("\nGoodbye!")
    elif toggle == 0 and x not in digits:
        res = input("Would you like to try again? ")
        if res.casefold() == "yes":
            print("")
            digitsBase(x, original)
        elif res.casefold() == "no":
            print("\nThanks for playing!")
        else:
            print("\nGuess not :(")
        

#-----------------------------------------------------------------------------#   
# Extra operations: +, -, *, /, %, ^, ^/, || (modulo, exponents, roots, concatenation)

def digitsPlus(x, digits, points):
    print(x)
    print("")
    print(digits)
    
    original = digits.copy()
    toggle = 0
    
    while len(digits) > 1:
        try:
            op = input("Operation: ")
            
            length = len(digits)
            if length == 5:
                first = digits.copy()
            elif length == 4:
                second = digits.copy()
            elif length == 3:
                third = digits.copy()
            elif length == 2:
                fourth = digits.copy()
            
            if op.casefold() == "undo":
                length = len(digits)
                if length == 6:
                    print("Nothing to undo")
                    continue
                elif length == 5:
                    digits = original.copy()
                elif length == 4:
                    digits = first.copy()
                elif length == 3:
                    digits = second.copy()
                elif length == 2:
                    digits = third.copy()
                    digits = third.copy()
                elif length == 1:
                    digits = fourth.copy()
                print("")
                print(digits)
                continue
            
            if op.casefold() == "reset":
                digits = original.copy()
                print(x)
                print(digits)
                continue
        
            if op.casefold() == "exit":
                toggle = 1
                break
            
            if op.casefold() == "submit":
                global pts
                toggle = 2
                for i in range(len(digits)-1, -1, -1):
                    if abs(x-digits[i]) <= 2:
                        pts = points+2
                        break
                    elif abs(x-digits[i]) <= 5:
                        pts = points+1
                        break
                break
            
            if any(char.isdigit() for char in op):
                if "+" in op:
                    ind = op.index("+")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    digits.append((p+q))
                elif "-" in op:            
                    ind = op.index("-")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    if p < q:
                        print("Numbers must be >= 0")
                        continue
                    else:
                        digits.append((p-q))
                elif "*" in op:
                    ind = op.index("*")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    digits.append((p*q))
                elif ("/" in op) and ("^/" not in op):
                    ind = op.index("/")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    if q == 0:
                        print("Division by 0 is undefined")
                        continue
                    if p % q != 0:
                        print("Numbers must be integers")
                        continue
                    else:
                        digits.append((p//q))
                elif "%" in op:
                    ind = op.index("%")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    if q == 0:
                        print("Modulo 0 is undefined")
                        continue
                    else:
                        digits.append((p%q))
                elif ("^" in op) and ("^/" not in op):
                    ind = op.index("^")
                    p = int(op[0:ind])
                    q = int(op[(ind+1):])
                    digits.append((p**q))
                elif "||" in op:
                    ind = op.index("||")
                    p = int(op[0:ind])
                    q = int(op[(ind+2):])
                    pq = int(str(p)+str(q))
                    if p == 0:
                        digits.append(q)
                    else:
                        digits.append(pq)
                elif "^/" in op:
                    ind = op.index("^/")
                    p = int(op[0:ind])
                    q = int(op[(ind+2):])
                    if q == 0:
                        print("Zeroth root is undefined")
                        continue
                    elif (p**(1/q)) % 1 != 0:
                        print("Numbers must be integers")
                        continue
                    else:
                        digits.append(int(p**(1/q)))
                else:
                    print("Please include a valid operator")
                    continue
    
                if (p in digits) and (q in digits):
                    if digits[(len(digits)-1)] >= 10000:
                        digits.pop()
                        print("Numbers must be less than 10,000")
                        print(digits)
                        continue
                    else:
                        digits.remove(p)
                        digits.remove(q)
                else:
                    digits.pop()
                    print("Please only include numbers from the list")
                    continue
                
                print("")
                print(digits)

                if x in digits:
                    pts = points+3
                    break
            
            else:
                print("No numbers entered")
                continue
        
        except ValueError:
            print("Invalid input")
            print(digits)
            
    if 0 <= pts <= 3:
        print("Nice!")
    elif 4 <= pts <= 6:
        print("Great!")
    elif 7 <= pts <= 9:
        print("Amazing!")
    elif 10 <= pts <= 12:
        print("Wow!")
    elif 13 <= pts <= 15:
        print("You're a genius!")
        
    if toggle == 1:
        print("\nGoodbye!")        
    elif toggle == 0 and x not in digits:
        res = input("Would you like to try again? ")
        if res.casefold() == "yes":
            print("")
            digitsPlus(x, original)
        elif res.casefold() == "no":
            print("\nEnd")
        else:
            print("\nGuess not :(")        


#-----------------------------------------------------------------------------#     

def playDigitsBase():
    print("Digits\n")
    print("Create target number using operators: +, - , *, /")
    print("Each number can only be used once, but each number does not have to be used")
    
    print("\nEnter one expression per input")
    print("e.g. Operation: 8+7")
    
    print("\nYou can 'undo' your last operation, 'reset' the current set, 'submit' your closest number, or 'exit' the game.")
    print("Submissions are automatic if the target number is created, though you can manually submit for partial points:")
    print("\t\u2022 3 points if the target number is created")
    print("\t\u2022 2 points for a number within 2 of the target")
    print("\t\u2022 1 point for a number within 5 of the target")
    
    pointSystem()
    
    print("\n\nSet 1")
    digitsBase(*initS1(), pts)
    print(pts)

    print("\n\nSet 2")
    digitsBase(*initS2(), pts)
    print(pts)

    print("\n\nSet 3")
    digitsBase(*initS3(), pts)
    print(pts)

    print("\n\nSet 4")
    digitsBase(*initS4(), pts)
    print(pts)

    print("\n\nSet 5")
    digitsBase(*initS5(), pts)
    print(pts)
    
    print("\n\nThanks for playing!")
    


def playDigitsPlus():
    print("Digits+\n")
    print("Create desired number using operators: +, - , *, /, %, ^, ^/, ||")
    print("\t % : modulo\n\t ^ : exponent\n\t^/ : root\n\t|| : concatentation")
    print("Each number can only be used once, but each number does not have to be used")
    
    print("\nEnter one equation per input")
    print("e.g. Operation: 6^2")
    
    print("\nYou can 'undo' your last operation, 'reset' the current set, 'submit' your closest number, or 'exit' the game.")
    print("Submissions are automatic if the target number is created, though you can manually submit for partial points:")
    print("\t\u2022 3 points if the target number is created")
    print("\t\u2022 2 points for a number within 2 of the target")
    print("\t\u2022 1 point for a number within 5 of the target")
    
    pointSystem()
    
    print("\n\nSet 1")
    digitsPlus(*initS1(), pts)
    print(pts)
    
    print("\n\nSet 2")
    digitsPlus(*initS2(), pts)
    print(pts)
    
    print("\n\nSet 3")
    digitsPlus(*initS3(), pts)
    print(pts)
    
    print("\n\nSet 4")
    digitsPlus(*initS4(), pts)
    print(pts)
    
    print("\n\nSet 5")
    digitsPlus(*initS5(), pts)
    print(pts)
    
    print("\n\nThanks for playing!")
    

#-----------------------------------------------------------------------------#  
 
#NOTE: Make sure to comment out one version (unless you wish to play both back to back)

#playDigitsBase()  

playDigitsPlus()









