# This is a sample Bundle Printing and Input
def updateInventory(bundle,excessBundle,itemName,itemValue):
    inventoryMax = 64
    inventoryValue = 0
    for i1 in range(len(bundle)):
        inventoryValue = inventoryValue + bundle[i1][1]
    if inventoryValue + itemValue <= inventoryMax:
        bundle.append([itemName,itemValue])
    elif inventoryValue + itemValue > inventoryMax and (itemValue - ((itemValue + inventoryValue) - inventoryMax)) != 0:
        bundle.append([itemName,itemValue - ((itemValue + inventoryValue) - inventoryMax)])
        excessBundle.append([itemName,itemValue - bundle[len(bundle)-1][1]])
    else:
        excessBundle.append([itemName,itemValue]);

def printBundle(bundle,excessBundle):
    print ("Current Bundle Items:")
    for i1 in range(len(bundle)):
        bundleString = ""
        for i2 in range(len(bundle[i1])):
            bundleString = bundleString + str(bundle[i1][i2])
            if i2 < len(bundle[i1])-1:
                bundleString = bundleString + " x "
        print (bundleString)
    print (" ")
    if len(excessBundle) > 0:
        print ("Excess Items:")
        for i1 in range(len(excessBundle)):
            excessBundleString = ""
            for i2 in range(len(excessBundle[i1])):
                excessBundleString = excessBundleString + str(excessBundle[i1][i2])
                if i2 < len(excessBundle[i1])-1:
                    excessBundleString = excessBundleString + " x "
            print (excessBundleString)
        print (" ")

bundle = []
excessBundle = []
#Bundle has 2 elements, maximum of 64 stackable items
while (True):
    itemName = str(input("Input your Item Name: "))
    itemValue = int(input("Input Item Quantity: "))
    updateInventory(bundle,excessBundle,itemName,itemValue)
    printBundle(bundle,excessBundle)
    response = str(input("Add another item? Enter X to end. "))
    print (" ")
    if response.upper() == "X":
        break
    excessBundle.clear()
