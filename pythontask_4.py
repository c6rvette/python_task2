s=str(input())
if s.count('f')==1:
    print(s.find('f'))
elif s.count('f')>1:
    print('Первое появление:', s.find('f'), 'Последнее появление:', s.rfind('f'))
else:
    print(' ')