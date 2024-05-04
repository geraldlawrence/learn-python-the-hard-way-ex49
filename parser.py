class ParserError(Exception):
    pass


class Sentence(object):
    
    def __init__(self, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]
        
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        
        if word[0] == expecting:
            return word
        
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    i = 0
    while i < len(word_list):
        if word_list[i][0] == word_type:
            #del is a tooling to delete specific argument in a list/dictionary/etc...
            del word_list[i]
        else:
            i += 1

def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)
    
    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
     verb = parse_verb(word_list)
     obj = parse_object(word_list)
     
     return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')
    
    start = peek(word_list)
    
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        subj = ('noun', 'player')
        return parse_subject(word_list, subj)
    else:
        raise ParserError("Must start with subject, object or verb not: %s" % start)
