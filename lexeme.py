'''
Created on 4 Feb. 2019 y.

@author: Jurij Bakhtin
'''
from builtins import str
import sys
import os



# -*- Класс, описывающий лексему в формате <номер строки>lex:<лексема>[<тип>:<распознанное_значение>][val:<значение>] -*-
class Lexeme:
    lineNumber = '?'
    lexeme = '?'
    typeLexeme = '?'
    recognizedValue = '?' 
    value = '?'
    
    
    def __init__(self, lineNumber, lexeme, typeLexeme, recognizedValue, value):
        self.lineNumber = str(lineNumber)
        self.lexeme = str(lexeme)
        self.typeLexeme = str(typeLexeme)
        self.recognizedValue = str(recognizedValue)
        self.value = str(value)
    
    
    # -*- Полное описание лексемы -*-
    def getDescription(self):
        return(self.lineNumber + 'lex:' + self.lexeme + self.typeLexeme + ':'+self.recognizedValue + 'val:' + self.value) 
    
    
    def getDescriptionTable(self):
        return("Номер строки: " + self.lineNumber + '\nЛексема: ' + self.lexeme + '\nТип: ' + self.typeLexeme + 
               '\nРАспознанное значение: ' + self.recognizedValue + '\nЗначение: ' + self.value) 
    
# -*- Определение принадлежности символа к классу букв -*-
def isLetter(ch):
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        return True
    else:
        return False

  
# -*- Определение принадлежности символа к классу двоичных цифр -*-
def isBin(ch):
    if((ch == '0' or ch == '1')):
        return True
    else:
        return False

   
# -*- Определение принадлежности символа к классу восьмиричных цифр -*- 
def isOctal(ch):
    if((ch >= '0' and ch <= '7')):
        return True
    else:
        return False


# -*- Определение принадлежности символа к классу десятичных цифр -*-
def isDigit(ch):
    if((ch >= '0' and ch <= '9')):
        return True
    else:
        return False


# -*- Определение принадлежности символа к классу шестнадцатеричныхцифр -*-
def isHex(ch):
    if((ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F') or (ch >= 'a' and ch <= 'f')):
        return True
    else:
        return False
    

# -*-Определение принадлежности символа к классу пропусков -*-
def isSkip(ch):
    if(ch == ' ' or ch == '\t' or ch == '\n' or ch == '\f'):
        return True
    else:
        return False

# -*- Определяет принадлежность к классу игнорируемых символов -*-
def isIgnore(ch):
    if (ch > 0 and ch < ' ' and ch != '\t' and ch != '\n' and ch !='\f'):
        return True
    else:
        return False


def transliterator(ch):
    pass


# -*- Лексический анализатор. Принимает целый файл-*-
def scanner(file_programm):
    lexems = [] # Список лексем.
    obj_list = []
    lexem = ''  # Обрабатываемая лексема
    ch_index_in_line = 0
    # Разбиваем вхожной поток по строкам
    for line_number, line in enumerate(file_programm):
        ch_index_in_line = 0 # Индекс обрабатываемого символа, обнуляем для каждой строки
        lexem = '' # обнуляем лексему
        # Блок транслитератор?!    <<<---
        # Начинаем перебор символов
        for index_in_line in range(ch_index_in_line, len(line)):
            # Если БУКВА, то начинаем обрабатывать возможные лексемы:
            #  - ЗАРЕЗЕРВИРОВАННАЯ ИНСТРУКЦИЯ
            #  - ИДЕНТИФИКАТОР
            #  - ... Дописать    <<<---
            if isLetter(line[index_in_line]):
                # Заполняем лексему 
                lexem = lexem + line[index_in_line]
                # Обрабатываем дальш потенциальную лексему
                for index_in_lexem in range(ch_index_in_line + 1, len(line)):
                    # Если последующий символ БУКВА то
                    if isLetter(line[index_in_lexem]):
                        # Заполняем лесему
                        lexem = lexem + line[index_in_lexem]
                        # Продолжаем обработку возможной лексемы
                        continue
                    # Иначе, если разделяющий символ, то определена лексема (ИДЕНТИФИКАТОР или ЗАРЕЗЕРВИРОВАННАЯ ИНСТРУКЦИЯ)
                    elif isSkip(line[index_in_lexem]):
                        # Добавляем лексему в список
                        lexems.append(lexem)
                        # Обнуляем обрабатываемую лексему
                        ch_index_in_line = index_in_lexem
                        index_in_line = index_in_lexem
                        lexem = ''
                        # Заканчиваем обраьотку лесемы
                        break
                    # Если символ не определен, то предположение о возможной лексеме ложно
                    else:
                        # Обнуляем обрабатываемую лесему
                        lexem = ''
                        # Заканчиваем обраьотку лесемы
                        break
                # Выходим из цикла, чтобы начать обработку новой, потенциальной, лексемы
                continue
             
            # Если ЦИФРА, то начинаем обрабатывать возможные лексемы:
            #  - ЦЕЛОЕ ЧИСЛО
            #  - ДРОБНОЕ ЧИСЛО
            #  - ... Дописать    <<<---
            if isDigit(line[index_in_line]):
                # Заполняем лексему 
                lexem = lexem + line[index_in_line]
                # Обрабатываем дальш потенциальную лексему
                for index_in_lexem in range(ch_index_in_line + 1, len(line)):
                    # Если последующий символ БУКВА то
                    if isDigit(line[index_in_lexem]):
                        # Заполняем лесему
                        lexem = lexem + line[index_in_lexem]
                        # Продолжаем обработку возможной лексемы
                        continue
                    # Иначе если точка то тип лессемы ДРОБНОЕ ЧИСЛО
                    #elif line[ch_index_in_line] == '.':
                         
                    # Иначе, если разделяющий символ, то определена лексема (ИДЕНТИФИКАТОР или ЗАРЕЗЕРВИРОВАННАЯ ИНСТРУКЦИЯ)
                    elif isSkip(line[index_in_lexem]):
                        # Добавляем лексему в список
                        obj = Lexeme(line_number, 'Int', type(int(lexem)), int(lexem), lexem)
                        obj_list.append(obj)
                        lexems.append(lexem)
                        # Обнуляем обрабатываемую лексему
                        ch_index_in_line = index_in_lexem
                        lexem = ''
                        # Заканчиваем обраьотку лесемы
                        break
                    # Если символ не определен, то предположение о возможной лексеме ложно - ОШИБКА
                    else:
                        # Обнуляем обрабатываемую лесему
                        lexem = ''
                        # Заканчиваем обраьотку лесемы
                        break
                # Выходим из цикла, чтобы начать обработку новой, потенциальной, лексемы
                continue

            # Смещаемся на индекс вперед, так как на текущий символ не определен Транслитератором    <<<--- Временно
            ch_index_in_line += 1
            
     
    print(lexems)
    for obj in obj_list:
        print(obj.getDescription())
        
    for obj in obj_list:
        print(obj.getDescriptionTable())


# -*- Главная функция -*-
def main(fp, fl):
    
    if len(sys.argv) != 1:
        if os.stat(sys.argv[1]).st_size != 0:
            with open(fp) as input_file_programm:
                scanner(input_file_programm)
        else:
            print("Input file is empty")
    else:
        print('Parametrs not found')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

