import speech_recognition as sr
from time import sleep
import webbrowser
import bitcoinAPI
from spokenInptProcessing import scanString


recognizer= sr.Recognizer()

bitcoin= bitcoinAPI.Bitcoin()

numbersOfSpeak= 0
b= True

def recog():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio= recognizer.listen(source)
            spokenInpt= recognizer.recognize_google(audio, language='en-US')
            print(f'-> {spokenInpt}')
            #numbersOfSpeak+= 1

        return spokenInpt

    #except AttributeError as aErr:
    #    print(f'inaccurately language: {lang}'


    except BaseException as err:
        print(f'an error occurred:\n{err}')



print('*** welcome ***')
print('type: google')





while b:
    try:
        inpt= input('::: ').lower()

        if inpt==('q' or 'esc' or 'c'):
            print(f'program stop, caused by KeyboardInterrupt({inpt})')
            b= False
            continue

        elif inpt == 'google':
            for i in range(3, 0, -1):
                print(f'{i} ', end='')
                sleep(0.3)
            print('\nspeak!')
            search = recog()
            numbersOfSpeak+= 1
            url = f'https://www.google.com/search?q={search}&oq={search}&aqs=chrome..69i57j0i131i433j0i433j0i131i433j0i433j0i131i433j0j69i61.1607j1j7&sourceid=chrome&ie=UTF-8'
            webbrowser.open(url)
            print(f'round{numbersOfSpeak} completed')

        elif inpt == '':
            for i in range(3, 0, -1):
                print(f'{i} ', end='')
                sleep(0.2)
            print('\nspeak!')
            search = recog()
            numbersOfSpeak+= 1
            search= search.lower()

            scanString(search)
            print(f'round{numbersOfSpeak} completed')

        else:
            continue

        print('--------------------')

        """
            elif inpt == 'language':
        lang= input(f'from {lang} to ?: ')
        print(f'language set to {lang}')
        """

    except Exception as err:
        print(f'an error occurred:\n{err}')

    except KeyboardInterrupt as kyInrpt:
        print(f'program stop, caused by KeyboardInterrupt')







