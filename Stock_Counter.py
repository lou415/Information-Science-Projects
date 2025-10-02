stock  = 20
num_purchases = 0

# while num purchases is less than the stock limit.
while num_purchases < stock:
    num_purchases += 1
    if stock - num_purchases > 15:
        print("Good amount remaining")
    elif stock - num_purchases > 10:
        print("Nothing to worry about")
    elif stock - num_purchases > 5:
        print("Uhhhh, let's figure something out")
    elif stock - num_purchases > 3:
        print("Start worrying")
    elif stock - num_purchases != 0:
        print("I would order more")
    else:
        print("We are fresh out!")
    