

Password Strength Checker

This Python-based Password Strength Checker tool evaluates the strength of passwords and helps users improve their password security by providing actionable feedback. The tool checks the password against several criteria, such as length, character variety (uppercase, lowercase, digits, special characters), and whether it matches commonly used passwords.

Features:
- **Password Strength Evaluation**: Checks password strength based on length, character diversity, and common password lists.
- **Common Password Check**: Verifies whether the entered password is commonly used or weak (based on a `common-password.txt` file).
- **Feedback System**: Provides suggestions to improve weak passwords, such as adding uppercase letters, digits, and special characters.
- **Password Strength Categories**: Classifies passwords into strength levels: **Very Weak**, **Weak**, **Moderate**, **Strong**, and **Very Strong**.

How It Works:
1. The user inputs a password.
2. The program checks its length and character diversity (uppercase, lowercase, digits, and special characters).
3. The password is compared against a list of commonly used passwords stored in a `common-password.txt` file.
4. Based on the evaluation, the program assigns a strength score (from 1 to 7) and categorizes the password into one of the following: Very Weak, Weak, Moderate, Strong, or Very Strong
5. The program then provides feedback and suggestions for improving weak passwords.

Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dev0558/Password_strength_checker.git
   ```
2. Install Python 3.x if not already installed.
3. Ensure you have the `common-password.txt` file in the same directory as the Python script.

Usage:
1. Run the `password_checker.py` script.
2. Input a password when prompted.
3. The program will evaluate the password's strength and provide feedback.

Contributing
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m "Add new feature"`).
- Push to your forked repository (`git push origin feature-branch`).
- Create a pull request with your proposed changes.

License:
This project is licensed under the MIT License.



Technologies Used:
- Python 3.x
- Git/GitHub

