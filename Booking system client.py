#only one instance of a client can connect to the running server
import socket

IP = "127.0.0.1"
HOST = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialise server instance 
server.connect((IP, HOST)) #client establishes conenction to server

def welcomeMsg():

    print("\n**** Welcome to the Robotics Festival, please read the quotes below and proceed with booking a ticket(s) by answering the questions. ****") #welcome message sent to client in utf-8 encoded bytes
    print("\n----- Saturday ticket: £25 per adult & £20 per child ----- \n----- VIP ticket: £50 per adult & £25 per child ----- \n----- Sunday ticket: £10 per adult & £7.5 per adult ----- \n----- Weekend ticket: £30 per adult & £22 per child -----") #quotes for booking tickets sent to client in utf-8 encoded bytes


def userBookingInput():

    ## user inputs are asked for regarding ticket information and quantity ##
    name = input("\nEnter Name: ") #e.g., user input is asked for and stored in variable
    server.send(bytes(name, "utf-8")) #user input data is encoded to utf-8 bytes and sent to server

    ticketType = input("Enter ticket type: ")
    server.send(bytes(ticketType, "utf-8"))

    adultTickets = input("Enter quantity of adult tickets: ")
    server.send(bytes(adultTickets, "utf-8"))

    childTickets = input("Enter quantity of child tickets: ")
    server.send(bytes(childTickets, "utf-8"))


def checkTicketValidity():

    ticketCostEncoded = server.recv(1024) #client recieves the tickets costs in the form of encoded data (bytes) from server
    print(ticketCostEncoded.decode("utf-8")) #tickets costs byte data is decoded back into plain text and printed to screen

    if "invalid" in ticketCostEncoded.decode("utf-8"): #if the message sent by the server to the client is an error message that notifies of an invalid ticket type, exit program
        exit()

    if "waiting" in ticketCostEncoded.decode("utf-8"): #if the message sent by the server to the client notifies the user they're in the waiting list, exit program
        exit()


def userAdditionalBookingInput():

    #print statement to notify user that they can now book tickets for activities to take part of in the festival
    print("\nHere are the additional activities you can book -\n----- Baking: £8 per adult & £5 per child ----- \n----- Dancing class: £15 per adult & £10 per child ----- \n----- Craft: £10 per adult & £7.5 per child ----- \n----- Disco: £15 per adult & £11 per child")


    ## The user will now be serially asked which activities they want to book, and depending on their input, the program will either proceed to ask if they want to book the next activity (if user input is no), or ask the user to input the quantity of tickets they want to buy for a given activity ##

    bakingActivities = input("\nDo you wish to book the baking activity? (yes/no) ") #user is asked to input either yes or no
    if "yes" in bakingActivities or "Yes" in bakingActivities: #checks if the word yes was inputted by the user to proceed to booking
        bakingAdultTickets = input("Enter quantity of adult tickets: ")
        server.send(bytes(bakingAdultTickets, "utf-8")) #the quantity data is encoded and sent over to the server for final cost calculation
        bakingChildTickets = input("Enter quantity of child tickets: ")
        server.send(bytes(bakingChildTickets, "utf-8")) #the quantity data is encoded and sent over to the server for final cost calculation
    else: #temp variables initialised in order to send back a message to the server that notifies it the user booked 0 tickets for the corresponding activity
        temp1 = "0"
        temp2 = "0"
        server.send(bytes(temp1, "utf-8"))
        server.send(bytes(temp2, "utf-8")) 

    dancingActivities = input("\nDo you wish to book the dancing class activity? (yes/no) ")
    if "yes" in dancingActivities or "Yes" in dancingActivities:
        dancingAdultTickets = input("Enter quantity of adult tickets: ")  
        server.send(bytes(dancingAdultTickets, "utf-8"))
        dancingChildTickets = input("Enter quantity of child tickets: ")
        server.send(bytes(dancingChildTickets, "utf-8"))
    else:
        temp1 = "0"
        temp2 = "0"
        server.send(bytes(temp1, "utf-8"))
        server.send(bytes(temp2, "utf-8"))    

    craftActivities = input("\nDo you wish to book the craft activity? (yes/no) ")
    if "yes" in craftActivities or "Yes" in craftActivities:
        craftAdultTickets = input("Enter quantity of adult tickets: ")
        server.send(bytes(craftAdultTickets, "utf-8"))
        craftChildTickets = input("Enter quantity of child tickets: ")
        server.send(bytes(craftChildTickets, "utf-8"))
    else:
        temp1 = "0"
        temp2 = "0"
        server.send(bytes(temp1, "utf-8"))
        server.send(bytes(temp2, "utf-8"))      

    discoActivities = input("\nDo you wish to book the disco activity? (yes/no) ")
    if "yes" in discoActivities or "Yes" in discoActivities:
        discoAdultTickets = input("Enter quantity of adult tickets: ")
        server.send(bytes(discoAdultTickets, "utf-8"))
        discoChildTickets = input("Enter quantity of child tickets: ")
        server.send(bytes(discoChildTickets, "utf-8"))      
    else:
        temp1 = "0"
        temp2 = "0"
        server.send(bytes(temp1, "utf-8"))
        server.send(bytes(temp2, "utf-8"))    


def ticketCost():
    
    activitiesCostEncoded = server.recv(1024) #client recieves total activities cost (for the activities they booked) encoded data (bytes) from server
    activitiesCostDecoded = activitiesCostEncoded.decode("utf-8")
    print("\n" + activitiesCostDecoded) #byte data is decoded back into plain text and printed to screen   

    finalCostEncoded = server.recv(1024) #client recieves final cost of all booked tickets in the form of encoded data (bytes) from server
    print(finalCostEncoded.decode("utf-8")) #byte data is decoded back into plain text and printed to screen



welcomeMsg()
userBookingInput()
checkTicketValidity()
userAdditionalBookingInput()
ticketCost()