def FindNumsAppearOnce(self,array):
    arrdic = {}
    for i in array:
        if i in arrdic:
            del arrdic[i]
        else:
            arrdic[i] = 1
    return list(arrdic.keys())
