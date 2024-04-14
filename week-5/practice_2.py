def changme(mylist):
    #this changes a passes list
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changme( mylist )
print ("Values outside the function: ", mylist)
