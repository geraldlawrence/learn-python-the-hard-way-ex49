from nose.tools import *
from ex49 import lexicon, parser


def test_Sentence():
    result = parser.Sentence(('noun', 'bear'), ('verb', 'kill'), ('noun', 'princess'))
    assert result.object == 'princess'
    assert result.subject == 'bear'
    assert result.verb == 'kill'

def test_peek():
    word_list = lexicon.scan("princess kill the bear")
    peek_result = parser.peek(word_list)
    assert peek_result == ('noun')

def test_match():
    word_list = lexicon.scan("eat by the bear")
    match_result = parser.match(word_list, 'verb')
    assert match_result == ('verb', 'eat')

def test_skip():
    word_list = lexicon.scan("bear kill the princess")
    parser.skip(word_list, 'stop')
    assert_equal(word_list, lexicon.scan("bear kill princess"))

def test_parse_verb():
    word_list = lexicon.scan("killed the princess")
    result = parser.parse_verb(word_list)
    assert_equal(result, ('verb', 'killed'))
    
    word_list = lexicon.scan("bear killed the princess")
    with assert_raises(parser.ParserError) as cm:
        parser.parse_verb(word_list)
    exception = cm.exception
    assert str(exception) == "Expected a verb next."

def test_parse_object():
    word_list = lexicon.scan("bear eat the princess")
    result = parser.parse_object(word_list)
    assert result == ('noun', 'bear')
    
    word_list2 = lexicon.scan("to north the princess go")
    result2 = parser.parse_object(word_list2)
    assert result2 == ('direction', 'north')
    
    word_list3 = lexicon.scan("go to north the princess")
    assert_raises(parser.ParserError, parser.parse_object, word_list3)

def test_parse_subject():
    subj = ('noun', 'bear')
    word_list = lexicon.scan("eat the princess")
    result = parser.parse_subject(word_list, subj)
    assert_equal(result.object, 'princess')
    assert_equal(result.verb, 'eat')
    assert_equal(result.subject, 'bear')

def test_parse_sentence():
    word_list = lexicon.scan("the bear go to north")
    result = parser.parse_sentence(word_list)
    assert result.subject == 'bear'
    assert result.verb == 'go'
    assert result.object == 'north'
    
    word_list = lexicon.scan("open the door")
    result = parser.parse_sentence(word_list)
    assert result.subject == 'player'
    assert result.verb == 'open'
    assert result.object == 'door'
    
    word_list = lexicon.scan("asjhdj 12j ahjsd")
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)
