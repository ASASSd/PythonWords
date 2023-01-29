lex_list = ['', ['тысяч', 'тысячи', 'тысяча'], ['миллионов', 'миллиона', 'миллион']]

ones = {1:['одна', 'один'], 2:['две', 'два'], 3:['три', 'три'], 4:['четыре', 'четыре'], 5:['пять', 'пять'], 6:['шесть', 'шесть'], 7:['семь', 'семь'], 8:['восемь', 'восемь'], 9:['девять', 'девять']}
afterones = {10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 19:'девятнадцать'}
tens = {2:'двадцать', 3:'тридцать', 4:'сорок', 5:'пятьдесят', 6:'шестьдесят', 7:'семьдесят', 8:'восемьдесят', 9:'девяносто'}
hundreds = {1:'cто', 2:'двести', 3:'триста', 4:'четыреста', 5:'пятьсот', 6:'шестьсот', 7:'семьсот', 8:'восемьсот', 9:'девятьсот'}

def val_to_num(n):
    edn = n % 10
    des = (n // 10) % 10
    sot = n // 100
    return [edn, des, sot]
    
def lng_to_sht(n):
    mil = n // 1000000
    ths = n // 1000 % 1000
    sot = n % 1000
    return [sot, ths, mil]
    
def sht_to_lex(edn, des, sot, flag):
    ret_str = str()
    
    if sot != 0:
        ret_str += hundreds[sot] + ' '
    
    if des != 0:
        if des == 1:
            ret_str += afterones[des * 10 + edn]
            return ret_str
        else:
            ret_str += tens[des] + ' '
            
    if edn != 0:        
        ret_str += ones[edn][flag]
        
    return ret_str
    
n = int(input())

if n == 0:
    print('ноль')
    exit()

num_lg = lng_to_sht(n)
num_sht = list()
for i in num_lg:
    num_sht.append(val_to_num(i))

out_str = str()
for i in reversed(range(1, 3)):
    if num_sht[i] != [0, 0, 0]:
        if (num_sht[i][0] >= 5) | (num_sht[i][0] == 0) | ((num_lg[i] % 100 >= 10) & (num_lg[i] % 100 <= 19)):       # обрабатываем: тысяч, миллионов
            out_str += sht_to_lex(num_sht[i][0], num_sht[i][1], num_sht[i][2], i-1) + ' ' + lex_list[i][0] + ' '    # достаём нужные слова из словарей и листа с номиналами
        elif (num_sht[i][0] < 5) & (num_sht[i][0] > 1):                                                             # обрабатываем: тысячи, миллиона
            if (num_lg[i] % 100 <= 9) | (num_lg[i] % 100 >= 20):                                                    # проверка на принадлежность к т.н. afterones...
                out_str += sht_to_lex(num_sht[i][0], num_sht[i][1], num_sht[i][2], i-1) + ' ' + lex_list[i][1] + ' '# достаём нужные слова из словарей и листа с номиналами
        elif (num_sht[i][0] == 1) :                                                                                 # обрабатываем: тысяча, миллион
            if (num_lg[i] % 100 <= 9) | (num_lg[i] % 100 >= 20):                                                    # проверка на принадлежность к т.н. afterones...
                out_str += sht_to_lex(num_sht[i][0], num_sht[i][1], num_sht[i][2], i-1) + ' ' + lex_list[i][2] + ' '# достаём нужные слова из словарей и листа с номиналами

out_str += sht_to_lex(num_sht[0][0], num_sht[0][1], num_sht[0][2], 1)
print(out_str)
