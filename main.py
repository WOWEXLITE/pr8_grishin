
from random import choices

symbols = 'ABCDEFGHJKLMNOPQRSTUVWXYZ'

chars = ''

pwd_length = int(input('длинна пароля?: '))
pwd_auto = (input('автоматически подобрать пароль? (y,n): ') == 'y')

for text, seq in(
                 ('Включить верхний регистор', symbols),
    if pwd_auto or(input(text + ' (y,n): ') == 'y'):
       chars += seq
password = ''.join(choices(chars, k=pwd_length))

print ('\n', password '\n', sep='')
