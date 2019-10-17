x= raw_input("onoma omadas A")
y= raw_input("onoma omadas B")
z1= int(raw_input("set omadas A"))
z2= int(raw_input("set omadas B"))
if z1>z2:
    print "winner is " + x+ " with set " +str(z1-z2)
else:
    print "winner is " + y+ " with set " +str(z2-z1)
