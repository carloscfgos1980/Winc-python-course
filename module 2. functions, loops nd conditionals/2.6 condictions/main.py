def eligible_to_vote(age, nationality):
    if age >= 18:
        return True
    else:
        return False

# not recommended


def eligible_to_vote(age, nationality):
    if age >= 18:
        if nationality == 'Italian':
            return True
        else:
            return False
    else:
        return False

# recommended:


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    else:
        return False

# even better


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    return False

# elif


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    elif age >= 25 and nationality == 'Portuguese':
        return True
    else:
        return False


def eligible_to_vote_more(age, nationality):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19 and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False


print(eligible_to_vote_more(25, 'Italian'), eligible_to_vote_more(37, 'Dutch'))
'''
Why are we able to leave out else here? Recall that a function does not proceed in executing its code after hitting a return statement, it immediately returns whatever we asked it to return.
'''
