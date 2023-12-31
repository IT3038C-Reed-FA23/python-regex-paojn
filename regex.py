import re

# Part 1: Extract Email Addresses
def extract_emails(text):
    email_regex = r"(?:(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,253}[a-zA-Z0-9])@(?:(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]{0,253}[a-zA-Z0-9])\.[a-zA-Z]{2,}))"
    return re.findall(email_regex, text)
    # Use re.findall() to find all email addresses and return them as a list.
    email_addresses = re.findall(email_pattern, text)
    return re.findall(email_regex, text)
    # An email consists of these parts: username, @ symbol, domain name, top-level domain (TLD) (e.x. user@domain.tld)
    # Email rules:
      # 1. Username consists of alphanumeric characters, ., _, %, +, and -
      # 2. Usernames cannot start or end with a special character (. _ % + -)
      # 3. Domain name consists of alphanumeric characters, ., and -
      # 4. Domain name cannot start or end with a special character (. -)
      # 5. TLD consists of lowercase alphabetic characters and has a length of 2 or more
      # 6. The @ symbol separates the username and the domain name
      # 7. The . separates the domain name and the top-level domain (TLD)
      # 8. The regular expression should match the entire email address
    email_addresses = extract_emails(sample_text)
    print("Email Addresses:", email_addresses)
    pass

# Part 2: Validate Phone Numbers
def validate_phone_numbers(phone_numbers):
    valid_numbers = []
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    for number in phone_numbers:
        if re.match(phone_pattern, number):
            valid_numbers.append(number)

    return valid_numbers
    # Use re.match() to check if each phone number is valid and return a list of valid phone numbers.
    pass

# Part 3: Find Dates
def find_dates(text):
    date_pattern = r'\d{2}/\d{2}/\d{4}'
    # Use re.finditer() to find all date occurrences and return them as a list.
    date_occurrences = list(re.finditer(date_pattern, text))
    return date_occurrences
    pass

# Part 4: Replace Names
def format_phone_numbers(text):
    # TODO: Write a regex pattern to find phone numbers and replace them with format (xxx) xxx-xxxx
    pattern = r'(\d{3})[-.\s]?(\d{3})[-.\s]?(\d{4})'
    phone_format = r'(\1) \2-\3'
    # Use re.sub() to perform the substitution and return the modified text.
    formatted_text = re.sub(pattern, phone_format, text)
    return formatted_text
    pass

# Testing your functions
if __name__ == "__main__":
    sample_text = """
    John Doe's email is john@example.com, and he has two phone numbers: 123-456-7890 and 987-654-3210.
    Some important dates are 01/25/2023 and 12/31/2023.
    """

    # Test Part 1: Extract Email Addresses
    email_addresses = extract_emails(sample_text)
    print("Email Addresses:", email_addresses)

    # Test Part 2: Validate Phone Numbers
    phone_numbers = ["123-456-7890", "987-654-3210", "555-5555", "1-800-123-4567"]
    valid_numbers = validate_phone_numbers(phone_numbers)
    print("Valid Phone Numbers:", valid_numbers)

    # Test Part 3: Find Dates
    date_occurrences = find_dates(sample_text)
    print("Date Occurrences:", [match.group() for match in date_occurrences])

    # Test Part 4: Format Phone Numbers
    formatted_text = format_phone_numbers(sample_text)
    print("Formatted Text:")
    print(formatted_text)
