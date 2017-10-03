test = 10000000000000

if type(test) == int:
    if test >= 100:
        print "That's a big number!"
    else:
        print "That's a small number"
elif type(test) == str:
    if len(test) >= 50:
        print "Long sentence."
    else:
        print "Short Sentence."
elif type(test) == list:
    if len(test) >= 10:
        print "Big List!"
    else:
        print "Short List."