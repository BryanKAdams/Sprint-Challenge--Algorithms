'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    elif len(word) == 2:
        if word == "th":
            return 1
        else:
            return 0
    else:
        if word[0:2] == "th":
            return 1 + count_th(word[2:])
        elif word[1] == "t":
            return count_th(word[1:])
        else:
            return 0 + count_th(word[2:])


print(count_th("You are my best friend, don't you know that. I love you thooooo much"))
