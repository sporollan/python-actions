"""
    author: Santiago Porollan
    email: santiago.porollan@gmail.com
"""


def concatenate(words):
    """
    Receive array of words.
    Return concatenation of n char of
    each word where n is its position
    in the list.
    """

    word = ""
    for i in range(len(words)):
        word = word+words[i][i]
    return word


if __name__ == '__main__':
    words = ["yoda", "best", "has"]
    word = concatenate(words)

    # expected: 'yes'
    print(word)
