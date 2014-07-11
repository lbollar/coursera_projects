import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweets = open(sys.argv[1])
    terms = {}
    all_terms = 0
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet:
            string = tweet['text'].strip()
            string = string.lower()
            phrases = string.split()
            
            for word in phrases:
                all_terms = all_terms + 1
                if word not in terms:
                    terms[word] = 1
                else:
                    terms[word] = terms[word] + 1
 
    for term in terms:
        dec = float(terms[term])/float(all_terms)
        print term + " " + str(dec)

if __name__ == '__main__':
    main()
