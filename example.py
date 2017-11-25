import nltk
import sys

sentence = "Run down to room 6" if len(sys.argv) == 1 else sys.argv[1]


def get_obj_name(text: str) -> str:
    """
    :param text: the text the user spoke.
    :return: the name of the object the user is referring to.
    """
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    nouns = [(i, word) for i, (word, tag) in enumerate(tagged) if tag == 'NN']

    if nouns is None:
        raise Exception('No place name found')

    i, noun = nouns[0]

    # Find the name of the room.
    if noun == 'room' and i+1 < len(tokens):
        room_name = tokens[i+1]
        return 'room ' + room_name

    return noun


print('PLACE: ' + get_obj_name(sentence))