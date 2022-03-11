def minion_game(string):
    # your code goes here
    stuat, kevin = 0, 0
    vowels = 'AEIOU'

    cur_non_vowel, cur_vowel = 0, 0

    for l in range(len(string)):
        if string[l] not in vowels:
            cur_non_vowel += 1
        else:
            cur_vowel += 1
        stuat += cur_non_vowel
        kevin += cur_vowel

    return '{} {}'.format('Stuart', stuat) if stuat >= kevin else '{} {}'.format('Kevin', kevin)


s = 'BANANA'
print(minion_game(s))
