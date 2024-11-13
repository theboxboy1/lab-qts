

# to run each code, delete the '#' next to the main function call

def main():
    temp = int(input("Input temperature: "))
    unit = input("Input unit (C or F): ").lower()
    print(convert(temp,unit))

def convert(temp,unit):
    if unit == "c":
        return f"{(temp-32)*(5/9):.2f} C"
    elif unit == "f":
        return f"{temp*(9/5)+32:.2f} F"
    else:
        return "Invalid unit. Select C or F"
    
#main()


def main2():
    num = int(input("Input num: "))

    print(check(num))


def check(num):
    if num %2 == 0:
        return "Even"
    else:
        return "Odd"

#main2()


def main3():
    
    num1 = float(input("Enter first num: "))
    num2 = float(input("Enter second num: "))
    operator = input("Input operator (+,-,*,/): ")
    print(calc(num1,num2,operator))

def calc(num1, num2, operator):

    if operator == "+":
        return num1+num2
    
    elif operator == "-":
        return num1-num2
    
    elif operator == "*":
        return num1*num2
    
    elif operator == "/":
        return num1/num2
    
    else:
        return "Invalid operator yo."

#main3()

def main4():
    num = int(input("Input num: "))
    print(multi_table(num))

def multi_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {3*i}")
    return "" 

#main4()


def main5():

    score = int(input("Enter score: "))
    print(grade_calc(score))


def grade_calc(score):
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
#main5()






dic = {}

def main6():
   
   while True:
        try:
            item = input()
            if item in dic:
                dic[item] += 1
            else:
                dic[item] = 1



        except EOFError:
            sorted_dict = dict(sorted(dic.items()))
            
            for key, value in sorted_dict.items():
                print (value, key.upper())
            break


#main6()
