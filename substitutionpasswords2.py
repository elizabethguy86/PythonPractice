CAPITALS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERS = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '1234567890'
SYMBOLS = '!@#%&~?$'
#Dictionary of lower:upper values -- shorthand to make a dictionary
LOWERS_SUBSTITUTIONS = {char: char.upper() for char in LOWERS}
CAPITALS_SUBSTITUTIONS ={char: char.lower() for char in CAPITALS}
DIGITS_SUBSTITUTIONS = {'o':'0', 'a':'4', 'e':'3', 's': '3', 'O':'0',
                            'A':'4', 'E':'3', 'S':'3', 'n': '1', 'y': '5'}
SYMBOLS_SUBSTITUTIONS = {'a':'@', 'b':'!', 'c':'#', 'd': '%', 'e':'#','f':'$', 'g':'&','h':'!','i':'!','A':'@',
                        'B':'!', 'C':'#','D':'%','E':'#','F':'$', 'G':'&', 'H':'!', 'I':'!'}
def is_valid(password):
    return(has_at_least_one_of(password,CAPITALS)and has_at_least_one_of(password,LOWERS)
        and has_at_least_one_of(password,DIGITS)and has_at_least_one_of(password,SYMBOLS))

def has_at_least_one_of(password, characters):
    for letter in password:
        if letter in characters:
            return True
    return False

def make_substitutions(password, substitution_dictionary):
    for char in password:
        if char in substitution_dictionary:
            password = password.replace(char, substitution_dictionary[char], 1)
            break
    return password

password = sys.argv[1]

def check_valid(password):
    if is_valid(password):
        print("your password {} is valid".format(password))
    else:
        password = make_substitutions(password, LOWERS_SUBSTITUTIONS)
        if is_valid(password):
            print("how about this: ", password)
            return password
        password = make_substitutions(password, CAPITALS_SUBSTITUTIONS)
        if is_valid(password):
            print("how about this: ", password)
            return password
        password = make_substitutions(password, DIGITS_SUBSTITUTIONS)
        if is_valid(password):
            print("how about this: ", password)
            return password
        password = make_substitutions(password, SYMBOLS_SUBSTITUTIONS)
        if is_valid(password):
            print("how about this: ", password)
            return password
        else:
            print("this doesn't work! How about this: ", password)
