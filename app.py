from random import shuffle


def generate_user_name(name: str) -> str:
    #splitting the string into a list of chars
    unique_letters = list(set(name))

    # shuffle letters
    shuffle(unique_letters)

    # join letters into a string
    nick_name = "".join(unique_letters)

    #limit to seven letters
    nick_name = nick_name[0:8]

    return nick_name
