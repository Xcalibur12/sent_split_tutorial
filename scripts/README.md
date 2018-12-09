# Audio Sentence Segmentation via ASR Result
This tutorial to retrieve sentence segmented audio files from one long file by getting time information from its recognized transcription

# File Descriptions
* main.py  
- This file is the main script that imports necessary functions for audio sentence segmentation
* sent_splitter.py
- This file reads the transcription data and outputs the time infromation (start and end) of each sentence segmented chunk
* wave_splitter.py
- This file reads the time information from `sent_splitter.py` and outputs actual segmented wav files
