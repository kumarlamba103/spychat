#import spy details from spy_details.py
from spy_details import spy

#import steganography class from python library


#from datetime library import date-time
from datetime import datetime

print"Hello!!"
print"Welcome to Spychat"
print"Let\'s get started"

STATUS_MESSAGES = ['I\'m in Gym','Sleeping','Busy']
friends = [{'name':'vikas','age':43,'rating':6}]

def add_status(current_status_message):
    if current_status_message != None:
        print"your current status message is "+ current_status_message
    else:
        print"you dont have any status currently"

    status= raw_input("Do you want select from old status? Y or N: ")
    if len(status)>=1:
        if status.upper()=='Y':
            serial_no = 1
            for old_status in STATUS_MESSAGES:
                print str(serial_no) + old_status
                serial_no = serial_no+ 1
            user_selection = input("Which one do you want select: ")
            if len(STATUS_MESSAGES)>=user_selection:
                 new_status= STATUS_MESSAGES[user_selection - 1]
            else:
                print"Invalid selection"
            return new_status
        elif status.upper()=='N':
             new_status=raw_input("Enter your status: ")
             if len(new_status)>1:
                STATUS_MESSAGES.append(new_status)

        else:
            print"Invalid entry"
        return new_status
    else:
        set_status='no status'
        return set_status

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }
    new_friend['name']=raw_input("what is the name of frnd")
    new_friend['age']=input("what is the age of frnd")
    new_friend['rating']=input("what is your rating")
    if len(new_friend['name'])>3 and 50>new_friend['age']>12 and new_friend['rating']>=spy['rating'] :
        friends.append(new_friend)

    else:
        print"friend cannot be added"
    return len(friends)

def select_a_friend():
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + " " + frnd['name']
        serial_no = serial_no + 1
    user_selected_friend = input("select your friend")
    user_index =int(user_selected_friend) - 1
    return user_index
def send_message():
    user_friend_index = select_a_friend()
    original_image = raw_input("What is the name of your image? ")
    text = raw_input("What is your secret message? ")
    output_path = 'output.jpg'
    # use of steganography library function encode to encode a message in image
    Steganography.encode(original_image, output_path, text)
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    # append new_chat to friends list
    friends[user_friend_index]['chats'].append(new_chat)
    print "Your secret message is ready!!!"

def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of your encrypted file? ")
    # use decode() function of steganography library to decode the encoded message
    Decrypted_text = Steganography.decode(output_path)

    new_chat = {
        "message": Decrypted_text,
        "time": datetime.now(),
        "sent_by_me": False
    }
    print "Your secret message is:" + Decrypted_text

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"



def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice=input("What do you want to do? \n 1. Add a status update\n!2.Add a friend \n 3.Send a message\n 4.Read a message.\n 5.Read chat history\n 0. Exit :: \n")

        if(menu_choice == 1):
           current_status_message = add_status( current_status_message)
           if len(current_status_message)>=1:
                if current_status_message == 'no status':
                    print"you didn't select status correctly"
                else:
                    print"your status has been set to " + current_status_message
           else:
               print"you did'nt select the status correctly"
        elif menu_choice == 2:
            no_of_frnds= add_friend()
            print"you have" + str(no_of_frnds) + "of friends"
        elif menu_choice == 3:
            user_friend=select_a_friend()
        elif menu_choice == 4:
            read_message()

        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid Choice"


spy_exist=raw_input("Are you existing user? Y or N ::")
if spy_exist.upper() == "Y":
    print "We already have your details..."
    start_chat(spy['name'], spy['age'], spy['rating'])

elif spy_exist.upper() == "N":
    spy = {
        'name': '',
        'age': 0,
        'rating': 0.0
    }
    spy['name']=raw_input("What is your spy name?\n")

    if len(spy['name'])>3:
        print"Welcome " + spy['name'] + ",Glad to meet you. "
        spy['salutation']=raw_input("What should we call you (Mr. or Ms.)?\n")
        if (spy['salutation'])>0:
            spy['name']= spy['salutation'] + " " + spy['name']
            print"Alright " +spy['name'] + ". I'd like to know a little bit more about...."
            spy['age']=input("Enter Your Age::")
            if spy['age'] > 12 and spy['age'] < 50:
                print "Your age is fine to be a spy"
                spy['rating']=input("Enter Your Rating::")
                if spy['rating']>=5:
                    print "Great Spy"
                elif spy['rating']>=4.5 and spy['rating']<5:
                    print "Good Spy"
                elif spy['rating']>=3.5 and spy['rating']<4.5:
                    print "Average Spy"
                else:
                    print "Bad Spy"
                spy_is_online=True
                print "Authentication Complete. Welcome  %s  Age:  %d  And Rating of: %.2f Proud to have you on board" %(spy['name'] ,spy['age'] ,spy['rating'] )
                start_chat(spy['name'],spy['age'],spy['rating'])
            else:
                print "Your age is not fine to be a spy..."
        else:
            print"Invalid salutation..."

        print"Invalid name!! please enter a 3 letters name atleast..."
else:
    print "Wrong Input..."