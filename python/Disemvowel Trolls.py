import re
def disemvowel(string_):
    return re.sub(r"[aeoiu]", "", string_, flags=re.IGNORECASE)

if __name__ == '__main__':
    print(disemvowel('This website is for losers LOL!'))
