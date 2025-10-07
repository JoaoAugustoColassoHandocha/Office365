'''


'''

import os

os.system('color 1f')

texto = 'Bem vindo ao instalador do Office 365!'
largura = 30

def menu():
                
    print('\n--------------')
    print('| OFFICE 365 |')
    print('--------------\n')
    
    print('\n--------------')           
    print('1 - Instalar Office 365')
    print('2 - Sair')
    print('--------------\n')
                
    op_menu = int(input('Selecione uma opção: '))
                
    os.system('cls')
                
    if op_menu == 1:
                    
        ins_office()
                    
    elif op_menu == 2:
                    
        print('\nSaindo...!\n')
        os.system('pause')
        os.system('cls')
        os.system('exit')
                
    else:
                    
        print('\nFavor repassar opção correta!\n')
        os.system('pause')
        os.system('cls')
        menu()
                
def ins_office():
    
    print('\n--------------')    
    print('1 - Instalar Office 365 - Configuração x64')
    print('1 - Instalar Office 365 - Configuração x86')
    print('2 - Sair')
    print('--------------\n')
                
    op_install = int(input('Selecione uma opção: '))
                
    os.system('cls')
                
    if op_install == 1:
                    
        ins_office()
                    
    elif op_install == 2:
                    
        print('\nSaindo...!\n')
        os.system('pause')
        os.system('cls')
        os.system('exit')
                
    else:
                    
        print('\nFavor repassar opção correta!\n')
        os.system('pause')
        os.system('cls')
        menu()
    os.system('pause')
    os.system('cls')
    menu()

try:
    
        print(f'\n{texto:^{largura}}\n')
        os.system('pause')
        os.system('cls')
        
        menu()

except Exception  as error:
    
    os.system('cls')
    print(f'{error.__class__.__name__}: {error}')