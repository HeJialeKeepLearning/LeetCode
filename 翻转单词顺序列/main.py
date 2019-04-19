def ReverseSentence(s):
    sreverselist = s.split(' ')
    sreverselist.reverse()
    sreverse = ''
    for c in sreverselist:
        sreverse = sreverse + ' ' + c
    return sreverse[1:]
