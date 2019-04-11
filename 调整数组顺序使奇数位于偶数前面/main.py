def reOrderArray(array):
    oddlist=[]
    evenlist=[]
    for i in array:
        if i%2==0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    return oddlist+evenlist