# src/utils.py

def determine_column(number):
    if 1 <= number <= 12:
        return "1st"
    elif 13 <= number <= 24:
        return "2nd"
    elif 25 <= number <= 36:
        return "3rd"
    return None

def determine_dozen(number):
    if 1 <= number <= 12:
        return "1-12"
    elif 13 <= number <= 24:
        return "13-24"
    elif 25 <= number <= 36:
        return "25-36"
    return None
