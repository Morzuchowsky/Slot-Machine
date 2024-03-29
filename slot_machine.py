import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Function that calculates the total winnings for a given slot machine spin result
def check_win(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        line_symbol = columns[0][line]
        for column in columns:
            current_symbol = column[line]
            if line_symbol != current_symbol:
                break
        else:
            winnings += values[line_symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


# Function to simulate the spinning of a slot machine.
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


# Function that prints the result of a slot machine spin in a formatted manner.
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


# Function to allow users to deposit an amount of money.
def deposit_money_by_user():
    while True:
        bet_amount = input("Please input the amount of money you'd like to play with (greater than 0): ")
        try:
            bet_amount = float(bet_amount)
            if bet_amount > 0:
                break
            else:
                print("Amount should be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    return bet_amount


# Function to allow users to choose the number of betting lines.
def number_of_lines_chosen_by_user():
    while True:
        chosen_lines = input(f"Please input number of lines you'd like to bet on (1-{MAX_LINES}): ")

        if chosen_lines.isdigit():
            chosen_lines = int(chosen_lines)
            if 1 <= chosen_lines <= MAX_LINES:
                break
            else:
                print(f"Please input a number between 1 and {MAX_LINES}.")
        else:
            print(f"Please input a valid number between 1 and {MAX_LINES}.")
    return chosen_lines


# Function to allow users to place a bet for each line.
def get_bet():
    while True:
        bet_amount = input("What amount of money You would like to bet on each line?: $")
        try:
            bet_amount = float(bet_amount)
            if MIN_BET < bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        except ValueError:
            print("Please enter a valid number.")
    return bet_amount


# Function to check if the user has sufficient funds to place the desired bet.
def can_place_bet(bet, lines, amount):
    total_bet = bet * lines
    if total_bet > amount:
        print(f"You do not have enough money to bet that amount. Your current balance is: ${amount}")
        return False
    return True


def game(amount):
    user_lines = number_of_lines_chosen_by_user()
    while True:
        bet = get_bet()
        if can_place_bet(bet, user_lines, amount):
            break
    total_bet = bet * user_lines
    print(f"Your balance: {amount} $. You chose to bet on {user_lines} lines.")
    print(f"You are betting {bet} $ on {user_lines} lines. Total bet is equal to: {total_bet} $")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_win(slots, user_lines, bet, symbol_values)
    print(f"You won ${winnings}")
    if winning_lines:
        print(f"You won on", *winning_lines)
    else:
        print("Better luck next time!")
    print_slot_machine(slots)
    return winnings - total_bet


def main():
    amount = deposit_money_by_user()
    while True:
        print(f"Current balance is: ${amount}")
        if amount <= 0:  # Sprawdzenie czy saldo wynosi 0
            print("You lost everything!")
            break  # Wyjście z pętli
        answer = input("Please press enter to play or type q to quit: ")
        if answer == "q":
            break
        amount += game(amount)

    print(f"You left with ${amount}")


main()
