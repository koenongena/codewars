class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.encoding_matrix = {}
        self.decoding_matrix = {}
        # This for loop creates a lookup map for each combination of letters.
        # See https://scoop-cms.s3-eu-west-1.amazonaws.com/566e8c75ca2f3a5d5d8b45ae/2.PNG for a visual example
        for i, letter in enumerate(alphabet):
            self.encoding_matrix[letter] = dict(zip(alphabet, alphabet[i:len(alphabet)] + alphabet[0:i]))
            self.decoding_matrix[letter] = dict(zip(alphabet[i:len(alphabet)] + alphabet[0:i], alphabet))

        pass

    def encode(self, text):
        return ''.join(
            [self.encoding_matrix[letter][self.key[i % len(self.key)]]
             if letter in self.alphabet else letter
             for i, letter in enumerate(text)]
        )

    def decode(self, text):
        return ''.join(
            [
                self.decoding_matrix[self.key[i % len(self.key)]][letter]
                if letter in self.alphabet else letter
                for i, letter in enumerate(text)
            ]
        )


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)


def test_encode():
    assert c.encode('codewars') == 'rovwsoiv'
    assert c.encode('waffles') == 'laxxhsj'
    assert c.encode('CODEWARS') == 'CODEWARS'


def test_decode():
    assert c.decode('rovwsoiv') == 'codewars'
    assert c.decode('laxxhsj') == 'waffles'
    assert c.decode('CODEWARS') == 'CODEWARS'
