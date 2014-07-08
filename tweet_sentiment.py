import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweets = open(sys.argv[2])
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text'].strip()
            text = text.lower()
            terms = text.split()
            sum = 0
            for word in terms:
                if word in scores:
                    sum = sum + scores[word]
            print sum

    
if __name__ == '__main__':
    main()
