def fav_num_check():
    while True:
        try:
            fav_num_divisble = []
            fav_number_input = input("Enter your favorite number: ")
            num_quant_input = input("How many nums would you like?: ")
            
            if '.' in fav_number_input or '.' in num_quant_input:
                print("You have not entered whole numbers, please try again.")
                continue
            
            fav_number = int(fav_number_input)
            num_quant = int(num_quant_input)
            
            range_list = [i for i in range(num_quant + 1)]
            for num in range_list:
                if num % fav_number == 0:
                    fav_num_divisble.append(num)
            
            return f"Your favorite number is {fav_number}.\nThe numbers divisble by your favorite number are {fav_num_divisble}"
                    
        except ValueError:
            print("Please enter a valid number!")
        except ZeroDivisionError:
            print("You cannot divide by zero buddy")

print(fav_num_check())