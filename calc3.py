import csv
import datetime

class AdvancedCalculator:
    def __init__(self, user_name, test_case_number):
        self.user_name = user_name
        self.test_case_number = test_case_number
        self.expression = ""

    def press(self, key):
        # Log each key press with a timestamp
        self.log_key_press(key)
        
        # Ensure multiplication uses the correct symbol for eval
        if key.isdigit() or key in '+-x/()=' or key in '()':
            corrected_key = key.replace('x', '*')  # Replace 'x' with '*' for multiplication
            self.expression += corrected_key
        elif key.lower() == 'c':  # Clear the expression
            self.expression = ""
        else:
            raise ValueError("Invalid key pressed")

    def calculate(self):
        try:
            # Evaluate the mathematical expression safely
            result = eval(self.expression)
            self.expression = str(result)  # Reset expression to the result for continuity in calculations
            return result
        except Exception as e:
            self.expression = ""  # Reset the expression on error
            raise ValueError(f"Error in calculation: {e}")

    def log_key_press(self, key):
        filename = f"{self.user_name}_{self.test_case_number}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), key])

def main():
    print("Welcome to the Advanced Calculator.")
    print("This calculator supports +, -, x, /, (), and order of operations.")
    print("Enter your calculation and press '=' to compute.")
    print("Type 'exit' to quit the application.")
    
    user_name = 'calc3'
    test_case_number = 'test'
    calculator = AdvancedCalculator(user_name, test_case_number)

    while True:
        user_input = input("Enter an operation or '=' to calculate (type 'C' to clear): ")
        if user_input.lower() == 'exit':
            break
        elif user_input == '=':
            try:
                result = calculator.calculate()
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        elif user_input.isdigit() or user_input in '+-x/()=' or user_input in '()C':
            calculator.press(user_input)
        else:
            print("Invalid input. Please enter a valid number, operator, or '=' to calculate.")

if __name__ == "__main__":
    main()
