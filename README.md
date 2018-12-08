# Sentence Segmentation Tutorial

Let's split a big string into sentences!

# Purpose of This Tutorial

What if you want to split a long sound file and save the smaller files that have a sentence each? (one sentence per file)

# Basic Idea

After you get a recognition result of your sound file with an ASR model, you can use the information from the result for sentence segmentation, since the result file has all the information needed for the task

# The structure of the result file

1st row: A long string of the transcription of the sound file recognized by the ASR model  
2nd ~ last row:

|Column    |Description                          |
|----------|-------------------------------------|
|1st column|Start time of a PLU (Phone Like Unit)|
|2nd column|End time of a PLU                    |
|3rd column|A PLU                                |
|4th column|Optional. A word                     |
  
You can see the example of the structure from data/example.trn

# The approach

The speech from the sound file (which is data/example.wav) is a read speech of over 55 sentences.  
Your task is to divide this long file into one-sentence files.  

When you closely look at the first row of the example.trn, you can easily find out a sentence delimiter is '-다'.  
Since this sound file is a read speech file, you can divide the data based on the time point of every '-다'.  

Also, when you closely look at from the second row this time, on the 3rd column where you can see PLUs, after the last PLU of a word you can see 'sil', which means 'silence'. And then a new word starts with the first PLU of the next word.  

If you consider the two things mentioned above, you can find out a time interval of a sentence
1) Find the end time point of '-다' (which is the end point of a sentence)
2) Find the end time point of 'sil' after '-다' (which is the start point of the next sentence)
