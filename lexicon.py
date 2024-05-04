from sys import argv

lexicon = {}
directions = ['north', 'south', 'east', 'west']
verbs = ['go', 'eat', 'kill', 'killed', 'open']
stops = ['the', 'of', 'in', 'by', 'with', 'from', 'is', 'to']
nouns = ['bear', 'princess', 'door']
lexicon.update(dict.fromkeys(nouns, 'noun'))
lexicon.update(dict.fromkeys(stops, 'stop'))
lexicon.update(dict.fromkeys(verbs, 'verb'))
lexicon.update(dict.fromkeys(directions, 'direction'))

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    result = []
    for word in words:
        if convert_numbers(word) != None:
            result.append(('number', convert_numbers(word)))
        else:
            try:
                result.append((lexicon[word], word))
            except KeyError:
                result.append(('error', word))
    return result