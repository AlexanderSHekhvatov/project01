# Пункт A
def remove_exclamation_marks(s):
    return s.replace("!", "")


# Пункт B
def remove_last_em(s):
    if len(s) > 0 and s[-1] == "!":
        return s[:-1]
    return s


# Пункт C
def remove_word_with_one_em(s):
    words = s.split()
    filtered_words = [word for word in words if word.count("!") != 1]
    return " ".join(filtered_words)
