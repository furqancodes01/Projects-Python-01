class WeakPassworkError(Exception):
    pass

def is_strong(password):
    msg = 'Password must contain at least'
    if len(password) < 8:
        return False , msg + " 8 characters"    
    
    has_upper =  any(c.isupper() for c in password)
    has_lower =  any(c.islower() for c in password)
    has_digit =  any(c.isdigit() for c in password)
    special_char = set("!@#$%^*()_+")
    has_special = any(c in special_char for c in password)
    
    if not has_upper:
        raise WeakPassworkError(msg + "One uppercase letter")
    if not has_lower:
        raise WeakPassworkError(msg + "One lowercase letter")
    if not has_digit:
        raise WeakPassworkError(msg + "One digit")
    if not has_special:
        raise WeakPassworkError(msg + "One special character (!@#$%^&*()_+)")
    
    return True, "!!!Password is Strong!!!"

password = input("Enter the password: ")
try:
    valid, message = is_strong(password)
    print(message)
except WeakPassworkError as e:
        print(e)    