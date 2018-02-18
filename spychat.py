from spy_details import spy


from spy_details import Spy, ChatMessage

from steganography.steganography import Steganography

import time

import csv

print"\033[1;31m Hello\033[1;m"
print"\033[1;31m Welcome to Spychat\033[1;m"
print"\033[1;31m Let\'s get started\033[1;m"


def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            if row:
                name = row[0]
                age = row[1]
                rating = row[2]
            spy = Spy(name, age, rating)
            friends.append(spy)




STATUS_MESSAGES = ['I\'m in Gym','Sleeping','Busy']
friends = []
new_chats =[]
chats =[]


#define add status() function with parameters
def add_status(current_status_message):
    if current_status_message != None:
        print"your current status message is "+ current_status_message
    else:
        print "you dont have any status currently"

        #ask if a user want to select from old status

    status= raw_input("Do you want select from old status? Y or N: ")
    if len(status)>=1:
        # if use the old status
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

           #if not using old status
        elif status.upper()=='N':
             new_status=raw_input("Enter your status: ")
             if len(new_status)>1:
                STATUS_MESSAGES.append(new_status)
                return new_status
        else:
            print"Invalid entry"

    else:
        set_status='no status'
        return set_status




# define add friend() function to add a friend
def add_friend():

    new_friend = Spy("",0,0.0)

    new_friend.name=raw_input("what is the name of frnd")
    new_friend.age=input("what is the age of frnd")
    new_friend.rating=input("what is your rating")
    if len(new_friend.name)>3 and 50>new_friend.age>12 and new_friend.rating>=spy.rating :
        # append() function of list friends used to append details in dictionary new_friend
        friends.append(new_friend)
        print "friend is added"
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.age, new_friend.rating,new_friend.is_online])


    else:

        print"Sorry friend cannot be added......"
    return len(friends)
# define select_a_friend() function to select a friend from choices given

def select_a_friend():
    serial_no = 1
    for new_friend in friends:
        print str(serial_no) + " " + new_friend['name']
        serial_no = serial_no + 1
    user_selected_friend = input("select your friend")
    user_index =user_selected_friend - 1
    return user_index

# define send_message() function to send secret message to someone
def send_message():
    user_index = select_a_friend()
    original_image = raw_input("What is the name of your image? ")
    text = raw_input("What is your secret message? ")
    output_path =raw_input("Enter the name of your secret message image")
    # use of steganography library function encode to encode a message in image
    Steganography.encode(original_image, output_path, text)
    new_chat = ChatMessage(text,sent_by_me)

    with open('chats.csv', 'ab') as chats_data:
        write = csv.writer(chats_data)
        write.writerow([spy.name, friends[user_index].name , new_chat.message ,new_chat.time , new_chat.sent_by_me])


    # append new_chat to friends list
    user_index.chats.append(new_chat)
    print "Your secret message is ready!!!"
    print "The image is saved "+ output_path + " name . "
#Function defines for read the secret message


def send_help_message():
    # Selecting a friend
    friend_choice = select_a_friend()
    # The response
    text = ("Don't worry... I'm coming to save you!","magenta")
    # Creating new chat
    new_chat = ChatMessage((text,),False)
    # Appending the chat
    friends[friend_choice].chats.append(new_chat)



def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of your encrypted file? ")
    # use decode() function of steganography library to decode the encoded message
    secret_text = Steganography.decode(output_path)
    print secret_text

    new_chat = {
        "message":'text',
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your secret message is:" + secret_text
    print "Your secret message has been saved!"


def read_chat_history():
    friend_choice = select_a_friend()

    print '\n'

    for chat in friends[friend_choice].chats:
        if chat.sent_by_me:
            print (str(chat.time.strftime("%d %B %Y %A %H : %M")) + ",")
            # The message is printed in red
            print ("You : ")
            # Default colour black for text
            print str(chat.message)

        # Message sent by another spy
        else:
            # Date and time is printed in blue
            print (str(chat.time.strftime("%d %B %Y %A %H : %M"))+ "," )
            # The message is printed in red
            print (str(friends[friend_choice].name) + " : ", )
            # Black is by default
            print str(chat.message)

def remove_friend():                                         # Friend is removed from the current running application but changes aren't updated to friends.csv
    # Asking the user which friend to delete
    friend_choice = select_a_friend()                        # Hence, it is used to delete a friend from current running application only.
    # del command is used for deleting a particular friend
    del friends[friend_choice]                                # friend_choice specifies the friend to be deleted
    # Displaying message
    print ("Friend has been removed !")
    # Displaying number of friends left after removal
    return len(friends)





def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice=input("What do you want to do? \n 1. Add a status update\n!2.Add a friend \n 3.Send a message\n 4.Read a message.\n 5.Read chat history\n 6. Remove a friend\n 7.display a friend\n 0. Exit :: \n")

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
            new_friend = add_friend()
            print"you have"  +  str(new_friend) + "of friends"
        elif menu_choice == 3:
            user_index=select_a_friend()
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        elif menu_choice == 6:
            remove_friend()

        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid Choice"


spy_exist=raw_input("\033[1;35m Are you existing user? Y or N :: \033[1;m")
if spy_exist.upper() == "Y":
    print "\033[We already have your details..."
    time.sleep(0.001)
    start_chat(spy.name,spy.age, spy.rating)


elif spy_exist.upper() == "N":
    Spy = ("",0,0.0)
    spy.name=raw_input(" What is your spy name? ")

    if len(spy.name)>3:
        print"\033[1;31m Welcome " + spy.name + ",Glad to meet you.\033[1;m "
        spy.salutation=raw_input("\033[1;31m What should we call you (Mr. or Ms.)?\033[1;m")
        if (spy.salutation)>0:
            spy.name= spy.salutation + " " + spy.name
            print"\033[1;31m Alright " +spy.name + ". I'd like to know a little bit more about....\033[1;m"
            spy.age=input("\033[1;31m Enter Your Age:: \033[1;m ")
            if spy.age > 12 and spy.age < 50:
                print "Your age is fine to be a spy"
                spy.rating=input("Enter Your Rating::")
                if spy.rating>=5:
                    print "Great Spy"
                elif spy.rating>=4.5 and spy.rating<5:
                    print "Good Spy"
                elif spy.rating>=3.5 and spy.rating<4.5:
                    print "Average Spy"
                else:
                    print "Bad Spy"
                spy_is_online=True
                # Authentication is completed
                print "Authentication Complete. Welcome  %s  Age:  %d  And Rating of: %.2f Proud to have you on board" %(spy.name ,spy.age ,spy.rating )
                # call the start_chat() function
                start_chat(spy.name,spy.salutation,spy.age,spy.rating)

            #if age is  not valid
            else:
                print "Your age is not fine to be a spy..."
            # if name is not valid
        else:
            print"Invalid salutation..."

        print"Invalid name!! please enter a 3 letters name atleast..."
        # if input is eneterd wrong
else:
    print "\033[1;41m Wrong Input... INTRUDER ALERT\033[1;m"