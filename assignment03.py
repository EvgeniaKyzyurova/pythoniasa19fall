
def task01(start, end, func):
    print(','.join(str(i) for i in range(start, end + 1) if func(i) ))
task01(2000, 3200, lambda i:i % 7 == 0 and i % 5 != 0)


def task02(x,y):
    return [ [i*j for j in range (y)] for i in range (x)]
print(task02(3,5))

def task03(password):
    """
        >>> task03('ABd1234@1')
        True
        >>> task03('a F1#')
        False
        >>> task03('2w3E*')
        False
        >>> task03('2We3345')
        False
    """

    return (6 <= len(password) <= 12
          and any('a' <= s <= 'z' for s in password)
          and any('A' <= s <= 'Z' for s in password)
          and any('0' <= s <= '9' for s in password)
          and any(s in '$#@' for s in password))

if __name__ == '__main__':
    import doctest
    doctest.testmod()



import string
import random

def task05(passw):
   return (6 <= len(passw) <= 12
          and any('a' <= s <= 'z' for s in passw)
          and any('A' <= s <= 'Z' for s in passw)
          and any('0' <= s <= '9' for s in passw)
          and any(s in '#$@' for s in passw))


def passwo_gen():
    characters = string.ascii_letters + string.digits + '$#@'
    passwor =  "".join(random.choice(characters) for x in range(random.randint(8, 16)))
    if task05(passwor)==True:
        return passwor
    else:
        return False



if __name__ == '__main__':
    while True:
        p = passwo_gen()
        if p!=False:
            break
    print(p)



