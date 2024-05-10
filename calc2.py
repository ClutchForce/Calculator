#Reverse Polish Notation (RPN) CALCULATOR

import csv
import datetime

class RPNCalculator:
    def __init__(self, user_name, test_case_number):
        self.user_name = user_name
        self.test_case_number = test_case_number
        self.stack = []

    def press(self, key):
        # Log each key press with a timestamp
        self.log_key_press(key)
        
        if key.isdigit():
            self.stack.append(int(key))
        elif key in '+-x/':
            if len(self.stack) < 2:
                raise ValueError("Not enough values in the stack for an operation.")
            b = self.stack.pop()
            a = self.stack.pop()
            result = self.operate(a, b, key)
            self.stack.append(result)
            return result
        elif key.lower() == 'enter':
            # For RPN, 'enter' does not immediately trigger a calculation
            return None
        else:
            raise ValueError("Invalid key pressed")

    def operate(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == 'x':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a // b  # Assuming integer division for simplicity

    def log_key_press(self, key):
        filename = f"{self.user_name}_{self.test_case_number}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), key])

def main():
    print("Welcome to the RPN Calculator.")
    print("Enter numbers and press 'enter'. Use '+', '-', 'x', '/' for operations.")
    print("Type 'exit' to quit the application.")
    
    user_name = 'calc2'
    test_case_number = 'test'
    calculator = RPNCalculator(user_name, test_case_number)

    while True:
        user_input = input("Enter a number or operation ('enter' to push number to stack): ")
        if user_input.lower() == 'exit':
            break
        elif user_input.isdigit() or user_input in '+-x/':
            try:
                result = calculator.press(user_input)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_input.lower() == 'enter':
            calculator.press('enter')
            print("Number entered.")
        else:
            print("Invalid input. Please enter a valid number or operator.")

if __name__ == "__main__":
    main()
