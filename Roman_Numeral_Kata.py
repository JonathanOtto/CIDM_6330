# User is prompted to enter a number and it is returned in roman numerals
print("Enter a number")
number = int(input())
roman = ""
while number > 0:
    if number >= 1000:
        roman = roman + "M"
        number = number - 1000
    elif number >= 900:
        roman = roman + "CM"
        number = number - 900 
    elif number >= 500:
        roman = roman + "D"
        number = number - 500
    elif number >= 400:
        roman = roman + "CD"
        number = number - 400
    elif number >= 100:
        roman = roman + "C"
        number = number - 100
    elif number >= 90:
        roman = roman + "XC"
        number = number - 90
    elif number >= 50:
        roman = roman + "L"
        number = number - 50
    elif number >= 40:
        roman = roman + "XL"
        number = number - 40
    elif number >= 10:
        roman = roman + "X"
        number = number - 10
    elif number >= 9:
        roman = roman + "IX"
        number = number - 9
    elif number >= 5:
        roman = roman + "V"
        number = number - 5
    elif number >= 4:
        roman = roman + "IV"
        number = number - 4
    elif number >= 1:
        roman = roman + "I"
        number = number - 1
print("Number is " + roman)

# User is asked for a roman numeral and it is converted to numbers
print ("Enter Roman Numerals")
roman = str(input())
number = 0
check = 0
for x in roman:
    if check == 1:
        if x == "M":
            number = number + 800
        elif x == "D":
            number = number + 300
        elif x == "C":
            number = number + 80
        elif x == "L":
            number = number + 30
        elif x == "X":
            number = number + 8
        elif x == "V":
            number = number + 4
        check = 0    
    elif x == "M":
        number = number + 1000
    elif x == "D":
        number = number + 500
    elif x == "C":
        number = number + 100
        check = 1
    elif x == "L":
        number = number + 50
    elif x == "X":
        number = number + 10
        check = 1
    elif x == "V":
        number = number + 5
    elif x == "I":
        number = number + 1
        check = 1
print (number)