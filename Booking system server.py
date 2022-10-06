#run server first
import socket #TCP socket module used to establish the connection between server and client (https://realpython.com/python-sockets/)
import random #random module used to generate a random integer

IP = "127.0.0.1"
HOST = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialise server instance 
server.bind((IP, HOST)) #bind
server.listen(1) #listens to and allows connection with 1 client at a time

while True:

    client, address = server.accept() #accept client connection with IP address and client socket
    print(f"Connection from {address} has been established.")
        
    def applyDiscount(price, ticket, name): 
        # apply 10% discount if the total price of tickets exceeds £500
        if price > 500:
            price = price - (price * 0.1) 
            client.send(bytes(name + ", the cost of your " + ticket + " tickets is " + "£" + str(price) + ". " + "You've been given a 10% discount for spending over £500.", "utf-8")) #encoded message returned to user letting them know the cost of their tickets after the discount has been applied
        else: #otherwise, do not apply discount and return to the user the cost of their tickets in an encoded message from the server to client
            client.send(bytes(name + ", the cost of your " + ticket + " tickets is " + "£" + str(price) + ".", "utf-8"))


    def ticketsQuantity():
        #variables that store quantity of each ticket type which is randomly generated
        saturdayTickets = random.randint(0, 25)
        vipTickets = random.randint(0, 20)
        sundayTickets = random.randint(0, 50)
        weekendTickets = random.randint(0, 20)

        return saturdayTickets, vipTickets, sundayTickets, weekendTickets

    
    def userInputEvaluation():

        ticketsQuantity()

        saturdayTickets, vipTickets, sundayTickets, weekendTickets = ticketsQuantity()
    
        nameEncoded = client.recv(1024) #server recieves enconded name data from client, 1024 refers to the bytes of data the server receives
        nameTxt = nameEncoded.decode("utf-8") #server decodes name back to plain text

        ticketTypeEncoded = client.recv(1024) #server recieves tickets enconded data from client, 1024 refers to the bytes of data the server receives
        ticketTypeTxt = ticketTypeEncoded.decode("utf-8").upper() #server decodes tickets back to plain text

        adultTicketsEncoded = client.recv(1024) #server recieves adult tickets enconded data from client, 1024 refers to the bytes of data the server receives
        adultTicketsTxt = adultTicketsEncoded.decode("utf-8") #server decodes data back to plain text
        adultTicketsInt = int(adultTicketsTxt) #converts plain text to integer for arithmetic processing

        childTicketsEncoded = client.recv(1024) #server recieves child tickets enconded data from client, 1024 refers to the bytes of data the server receives
        childTicketsTxt = childTicketsEncoded.decode("utf-8") #server decodes data back to plain text
        childTicketsInt = int(childTicketsTxt) #converts plain text to integer for arithmetic processing


        #the following if statements check if the ticket type input is valid, and given that it is, it will then check what type of ticket was booked to see if its available, and if it is, the cost of the ticket(s) is calculated ##

        if ticketTypeTxt == "SATURDAY" or ticketTypeTxt == "VIP" or ticketTypeTxt == "SUNDAY" or ticketTypeTxt == "WEEKEND":
            #if client inputted saturday
            if ticketTypeTxt == "SATURDAY":
                if saturdayTickets == 0 or (adultTicketsInt + childTicketsInt) > saturdayTickets: #if client is ordering more tickets than there are availaible
                    client.send(bytes(nameTxt + ", SATURDAY tickets are currently sold out, so you've been put in a waiting list.", "utf-8")) #send to client an encoded message to let them know they're in a waiting list 
                else: #otherwise calculate cost of ticket prices based on how many tickets the client wants to book
                    adultPrice = adultTicketsInt * 25 #one saturday adult ticket costs £25
                    childPrice = childTicketsInt * 20 #one saturday child ticket costs £20
                    totalPrice = adultPrice + childPrice #final sum
                    applyDiscount(totalPrice, ticketTypeTxt, nameTxt)
        
            elif ticketTypeTxt == "VIP":
                if vipTickets == 0 or (adultTicketsInt + childTicketsInt) > vipTickets:    
                    client.send(bytes(nameTxt + ", VIP tickets are currently sold out, so you've been put in a waiting list.", "utf-8"))
                else:
                    adultPrice = adultTicketsInt * 50
                    childPrice = childTicketsInt * 25
                    totalPrice = adultPrice + childPrice
                    applyDiscount(totalPrice, ticketTypeTxt, nameTxt)

            elif ticketTypeTxt == "SUNDAY":
                if sundayTickets == 0 or (adultTicketsInt + childTicketsInt) > sundayTickets:    
                    client.send(bytes(nameTxt + ", SUNDAY tickets are currently sold out, so you've been put in a waiting list.", "utf-8"))
                else:
                    adultPrice = adultTicketsInt * 10
                    childPrice = childTicketsInt * 7.5
                    totalPrice = adultPrice + childPrice
                    applyDiscount(totalPrice, ticketTypeTxt, nameTxt) 

            elif ticketTypeTxt == "WEEKEND":
                if weekendTickets == 0 or (adultTicketsInt + childTicketsInt) > weekendTickets:    
                    client.send(bytes(nameTxt + ", WEEKEND tickets are currently sold out, so you've been put in a waiting list.", "utf-8"))
                else:
                    adultPrice = adultTicketsInt * 30
                    childPrice = childTicketsInt * 22
                    totalPrice = adultPrice + childPrice
                    applyDiscount(totalPrice, ticketTypeTxt, nameTxt)       
        else:
            client.send(bytes("Sorry, you have entered an invalid ticket type.", "utf-8")) #return error message if the ticket type is invalid


        return totalPrice    


    
    def additionalActivitiesInput():
    ## server recieving (and decoding) client messages regarding additional activities' ticket info ##

        bakingAdultTicketsEncoded = client.recv(1024) #server recieves enconded data from client, 1024 refers to the bytes of data the server receives
        bakingAdultTicketsTxt = bakingAdultTicketsEncoded.decode("utf-8") #server decodes data back to plain text    
        bakingAdultTicketsInt = int(bakingAdultTicketsTxt) #converts plain text to integer for arithmetic processing
        bakingChildTicketsEncoded = client.recv(1024) #server recieves enconded data from client, 1024 refers to the bytes of data the server receives
        bakingChildTicketsTxt = bakingChildTicketsEncoded.decode("utf-8") #server decodes data back to plain text 
        bakingChildTicketsInt = int(bakingChildTicketsTxt) #converts plain text to integer for arithmetic processing

        dancingAdultTicketsEncoded = client.recv(1024) 
        dancingAdultTicketsTxt = dancingAdultTicketsEncoded.decode("utf-8") 
        dancingAdultTicketsInt = int(dancingAdultTicketsTxt)
        dancingChildTicketsEncoded = client.recv(1024) 
        dancingChildTicketsTxt = dancingChildTicketsEncoded.decode("utf-8")
        dancingChildTicketsInt = int(dancingChildTicketsTxt)

        craftAdultTicketsEncoded = client.recv(1024) 
        craftAdultTicketsTxt = craftAdultTicketsEncoded.decode("utf-8") 
        craftAdultTicketsInt = int(craftAdultTicketsTxt)
        craftChildTicketsEncoded = client.recv(1024) 
        craftChildTicketsTxt = craftChildTicketsEncoded.decode("utf-8") 
        craftChildTicketsInt = int(craftChildTicketsTxt)

        discoAdultTicketsEncoded = client.recv(1024) 
        discoAdultTicketsTxt = discoAdultTicketsEncoded.decode("utf-8") 
        discoAdultTicketsInt = int(discoAdultTicketsTxt)
        discoChildTicketsEncoded = client.recv(1024) 
        discoChildTicketsTxt = discoChildTicketsEncoded.decode("utf-8") 
        discoChildTicketsInt = int(discoChildTicketsTxt)

        return bakingAdultTicketsInt, bakingChildTicketsInt, dancingAdultTicketsInt, dancingChildTicketsInt, craftAdultTicketsInt, craftChildTicketsInt, discoAdultTicketsInt, discoChildTicketsInt


    
    def calculatePrice():
    ## server calculates total price of additional activities' tickets that the user requested ##

        bakingAdultTicketsInt, bakingChildTicketsInt, dancingAdultTicketsInt, dancingChildTicketsInt, craftAdultTicketsInt, craftChildTicketsInt, discoAdultTicketsInt, discoChildTicketsInt = additionalActivitiesInput()
        totalPrice = userInputEvaluation()

        if True:

            adultBakingPrice = bakingAdultTicketsInt * 8
            childBakingPrice = bakingChildTicketsInt * 5
            totalBakingPrice = adultBakingPrice + childBakingPrice

            adultDancingPrice = dancingAdultTicketsInt * 15
            childDancingPrice = dancingChildTicketsInt * 10
            totalDancingPrice = adultDancingPrice + childDancingPrice

            adultCraftPrice = craftAdultTicketsInt * 15
            childCraftPrice = craftChildTicketsInt * 10
            totalCraftPrice = adultCraftPrice + childCraftPrice

            adultDiscoPrice = discoAdultTicketsInt * 15
            childDiscoPrice = discoChildTicketsInt * 10
            totalDiscoPrice = adultDiscoPrice + childDiscoPrice

            totalEventsPrice = totalBakingPrice + totalDancingPrice + totalCraftPrice + totalDiscoPrice
            finalPrice = totalPrice + totalEventsPrice

            client.send(bytes("The cost of your additional activities' ticket(s) is " + "£" + str(totalEventsPrice) + ".", "utf-8")) #the cost of the activities tickets is returned to client in encoded message

            client.send(bytes("The final cost of your tickets is " + "£" + str(finalPrice) + ".", "utf-8")) #the final cost of the festival tickets and additional activities tickets is calculated and returned to client in encoded message


    userInputEvaluation()
    additionalActivitiesInput()
    calculatePrice()
    
    
    client.close() #client closes connection