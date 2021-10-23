import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    word_list = []
    with open(file_name) as f:
        for line in f:
            word_list.append(line.strip())
    print('  ', len(word_list), 'words loaded.')
    return word_list

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    with open("story.txt", "r") as f:
        story = str(f.read())
    return story

WORDLIST_FILENAME = '../words.txt'

class Message(object):

    _valid_words = load_words(WORDLIST_FILENAME)

    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text

    @property
    def valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self._valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        shift_dict = {}
        for letter in string.ascii_letters:
            shifted = ord(letter) + shift
            if shifted > ord('z') or shifted > ord('Z') and letter.isupper():
                shift_dict[letter] = chr(shifted - 26)
            else:
                shift_dict[letter] = chr(shifted)
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shifted = ""
        shift_dict = self.build_shift_dict(shift)
        for char in self.message_text:
            if char in string.ascii_letters:
                shifted += shift_dict[char]
            else:
                shifted += char
        return shifted

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        super().__init__(text)
        self._shift = shift
        self._encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(shift)

    @property
    def encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        return self._encrypting_dict.copy()

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        if 0 <= shift < 26:
            self.__init__(self.message_text, shift)
        else:
            raise ValueError("Shift must be greater or equal to 0 and less than 26.")


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_words = 0
        best_shift = None
        for shift in range(0, 26):
            count = 0
            for word in self.apply_shift(shift).split():
                if word in self.valid_words:
                    count += 1
            if count > max_words:
                best_shift = shift
                max_words = count
        return (best_shift, self.apply_shift(best_shift))



#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.message_text_encrypted)

#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

#Decrypt a story
story = CiphertextMessage(get_story_string())
print(story.decrypt_message())
