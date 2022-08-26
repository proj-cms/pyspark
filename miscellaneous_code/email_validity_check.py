import re


def check_email_validity(email):
    # print (email, end = "\n")
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    pat2 = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,2}\.[a-z]{1,2}$"
    if re.match(pat, email) or re.match(pat2, email):
        if len(email[0:email.index('@')]) <= 20:
            return True
        else:
            return False
    else:
        return False


def check(emails):
    """
    input:
    emails -> list of emails to check

    output:
    verified_lex -> the verified list of emails, in lexicographical order
    """

    verified_lex = None

    # Your code starts here
    verified_lex = sorted(list(filter(lambda email: check_email_validity(email), emails)))
    # Your code ends here
    return verified_lex


if __name__ == "__main__":
    emails = ['www.google.co.in', 'yeagerist@google.co.in', 'eren_voldig_yeager@gmail@rediffmail.com']
    print(check(emails))
