import re
import tkinter as tk
from tkinter import messagebox

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

def on_check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")
    feedback_text = "\n".join(feedback)
    feedback_label.config(text=f"Suggestions for improving your password:\n{feedback_text}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the password entry field
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

# Create and place the check button
check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Create and place the feedback label
feedback_label = tk.Label(root, text="", justify=tk.LEFT)
feedback_label.pack(pady=5)

# Run the application
root.mainloop()
