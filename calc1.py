import csv
import datetime

# Define the calculator class
class SimpleCalculator:
    def __init__(self, user_name, test_case_number):
        self.user_name = user_name
        self.test_case_number = test_case_number
        self.reset()

    def reset(self):
        self.current_value = ""
        self.operations = []

    def press(self, key):
        # Log each key press with a timestamp
        self.log_key_press(key)
        
        if key in '0123456789':
            self.current_value += key
        elif key in '+-x/':
            if self.current_value:
                self.operations.append(self.current_value)
                self.current_value = ""
            self.operations.append(key)
        elif key == '=':
            if self.current_value:
                self.operations.append(self.current_value)
            return self.calculate()
        else:
            raise ValueError("Invalid key pressed")

    def calculate(self):
        result = int(self.operations[0])
        for i in range(1, len(self.operations) - 1, 2):
            next_value = int(self.operations[i + 1])
            if self.operations[i] == '+':
                result += next_value
            elif self.operations[i] == '-':
                result -= next_value
            elif self.operations[i] == 'x':
                result *= next_value
            elif self.operations[i] == '/':
                result //= next_value
        self.reset()
        return result

    def log_key_press(self, key):
        filename = f"{self.user_name}_{self.test_case_number}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), key])

def main():
    print("Welcome to the Simple Calculator.")
    print("You can use this calculator by typing numbers (0-9) and operators (+, -, x, /).")
    print("To perform a calculation, end your input with '='.")
    print("Type 'exit' to quit the application.")
    
    user_name = "calc1"
    test_case = "test"
    calculator = SimpleCalculator(user_name, test_case)

    while True:
        user_input = input("Enter a number, operator, or '=' to calculate: ")
        if user_input.lower() == 'exit':
            break
        elif user_input in '0123456789+-x/=':
            try:
                result = calculator.press(user_input)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please enter a valid number or operator.")

if __name__ == "__main__":
    main()
