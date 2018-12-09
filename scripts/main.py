import sent_splitter
import wave_splitter

input_wav = ".\\data\\test.wav"
trn_name = ".\\data\\test.trn"

def main():
    sent_list = sent_splitter.sent_split(trn_name)
    wave_splitter.wav_split(input_wav, sent_list)

if __name__ == '__main__':
    main()
