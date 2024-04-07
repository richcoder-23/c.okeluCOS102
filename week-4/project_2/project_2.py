# TAKE YEARS OF EXPERIENCE
#IF NORE THAN 25 YEARS AND AGE >= 55. atr = 5,600,000
#IF MORE THAN 20 AND AGE >= 45. ATR = 4,480,000
#MORE THAN 10 AND AGE >= 35. ATR = 1,500,000
#ELSE IF STAFF < 10 AND AGE <35 . ATR = 550,000


years = int(input("HOW MANY YEARS OF EXPERIENCE DO YOU HAVE? : "))
age = int(input("HOW OLD ARE YOU? : "))

if years > 25 and age >= 55:
    print("YOUR ATR IS N 5,600,000") 
elif years > 20 and age >= 45:
    print("YOUR ATR IS N 4,480,000")
elif years > 10 and age >= 35:
    print("YOUR ATR IS N 1,500,000")
elif years < 10 and age < 35:
    print("YOUR ATR IS N 550,000")
else: 
    print("No ATR calculated.")

    