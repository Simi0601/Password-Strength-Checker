#This project aims to create a Password Strength Checker that evaluates the strength of a given password based on various criteria, such as length, use of uppercase and lowercase letters, numbers, and special characters. The program will provide feedback on how to improve the password strength.
import re

def check_length(password):
    """Check if the password length is at least 8 characters."""
    return len(password) >= 8

def check_uppercase(password):
    """Check if the password contains at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def check_lowercase(password):
    """Check if the password contains at least one lowercase letter."""
    return bool(re.search(r'[a-z]', password))

def check_digit(password):
    """Check if the password contains at least one digit."""
    return bool(re.search(r'\d', password))

def check_special_char(password):
    """Check if the password contains at least one special character."""
    return bool(re.search(r'[@$!%*?&#]', password))

def check_password_strength(password):
    """Evaluate the password strength based on various criteria."""
    score = 0
    feedback = []
    
    if check_length(password):
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if check_uppercase(password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if check_lowercase(password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if check_digit(password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    if check_special_char(password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    strength = "Weak"
    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    
    return strength, feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions for improving your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
