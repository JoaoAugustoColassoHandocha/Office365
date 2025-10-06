'''


'''

import os

os.system('color 1f')

texto = 'Bem vindo ao instalador do Office 365!'
largura = 30

try:
    
    def menu():
        
        print(f'\n{texto:^{largura}}\n')
        os.system('pause')
        os.system('cls')
    
        while True:
                
                print('\n--------------')
                print('| OFFICE 365 |')
                print('--------------\n')
                
                print('1 - Instalar Office 365')
                print('2 - Sair')
                
                op = int(input('\nSelecione uma opção: '))
                
                os.system('cls')
                
                if op == 1:
                    
                    ins_office()
                    
                elif op == 2:
                    
                    print('Saindo...!')
                    os.system('pause')
                    break
                
                else:
                    
                    print('Favor repassar opção correta!')
                    os.system('pause')
                    menu()
                
    def ins_office():
                
        os.system('pause')
        os.system('cls')
        menu()

except Exception  as error:
    
    print(f'{error.__class__.__name__}: {error}')

menu()