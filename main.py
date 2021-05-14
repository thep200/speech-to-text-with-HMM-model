import re
import random
import numpy as np
import scipy.io as wavfile
from pydub import AudioSegment

# Chuyển thời gian trong file srt sang milisecond
def convert_to_time(time_start, time_end):
    h1, m1, s1 = time_start.split(':')
    h2, m2, s2 = time_end.split(':')
    return [int((float(h1)*3600 + float(m1)*60 + float(s1))*1000), int((float(h2)*3600 + float(m2)*60 + float(s2))*1000)]
    

# Tách thời gian trong file srt và đoạn text tương ứng 
def get_time_segment(path, word_means):
    time_segment = []

    with open(path, "r", encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        if '-->' in line: 
            # clean string để có thể lấy được time text trong file srt
            array_line = line[0:len(line) - 1].split(' --> ')
            array_line[0] = array_line[0].replace(',', '.')
            array_line[1] = array_line[1].replace(',', '.')

            # i là thời gian tương ứng i + 1 là đoạn text tương ứng với segment đó
            if lines[lines.index(line) + 1][0:-1] == word_means:
                time_segment.append(convert_to_time(array_line[0], array_line[1]))
                # time_segment.append(lines[lines.index(line) + 1][0:-1])

    return time_segment


def extract_audio_segment(path, time, name_audio):
    newAudio = AudioSegment.from_wav(path)
    newAudio = newAudio[time[0]:time[1]]
    newAudio.export(name_audio + '.wav', format="wav") 


if __name__ == '__main__':
    list_path = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    for path in list_path:
        list_segment_cho = get_time_segment('datan/' + path + '.srt', 'cho')
        for _ in list_segment_cho:
            extract_audio_segment('datan/' + path + '.wav', _, 'data_export/' + path + '_' + str(random.randint(0, 999999)))    


