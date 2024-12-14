#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def check_password_strength(password: str) -> str:
    """
    Assess the strength of a given password.

    Parameters:
        password (str): The password to be analyzed.

    Returns:
        str: Feedback on password strength (e.g., Weak, Moderate, Strong).
    """
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check for common patterns or weaknesses
    common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "111111"]
    unique_criteria = password not in common_passwords

    # Count how many criteria are met
    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria,
        unique_criteria
    ])

    # Provide feedback based on criteria met
    if criteria_met <= 2:
        return "Weak: Consider making your password longer and adding uppercase letters, digits, and special characters."
    elif criteria_met <= 4:
        return "Moderate: Your password is decent but could be improved by adding more unique elements."
    else:
        return "Strong: Your password is strong."

if __name__ == "__main__":
    print("Password Strength Checker")
    print("Enter 'exit' to quit.")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "exit":
            break
        feedback = check_password_strength(password)
        print(f"Password Strength: {feedback}\n")


# In[ ]:




