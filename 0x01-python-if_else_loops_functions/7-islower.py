#!/usr/bin/python3
# Function that checks for lowercase charactors

def islower(c):
    """Checks for lowercase charactors."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
