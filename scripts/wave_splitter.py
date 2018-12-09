#!/usr/env/python3

from pydub import AudioSegment

def wav_split(input_wav, sent_list):
    i = 0
    for sent in sent_list:
        t1 = float(sent[0] ) * 1000. # Start of the sentence interval / the input is in milliseconds so needs to be multiplied by 1000
        t2 = float(sent[-1]) * 1000. # End of the sentence interval
        newAudio = AudioSegment.from_wav(input_wav)
        newAudio = newAudio[t1:t2]
        new_wav = input_wav.rsplit('.',1)[0]+'_%02d.wav'%(i+1) # Name of the segmented wav file: source wav name + sentence number
        newAudio.export(new_wav, format='wav')
        i += 1 # Change to the next sentence index
