def calculate_expression():
    user_input = input("Enter a mathematical expression: ")
    try:
        # !!! SECURITY ISSUE: Using eval() directly on user input !!!
        result = eval(user_input)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculate_expression()
