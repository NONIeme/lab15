import string

def clean_data(data):
    cleaned = list(map(lambda x: x.strip().lower(), data.split(',')))
    return cleaned

def filter_emails(emails):
    def is_valid_email(email):
        return email.count('@') == 1
    valid_emails = list(filter(is_valid_email, emails.split()))
    return valid_emails

def extract_keywords(words, length):
    filtered_words = list(filter(lambda x: len(x) > length, words.split()))
    return filtered_words

def process_text(text):
    cleaned = list(map(lambda x: x.strip(string.punctuation).strip().lower(), text.split()))
    filtered = list(filter(lambda x: len(x) > 2, cleaned))
    return filtered

def normalize_data(numbers):
    num_list = list(map(float, numbers.split(',')))
    max_num = max(num_list)
    normalized = [num / max_num for num in num_list]
    return normalized

def concatenate_strings(data, separator):
    concatenated = ''.join(data.split(separator))
    return concatenated

def sum_numeric_strings(numbers):
    total_sum = sum(map(float, numbers.split(',')))
    return total_sum

def filter_numbers(numbers, threshold):
    filtered = list(filter(lambda x: float(x) <= threshold, numbers.split(',')))
    return list(map(float, filtered))

def map_to_squares(numbers):
    squared_numbers = list(map(lambda x: int(x) ** 2, numbers.split(',')))
    return squared_numbers

def reverse_strings(words):
    reversed_words = list(map(lambda x: x[::-1], words.split(',')))
    return reversed_words
