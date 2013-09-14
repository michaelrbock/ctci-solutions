def all_unique(s):
    letters = {} # dict to hold if letter has been seen {char : bool}
    for c in s:
        if c in letters:
            return False
        else:
            letters[c] = True
    return True

def all_unique_no_xtra_space(s):
    for i, c in enumerate(s):
        for j, d in enumerate(s):
            if i == j: # don't compare the same letter
                continue
            else:
                if c == d:
                    return False
    return True