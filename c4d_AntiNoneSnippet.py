def main():
    # par = Link Port of Parent
    # Next = Distance Count
    # co = Present Instance
    # XPressoG = The XGroup with UserData
    
    if par != None:
        Next = XPressoG[c4d.ID_USERDATA,2]
        co = getInstance(par.GetDown(),Next)
        if co != None:
            co[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(PX,PY,PZ)
            co[c4d.ID_BASEOBJECT_REL_SCALE] = c4d.Vector(SX,SY,SZ)
            co[c4d.ID_BASEOBJECT_REL_ROTATION] = c4d.Vector(RH,RP,RB)
            XPressoG.SetName(co.GetName())
            XPressoG[c4d.ID_USERDATA,3] = co
        else:
            XPressoG.SetName("Object")
            XPressoG[c4d.ID_USERDATA,3] = None
    else:
        XPressoG.SetName("Object")
        XPressoG[c4d.ID_USERDATA,3] = None
