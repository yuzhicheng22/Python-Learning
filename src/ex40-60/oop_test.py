import random
for urllib request import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
          "Make a class named %%% that is-a %%%.",
      "class %%%(object):\n\tdef __init__(self, ***)" :
          "class %%% has-a __init__ that takes self and *** params.",
      "class %%%(object):\n\tdef ***(self, @@@)":
          "class %%% has-a function *** that takes self and @@@ params.",
      "*** = %%%()":
          "Set *** to an instance of class %%%.",
      "***.***(@@@)":
          "From *** get the *** function, call it with params self @@@.",
      "***.*** = '***'":
          "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_TEST = True
else:
    PHRASES_TEST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    