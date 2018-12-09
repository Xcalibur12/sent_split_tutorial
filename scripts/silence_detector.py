#!/usr/env/python3

import codecs
import sys

def sent_split(trn_name):
    sent_list = []
    interval = []
    stopwords = ['정화가', '마십시오', '잘해', '유명하지', '실까']
    
    f = codecs.open(trn_name,'r','utf8').readlines()[1:]
    for i in range(len(f)):
        f[i] = f[i].strip()
        if 'sil' in f[i]:
            if len(interval) == 0:
                interval.append(float(f[i].split()[1])-0.01)
            elif len(interval) > 0:
                interval.append(float(f[i].split()[0])+0.01)
                #print(interval)
                sent_list.append(interval)
                interval = []
                interval.append(f[i].split()[1])
        try:
            interval.append(f[i].split()[3])
        except:
            pass

    for k in range(len(sent_list)-1, -1, -1):
        if sent_list[k-1][-2][-1] != '다' and sent_list[k-1][-2] not in stopwords:
            sent_list[k-1] = sent_list[k-1][:-1]
            #print(sent_list[k], sent_list[k-1])
            sent_list[k-1].extend(sent_list[k][1:])
            sent_list.remove(sent_list[k])

    return sent_list
