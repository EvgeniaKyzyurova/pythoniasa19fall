"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""
def poem():



    res = ''
    p = [["the house that Jack built", "lay in"],
            ["the malt", "ate"],
            ["the rat", "killed"],
            ["the cat", 'worried'],
            ["the dog", "tossed"],
            ["the cow with the crumpled horn", "milked"],
            ["the maiden all forlorn", "kissed"],
            ["the man all tattered and torn", 'married'],
            ["the priest all shaven and shorn", "waked"],
            ["the cock that crowed in the morn", "kept"],
            ["the farmer sowing his corn", 'is']]

    for i in range(len(p)):
        for j in range(i, 0, -1):
            if j == i:
                res += f'This is {p[j][0]}'
            else:
                res += f'That {p[j][1]} {p[j][0]}'
            res += ',\n' if j > 1 else '\n'
        res += f'This is {p[i][i]}.\n\n' if i == 0 else f'That {p[0][1]} {p[0][0]}.\n\n'
    return res[:-1]





if __name__ == '__main__':
    import doctest
    doctest.testmod()

#print(poem())