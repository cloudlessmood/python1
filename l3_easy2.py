def lucky_ticket(ticket):
    
    first = int(ticket[0])+int(ticket[1])+int(ticket[2])
    second = int(ticket[3])+int(ticket[4])+int(ticket[5])
    
    if first == second:
        text = "Your ticket is lucky"
    else:
        text = "You ticket is unlucky"
    return(text)

ticket = input("Write number of the ticket which includes 6 values: ")
print(lucky_ticket(ticket))