
def main():
    msg = """
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:

    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.
    """
    print(msg)
    
    score = 0
    score += ask_positive_questions("1. I feel that I am a person of worth, at least on an equal plane with others (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_negative_questions("2. All in all, I am inclined to feel that I am a failure (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_positive_questions("3. I feel that I have a number of good qualities (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_negative_questions("4. I feel I do not have much to be proud of (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_positive_questions("5. I am able to do things as well as most other people (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_negative_questions("6. I wish I could have more respect for myself (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_positive_questions("7. I take a positive attitude toward myself (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_negative_questions("8. I certainly feel useless at times (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_positive_questions("9. On the whole, I am satisfied with myself (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    score += ask_negative_questions("10. At times I think I am no good at all (D: strongly disagree, d: disagree, a: agree, A: strongly agree): ")
    print(score)

def ask_positive_questions(statement):
    score = 0
    answer = input(f"{statement} ")
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score == 3

    return score

def ask_negative_questions(statement):
    score = 0
    answer = input(f"{statement} ")

    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score == 0

    return score


main()