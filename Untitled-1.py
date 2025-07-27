import pandas as pd 
print("welcome sir how are you")
items = {"ps5": [50000],
         "graphic card":[10]
         }
for i in items:
    print(i)
food_order = input("enter your electronic item")
if food_order in items:
    print("ok sir your order is placed",food_order)
    data = pd.DataFrame(items[food_order])
    print(data)
    bill = items[food_order]
    print(bill,"this is bill")
else :
    print("sorry sir this is not avaliable")
a = {"item":food_order}
print(a)
c= input("do you want anymore item")
while "yes" in c:
    o= input("what is item")
    if o in items:
        print("ok sir order is placed")
        totalbill= items[food_order]+items[o]
        print(totalbill)
    else:
        print("sorry sir this item is not avaliable")
    break
