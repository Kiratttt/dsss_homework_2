import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range.

    Parameters
    ----------
    min_value : int
        The minimum value for the random integer.
    max_value : int
        The maximum value for the random integer.

    Returns
    -------
    int
        A random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random arithmetic operator ('+', '-', '*').

    Returns
    -------
    str
        A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def perform_operation(number1, number2, operator):
    """
    Perform the arithmetic operation based on the given operator.

    Parameters
    ----------
    number1 : int
        The first operand.
    number2 : int
        The second operand.
    operator : str
        The arithmetic operator ('+', '-', '*').

    Returns
    -------
    tuple
        A tuple containing the arithmetic expression as a string and the result of the operation.
    """
    # Create the arithmetic expression
    expression = f"{number1} {operator} {number2}"

    # Perform the operation
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2

    return expression, result

def get_user_input():
    """
    Get user input for the answer and handle invalid input.

    Returns
    -------
    int
        User's input as an integer.
    """
    while True:
        try:
            user_input = int(input("Your answer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def math_quiz():
    """
    Run the Math Quiz Game, where the user answers random arithmetic questions.

    Displays random arithmetic questions to the user and evaluates their answers,
    providing feedback and a final score at the end.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the total number of questions
    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        user_answer = get_user_input()

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
