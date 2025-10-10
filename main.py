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
                    
        print('Instalando Office 365 - Configuração x64')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office365-x64.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
        
    elif op_install == '2':
                    
        print('Instalando Office 365 - Configuração x86')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office365-x86.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
    
    elif op_install == '3':
                    
        print('Instalando Office 2019 - Enterprise')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office2019Enterprise.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
        
    elif op_install == '4':
                    
        print('Instalando Office 2021 - Enterprise')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office2021Enterprise.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
                    
    elif op_install == '5':
                    
        print('\nRetornando ao menu...!\n')
        os.system('pause')
        os.system('cls')
        menu()
                
    else:
                    
        print('\nFavor repassar opção correta!\n')
        os.system('pause')
        os.system('cls')
        ins_office()

print(f'\n{texto:^{largura}}\n')
os.system('pause')
os.system('cls')
       
menu()