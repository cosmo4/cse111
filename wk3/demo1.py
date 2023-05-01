def main():
    """
    ...
    """
    # Gather user input
    y = input("What would you like to yell? ")
    w = input("What would you like to whisper? ")
    d = input("What would you like to day dream about? ")
    # Print results to the user
    print(yell(y))
    print(whisper(w))
    print(day_dream(d))

def yell(sentence):
    """
    ...
    """
    return sentence.upper()

def whisper(sentence):
    """
    ...
    """
    return sentence.lower()

def day_dream(sentence):
    """
    ...
    """
    """
    Put asterisks around a sentence

    Parameters:
    sentence (str): The sentence surrounded by asterisks.

    Returns:
    str: Teh sentence that has been surrounded by asterisks.
    """
    return f"*{sentence}*"

main()