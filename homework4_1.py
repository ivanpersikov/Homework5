
def password(b):
    return not(len(b) < 6 or b.isdigit() or b.isalpha() or "password" in b.lower() or "password" in b.upper())