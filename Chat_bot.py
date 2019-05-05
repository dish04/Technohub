input1 = input('Hi how can i help you? *press enter*').lower()

if input1 == 'i need help' or input1 == '' or 'hi':
   print('I can Help with queries related to technohub 2019')

input2 = input('''
 _______________________________________________________________________
|                                                                       |
|[1]|If you have a doubt regarding the events press "1" and press enter |  
|_______________________________________________________________________|
|                                                                       |
|[2]|If you have a doubt regarding the venue or timmings press "2" and  |
|    press enter|                                                       |
|_______________________________________________________________________|
|                                                                       |
|[3]|If you want more info about Technihub 2019 press "3" and press     |
|    enter|                                                             |
|_______________________________________________________________________|
|                                                                       |
|[4]If you have time to pass and want to chat or play with me press "4" |
|   and press enter|                                                    |
|_______________________________________________________________________|

 ''')

if input2 == '1':
    print("""There are a number of events in this years technohub 
    The events are:
    [1]Cryptonite
    [2]#WhatsTrending
    [3]Kode
    [4]Vlogger
    [5]Quad Damage
    """)
if input2 == '2':
    print('''
    
    __________________________________
   |               VENUE              |
   |MESKKPS, 3rd Stage,               |
   |4th Main, 11th Cross,             |
   |Vidyaranyapura, Bangalore 5600 97.|
   |__________________________________|
    ''')