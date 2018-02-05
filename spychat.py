print"hello world"
print"welcome to spychat"
print"Let's get started"
spy_name=raw_input("what is your spy name? ")
if len(spy_name)>=2:
    print "welcome " + spy_name, "glad to meet you. "
    spy_salutation = raw_input("what should we call you (Mr. or Mrs)?")
    if len(spy_salutation)>0:
        spy_name = spy_salutation + spy_name
        print"alright " + spy_name + ". I'd like to  know more about you "
        spy_age=input("enter your age")
        if spy_age>12 and spy_age<50:
            print"your age is fine to be spy"
            spy_rating=input("enter your rating: ")
            if(spy_rating)>=5:
                print"great spy"
            elif spy_rating>=4 and spy_rating<5:
                print"good spy"
            elif spy_rating>=3.5 and spy_rating<4.5:
                print"averag spy"
            else:
                print" you are a bad spy"


else:
    print"invalid name enter 2 letter name atleast"
