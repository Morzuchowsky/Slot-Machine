MAX_LINES = 3 

#I'm creating function that will allow user to deposit ammount of money.
def deposit_money_by_user():
    while True:
        user_balance = input("Please input ammount of money You would like to play with? :  ")
        if user_balance.isdigit():
                user_balance = int(user_balance)
                if user_balance > 0:
                    break
                else:
                    print("Please input the number that is greater than 0.")
        else:
            print("Please input the number (greater than 0) of money You would like to play with.")
    return user_balance


#I'm creathing function that will allow user to choose how many lines, she/he would like to bet.
def number_of_lines_choose_by_user():
    while True:
        user_lines = input("Please input number of lines that You would like to bet on (1-" + str(MAX_LINES) + ")? : ")
        if user_lines.isdigit():
                user_lines = int(user_lines)
                if 1 <= user_lines <= MAX_LINES:
                     break
                else:
                    print("Please input the number of lines which is one through three.")
        else:
            print("Please input the number of lines which is a number one through three.")
    return user_lines


#I'm creating main function to exectue the code.
def main():
    user_balance = deposit_money_by_user()
    user_lines = number_of_lines_choose_by_user()
    print(f"This is Your money: {user_balance} $ and this is number of lines: {user_lines} you would like to bet.")

#Calling main function
main()