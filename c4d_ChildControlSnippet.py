# par = The First child of Parent Object
# olen = Distance of child from Parent
# co = The returned reference

def getInstance(par,olen):
    co = par
    for x in range(olen):
        if co != None:
            co = co.GetNext()
    return co
