#!/usr/env/python3

"""
Author: Xcalibur12
Date: 2018-12-10
"""

import codecs # for hangeul encoding (ascii cannot encode cp949)

def sent_split(trn_name):
    sent_list = []
    interval = []
    stopwords = ['정화가', '마십시오', '잘해', '유명하지', '실까'] # Sentence ending words that do not end with '다' (including wrongly recognized words)
    
    f = codecs.open(trn_name,'r','utf8').readlines()[1:]
    for i in range(len(f)):
        f[i] = f[i].strip()
        if 'sil' in f[i]:
            if len(interval) == 0:
                interval.append(float(f[i].split()[1])-0.01) # Adding extra 0.01 second before the start of the sentence interval
            elif len(interval) > 0:
                interval.append(float(f[i].split()[0])+0.01) # Adding extra 0.01 second after the end of the sentence interval
                sent_list.append(interval)
                interval = []
                interval.append(f[i].split()[1])
        try:
            interval.append(f[i].split()[3])
        except:
            pass
    
    # Putting together wrongfully segmented chunks with '다' at the end but are not sentences
    for k in range(len(sent_list)-1, -1, -1): # Starting from the last sentence index prevents from skipping unprocessed sentences
        if sent_list[k-1][-2][-1] != '다' and sent_list[k-1][-2] not in stopwords:
            sent_list[k-1] = sent_list[k-1][:-1]
            sent_list[k-1].extend(sent_list[k][1:])
            sent_list.remove(sent_list[k])

    return sent_list
