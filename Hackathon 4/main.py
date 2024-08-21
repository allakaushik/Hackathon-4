import re
import random
import string


def validate_password(password):

    if (
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    ):
        return True
    return False


def validate_pattern(password_pattern):

    valid_patterns = ["1235", "7896", "4569"]
    if password_pattern in valid_patterns:
        return True
    return False


def generate_captcha():
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.choice(letters) for _ in range(6))
    return captcha


def verify_captcha(input_captcha, generated_captcha):
    if input_captcha == generated_captcha:
        return True
    return False


def three_level_password_system():
    print("Welcome to the Three-Level Password System")

    password = input("Enter your password: ")
    if not validate_password(password):
        print(
            "Invalid Password. Must be at least 8 characters long, include uppercase, lowercase, digits, and special characters."
        )
        return

    print("\nEnter your pattern based password (Example: 1235 for a 3x3 grid)")
    password_pattern = input("Enter pattern password: ")
    if not validate_pattern(password_pattern):
        print("Invalid Pattern Password.")
        return

    generated_captcha = generate_captcha()
    print(f"\nCAPTCHA: {generated_captcha}")
    input_captcha = input("Enter the CAPTCHA: ")
    if not verify_captcha(input_captcha, generated_captcha):
        print("CAPTCHA Verification Failed.")
        return

    print("Access Granted. All security levels passed!")


three_level_password_system()
