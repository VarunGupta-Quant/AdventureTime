# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Dialogue sounds for game

import wave

def merge_files(fileList, output_file, pitch):
    '''
    Concatenates a list of audio files together
    fileList is a list of paths to audio files, 
    output_file is the path to the output file
    '''

    data = []

    for file in fileList:
        w = wave.open(file, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])      # Now contains all audio files
        w.close()
    
    output = wave.open(output_file, 'wb')                               # Create final output file
    output.setparams(data[0][0])
    output.setframerate(pitch * data[0][0][2])

    for i in range(len(data)):
        output.writeframes(data[i][1])

    output.close()

def factor_sentence(sentence, voice = 'ivan', pitch = 1):
    '''
    Factor a sentence into corresponding 
    audio files based on its characters
    '''
    
    fileList = []
    
    for char in sentence:
        if char.isalpha():
            fileList.append('Assets/animalese/' + voice + '/' + voice + '_' + char.upper() + '.wav')
        elif char == ' ':
            fileList.append('Assets/animalese/ivan/space.wav')
        else:
            fileList.append('Assets/animalese/ivan/bebebese.wav')
    
    merge_files(fileList, 'output.wav', pitch)