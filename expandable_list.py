# Two Single Lists with Append and Looped Printing

list_a = []
list_b = []

list_a.append("a")
list_b.append(1)

list_a.append("b")
list_b.append(2)

list_a.append("c")
list_b.append(3)


print ("--- Print for Two Single Lists ---")
print ("Array of list_a: ",list_a)
print ("Array of list_b: ",list_b)
for i in range(len(list_a)):
    print (list_a[i] + " " + str(list_b[i]))

# One Double Lists with Append and Looped Printing

dList = []

dList.append(["d",4])
dList.append(["e",5])
dList.append(["f",6])
dList.append(["more_than_three_entries","g",7]) # Can expand, but not recommended to have more than 2 elements for a paired list

print ("--- Print for One Double List ---")
print ("Array of dList: ",dList)
for i1 in range(len(dList)): # This loop is for the root list
    pListString = "" # This string is to contain the results to be printed
    for i2 in range(len(dList[i1])): # This loop is for the child List being selected by the first loop
        pListString = pListString + str(dList[i1][i2]) # This adds the result as a string to the temporary string holder
        if (i2 < len(dList[i1])-1): # This checks if the current child loop did or did not reach the end index before adding a space/separator
            pListString = pListString + " "
    print (pListString) #This prints the temporary string
