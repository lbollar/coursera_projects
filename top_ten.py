import sys
import json
from operator import itemgetter

def lines(fp):
    print str(len(fp.readlines()))

def getkey(item):
    return item[1]

def main():
     tweets = open(sys.argv[1])
     hashtags = {}
     for line in tweets:
         tweet = json.loads(line)
         if 'text' in tweet:
             if tweet["entities"]["hashtags"]:
                 for i in tweet["entities"]["hashtags"]:
                     hashtag = i["text"]
                     if hashtag not in hashtags:
                         hashtags[hashtag] = 1
                     else:
                         hashtags[hashtag] = hashtags[hashtag] + 1
     top_ten = []

     for key, value in hashtags.iteritems():
         top_ten.append((key,value))
         
     new_list = sorted(top_ten, key=getkey, reverse=True)

     for i in range(0,10):
         print new_list[i][0] + " " + str(new_list[i][1])
if __name__ == '__main__':
    main()
