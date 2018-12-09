import silence_detector
import wave_splitter

input_wav = ".\\test.wav"
trn_name = ".\\test.trn"

def main():
    sent_list = silence_detector.sent_split(trn_name)
    wave_splitter.wav_split(input_wav, sent_list)

if __name__ == '__main__':
    main()