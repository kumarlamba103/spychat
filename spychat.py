from spy_details import spy_name,spy_age, spy_rating

print"Hello!!"
print"Welcome to Spychat"
print"Let\'s get started"


def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu:
        menu_choice=input("What do you want to do? \n 1. Add a status update\n 0. Exit :: \n")

        if(menu_choice == 1):
            status = raw_input( "Your status please::")
            print status
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid Choice"


spy_exist=raw_input("Are you existing user? Y or N ::")
if spy_exist.upper() == "Y":
    print "We already have your details..."
    start_chat(spy_name, spy_age, spy_rating)

elif spy_exist.upper() == "N":
    spy_name=raw_input("What is your spy name?\n")

    if len(spy_name)>3:
        print"Welcome " + spy_name + ",Glad to meet you. "
        spy_salutation=raw_input("What should we call you (Mr. or Ms.)?\n")
        if (spy_salutation)>0:
            spy_name= spy_salutation + " " + spy_name
            print"Alright " +spy_name + ". I'd like to know a little bit more about...."
            spy_age=input("Enter Your Age::")
            if spy_age > 12 and spy_age < 50:
                print "Your age is fine to be a spy"
                spy_rating=input("Enter Your Rating::")
                if spy_rating>=5:
                    print "Great Spy"
                elif spy_rating>=4.5 and spy_rating<5:
                    print "Good Spy"
                elif spy_rating>=3.5 and spy_rating<4.5:
                    print "Average Spy"
                else:
                    print "Bad Spy"
                spy_is_online=True
                print "Authentication Complete. Welcome  %s  Age:  %d  And Rating of: %.2f Proud to have you on board" %(spy_name ,spy_age ,spy_rating )
                start_chat(spy_name,spy_age,spy_rating)
            else:
                print "Your age is not fine to be a spy..."
        else:
            print"Invalid salutation..."

        print"Invalid name!! please enter a 3 letters name atleast..."
else:
    print "Wrong Input..."