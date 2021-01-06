def getInstance(par,olen):
    co = par
    for x in range(olen):
        if co != None:
            co = co.GetNext()
    return co
