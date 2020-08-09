import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class x(y)": "Make a class named x that is-a y",
    "class x(object):\n\tdef __init__(self, test)": "class x has-a __init__that takes self and test params."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("class x(y)"))]
    other_name = random.sample(WORDS, snippet.count("class x(object):\n\tdef __init__(self, test)"))
    results = []
    param_names = []

    for i in range(0, snippet.count("class x(y)")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
    
        #fake class name 
        for word in class_name:
            result = result.replace("class x(y)", word, 1)

        #fake other name 
        for word in other_name:
            result = result.replace("class x(object):\n\tdef __init__(self, test)", word, 1)

        results.append(result)
    return results

    try:
        while True:
            snippets = list(PHRASES.keys())
            random.shuffle(snippet)

            for snippet in snippets:
                phrase = PHRASES[snippet]
                question, answer = convert(snippet, phrase)
                if PHRASES_FIRST:
                    question, answer = answer, question
                
                print(question)

                input('> ')
                print(f"ANSWER: {answer}\n\n")
    except EOFError:
        print("\n Bye")