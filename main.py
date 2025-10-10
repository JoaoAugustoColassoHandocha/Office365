'''


'''

import os

os.system('color 1f')

texto = 'Bem vindo ao instalador do Office 365!'
largura = 30

def menu():
                
    print('\n-------------------')
    print('OFFICE')    
    print('-------------------')           
    print('1 - Instalar Office')
    print('2 - Sair')
    print('-------------------\n')
                
    op_menu = input('Selecione uma opção: ')
                
    os.system('cls')
    
    if op_menu == '' or op_menu == ' ':
        
        print('\nFavor inserir opção desejada!\n')
        os.system('pause')
        os.system('cls')
        menu()
            
    elif op_menu == '1':
                    
        ins_office()
                    
    elif op_menu == '2':
                    
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
    print('2 - Instalar Office 365 - Configuração x86')
    print('3 - Instalar Office 2019 - Enterprise')
    print('4 - Instalar Office 2021 - Enterprise')
    print('5 - Voltar ao menu')
    print('--------------\n')
                
    op_install = input('Selecione uma opção: ')
                
    os.system('cls')
    
    if op_install == '' or op_install == ' ':
        
        print('\nFavor inserir opção desejada!\n')
        os.system('pause')
        os.system('cls')
        ins_office()
                
    elif op_install == '1':
                    
        print('1')
        
    elif op_install == '2':
                    
        print('2')
    
    elif op_install == '3':
                    
        print('3')
        
    elif op_install == '4':
                    
        print('4')
                    
    elif op_install == '5':
                    
        print('\nRetornando ao menu...!\n')
        os.system('pause')
        os.system('cls')
                
    else:
                    
        print('\nFavor repassar opção correta!\n')
        os.system('pause')
        os.system('cls')
        menu()

    os.system('cls')
    menu()

print(f'\n{texto:^{largura}}\n')
os.system('pause')
os.system('cls')
       
menu()