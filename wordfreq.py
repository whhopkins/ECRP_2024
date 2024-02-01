#!/usr/bin/env python
import argparse, re
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def wordfreq(inFName, maxCount):
    ignoreWords = ['the', 'or', 'and', 'of', 'to', 'for', 'a', 'in', 'be', 'is', 'as', 'atlas', 'by', 'an', 'on', 'that', 'with', 'which', ',', '.', 'pmssm', 'clustering', 'ml', 'pi', 'lhc', '0', '1', '2', '3', 'are', 'this', 'bsm', 'will', 'from', 'at', 'these', 'run', 'fig', 'hl', 'cite', 'ref', 'figure', 's', 'two', 'fullsim', 'sm', 'have', 'has', 'pdf']
    inStr = ''
    with open(inFName, 'r') as inF:
        inStr = inF.read()

    words = [w.lower() for w in re.findall(r"\w+", inStr) if w.lower() not in ignoreWords]
    counts = Counter(words)

    for word, count in counts.most_common(maxCount):
        print(word, count)
        
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                #stopwords = stopwords,
                min_font_size = 10).generate(" ".join(words))
 
    # plot the WordCloud image                       
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig("figures/wordcloud.pdf", format="pdf")

    #plt.show()
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count the frequency of words in your document')
    parser.add_argument('-f', '--inF', type=str, default='proposal_WHopkins.tex')
    parser.add_argument('-m', '--maxCount', type=int, default=10)
    args = parser.parse_args()

    wordfreq(args.inF, args.maxCount)
    
