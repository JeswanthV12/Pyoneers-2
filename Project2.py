import random, string

dig1 = random.choice(string.digits)
dig2 = random.choice(string.ascii_lowercase)
dig3 = random.choice(string.digits)
dig4 = random.choice(string.ascii_uppercase)

print(f"Password: {dig1}{dig2}{dig3}{dig4}")