"""
3.	You have millions of emails which are with duplicates also.
You must remove the duplicate emails.
Please preserve the original order of the appearance of the email.
"""

import pandas as pd


def remove_duplicate_emails(emails):
    seen = set()
    unique_emails = []
    for email in emails:
        if email not in seen:
            seen.add(email)
            unique_emails.append(email)
    return unique_emails


def process_emails(input_file, output_file):
    df = pd.read_csv(input_file)
    if "email" not in df.columns:
        raise ValueError("Input file must contain 'email' column")
    unique_emails = remove_duplicate_emails(df["email"].tolist())
    pd.DataFrame({"email": unique_emails}).to_csv(output_file, index=False)
    print(f"{output_file} generated")


def main():
    process_emails("input.csv", "output.csv")


if __name__ == "__main__":
    main()
