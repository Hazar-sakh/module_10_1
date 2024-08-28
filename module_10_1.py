from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


ts1 = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
te1 = datetime.now()
print(f'Работа потоков {te1 - ts1}')

ts2 = datetime.now()
_1T = Thread(target=wite_words, args=(10, 'example5.txt'))
_2T = Thread(target=wite_words, args=(30, 'example6.txt'))
_3T = Thread(target=wite_words, args=(200, 'example7.txt'))
_4T = Thread(target=wite_words, args=(100, 'example8.txt'))

_1T.start()
_2T.start()
_3T.start()
_4T.start()

_1T.join()
_2T.join()
_3T.join()
_4T.join()
te2 = datetime.now()
print(f'Работа потоков {te2 - ts2}')
