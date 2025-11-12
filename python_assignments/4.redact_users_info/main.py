"""
4.	You are having CSV file which contains name, email, phone and city information.
    As the email and phone number are sensitive, you must anonymize as below
•	Phone numbers must be masked and should display only last 4 digits. XXXXXX2341
•	Emails should be hashed. Please use SHA256
"""

import pandas as pd
import hashlib


def mask_phone(phone):
    phone = str(phone).strip()
    return "X" * (len(phone) - 4) + phone[-4:]


def hash_email(email):
    email = str(email).strip()
    return hashlib.sha256(email.encode()).hexdigest()


def process_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df["email"] = df["email"].apply(hash_email)
    df["phone"] = df["phone"].apply(mask_phone)
    df.to_csv(output_file, index=False)
    print(f"{output_file} generated")


def main():
    process_data("input.csv", "output.csv")


if __name__ == "__main__":
    main()
