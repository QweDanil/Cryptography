
class Cesar():   
    def encryption(self, text, shift):
        alphabetENG = []
        alphabetENG1 = "abcdefghijklmnopqrstuvwxyz"
        alphabetENG1 = list(alphabetENG1)
        alphabetCesarENG1 = alphabetENG1[shift::] + alphabetENG1[:3:]
        dictAlphabetsENG1 = dict(zip(alphabetENG1, alphabetCesarENG1))
        for i in range(65, 91):
            alphabetENG.append(chr(i)) #функция возвращает строку, представляющую символ Unicode-код которой соответствует числу i переданному в эту функцию
            punctuationENG = []
        for i in range(0, 64):
            punctuationENG.append(chr(i))
        for i in range(91, 177):
            punctuationENG.append(chr(i)) #создание словаря из пунктуации
        punctuationENG = dict(zip(punctuationENG, punctuationENG))
        alphabetCesarENG = alphabetENG[shift::] + alphabetENG[:3:]
        dictAlphabetsENG = dict(zip(alphabetENG, alphabetCesarENG)) #Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи
        dictAlphabetsENG[" "] = " "
        dictAlphabetsENG["Ё"] = "И"

        _dictAlphabets_punctuationENG = dictAlphabetsENG | punctuationENG #слияние пунктуации и словаря Цезаря
        alphabet1 = "абвгдежзийклмнопрстуфчцчшщъыьэюя"
        alphabet1 = list(alphabet1)
        alphabetCesar1 = alphabet1[shift::] + alphabet1[:3:]
        dictCesar1 = dict(zip(alphabet1, alphabetCesar1))
        alphabet = ""
        for i in range(ord("А"), ord("Я")+1): #возвращает целое число - номер из таблицы символов Unicode, представляющий позицию данного символа
            alphabet += chr(i)
        alphabet = list(alphabet)
        punctuation = []
        for i in range(0, 64):
            punctuation.append(chr(i))
        for i in range(123, 177):
            punctuation.append(chr(i)) #создание словаря из пунктуации
        punctuation = dict(zip(punctuation, punctuation))
        alphabetCesar = alphabet[shift::] + alphabet[:3:]
        dictAlphabets = dict(zip(alphabet, alphabetCesar))#Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи
        dictAlphabets[" "] = " "

        _dictAlphabets_punctuation = dictAlphabets | punctuation #слияние пунктуации и словаря Цезаря
        encrypt1 = _dictAlphabets_punctuation | _dictAlphabets_punctuationENG
        encrypt2 = encrypt1 | dictCesar1
        encrypt3 = encrypt2 | dictAlphabetsENG1
        encrypt3["п"] = "х"
        encrypt3["х"] = "ш"
        del encrypt3["ф"]
        word = []
        for i in text:
            for x, c in encrypt3.items():
                if i == x:
                    word.append(c)
        word = "".join(word)
        return word

    def decryption(self, text, shift):

        alphabetENG = []
        alphabetENG1 = "abcdefghijklmnopqrstuvwxyz"
        alphabetENG1 = list(alphabetENG1)
        alphabetCesarENG1 = alphabetENG1[shift::] + alphabetENG1[:3:]
        dictAlphabetsENG1 = dict(zip(alphabetENG1, alphabetCesarENG1))
        for i in range(65, 91):
            alphabetENG.append(chr(i)) #функция возвращает строку, представляющую символ Unicode-код которой соответствует числу i переданному в эту функцию
            punctuationENG = []
        for i in range(0, 64):
            punctuationENG.append(chr(i))
        for i in range(91, 177):
            punctuationENG.append(chr(i)) #создание словаря из пунктуации
        punctuationENG = dict(zip(punctuationENG, punctuationENG))
        alphabetCesarENG = alphabetENG[shift::] + alphabetENG[:3:]
        dictAlphabetsENG = dict(zip(alphabetENG, alphabetCesarENG)) #Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи
        dictAlphabetsENG[" "] = " "
        # dictAlphabetsENG["Ё"] = "И"

        _dictAlphabets_punctuationENG = dictAlphabetsENG | punctuationENG #слияние пунктуации и словаря Цезаря
        alphabet1 = "абвгдежзийклмнопрстуфчцчшщъыьэюя"
        alphabet1 = list(alphabet1)
        alphabetCesar1 = alphabet1[shift::] + alphabet1[:3:]
        dictCesar1 = dict(zip(alphabet1, alphabetCesar1))
        alphabet = ""
        for i in range(ord("А"), ord("Я")+1): #возвращает целое число - номер из таблицы символов Unicode, представляющий позицию данного символа
            alphabet += chr(i)
        alphabet = list(alphabet)
        punctuation = []
        for i in range(0, 64):
            punctuation.append(chr(i))
        for i in range(123, 177):
            punctuation.append(chr(i)) #создание словаря из пунктуации
        punctuation = dict(zip(punctuation, punctuation))
        alphabetCesar = alphabet[shift::] + alphabet[:3:]
        dictAlphabets = dict(zip(alphabet, alphabetCesar))#Функция zip() принимает на входе несколько итерируемых объектов (iterable) или итераторов (iterators) и поэлементно группирует в кортежи
        dictAlphabets[" "] = " "

        _dictAlphabets_punctuation = dictAlphabets | punctuation #слияние пунктуации и словаря Цезаря
        encrypt1 = _dictAlphabets_punctuation | _dictAlphabets_punctuationENG
        encrypt2 = encrypt1 | dictCesar1
        encrypt3 = encrypt2 | dictAlphabetsENG1
        encrypt3["п"] = "х"
        encrypt3["х"] = "ш"
        del encrypt3["ф"]
        word = []
        for i in text:
            for x, c in encrypt3.items():
                if i == c:
                    word.append(x)
        word = "".join(word)
        return word