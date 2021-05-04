valid_domains = ("com", "net", "bg", "org")

class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

def validate_email(email):

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.split(".")[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")



while True:
    email = input()

    if email == "End":
        break
    validate_email(email)