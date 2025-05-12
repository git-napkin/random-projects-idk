import random
import string

def generate_code():
    """10 chances at gambling a free robux gift card!! yipee"""
    chars = string.ascii_uppercase + string.digits
    
    groups = []
    for _ in range(4):
        group = ''.join(random.choice(chars) for _ in range(4))
        groups.append(group)
    
    return '-'.join(groups)

def main():
    """alright guys here we go"""
    print("here you go kid:")
    # btw to change the amount outputted just change the number in range() to whatever you want (10 outputs 10 codes, 50 outputs 50 codes, etc.)
    for i in range(10):
        print(f"{i+1}. {generate_code()}")

if __name__ == "__main__":
    main()