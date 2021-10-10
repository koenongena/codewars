def spin_words(sentence):
    def reverse(s):
        return s if len(s) < 5 else s[::-1]

    return " ".join([reverse(word) for word in sentence.split()])


if __name__ == '__main__':
    print(spin_words("Hey fellow warriors"))
