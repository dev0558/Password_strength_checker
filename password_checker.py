import string

# Check if the password is common
def check_common_password(password):
    try:
        with open('common-password.txt', 'r') as f:
            common = f.read().splitlines()
        if password in common:
            return True
    except FileNotFoundError:
        print("Error: 'common-password.txt' file not found.")
    return False

# Assess password strength
def password_strength(password):
    if not password.strip():  # Check if the password is empty or just whitespace
        return "Invalid", 0
    
    score = 0
    length = len(password)

    upper_case = any(c.isupper() for c in password)
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)

    characters = [upper_case, lower_case, special, digits]

    # Points for length
    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 15:
        score += 1
    if length > 20:
        score += 1

    # Points for character diversity
    score += sum(characters) - 1

    # Strength categories with refined conditions
    if score <= 2:
        return "Very Weak", score
    elif score == 3:
        return "Weak", score
    elif score == 4:
        return "Moderate", score
    elif 5 <= score <= 6:
        return "Strong", score
    else:
        return "Very Strong", score

# Provide feedback to the user
def feedback(password):
    if not password.strip():
        return "Password cannot be empty or just whitespace. Please enter a valid password."

    if check_common_password(password):
        return "Password was found in a common list. Score: 0/7\nSuggestions:\n- Avoid using commonly known passwords.\n"

    strength, score = password_strength(password)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score < 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer (more than 8 characters).\n"
        if not any(c.isupper() for c in password):
            feedback += "- Include at least one uppercase letter.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include at least one lowercase letter.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"

    return feedback

# Main program
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    print("Created by Bhargav Raj Dutta")
    print("Ensure your 'common-password.txt' file is in the same directory.")
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            password = input("Enter your password: ")
            print(feedback(password))
        elif choice == '2':
            print("Exiting the program. Stay secure!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    
  
  
