'''


'''

import os # Importing the 'OS' module

os.system('color 1f')

# Declaration of the text and width variables
text = 'Bem vindo ao instalador do Office!'
width = 30

# Creating a system menu function with options to install Office or exit the program
def menu():
                
    print('\n-------------------')
    print('OFFICE')    
    print('-------------------')           
    print('1 - Instalar Office')
    print('2 - Sair')
    print('-------------------\n')
    
    # Menu Option Request Variable           
    op_menu = input('Selecione uma opção: ')
                
    os.system('cls')
    
    # Conditional structure that processes user input in the menu, ensuring that the user enters a valid option, and if the field is empty or displays an error due to a wrong option, redirects the user back to the menu, displaying the error message.
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

# Creating the ins_office function with the Office version options to install or return to the application menu.                
def ins_office():
    
    print('\n--------------')    
    print('1 - Instalar Office 365 - Configuração x64')
    print('2 - Instalar Office 365 - Configuração x86')
    print('3 - Instalar Office 2019 - Enterprise')
    print('4 - Instalar Office 2021 - Enterprise')
    print('5 - Voltar ao menu')
    print('--------------\n')
    
    # Option request variable to install a specific version of office or return to the menu.       
    op_install = input('Selecione uma opção: ')
                
    os.system('cls')
    
    # Conditional structure that processes the choice of the Office version to install, or the return to the menu, ensuring that the user enters a valid option and, if the field is empty or displays an error due to a wrong option, redirects the user back to the options, displaying the error message.    
    if op_install == '' or op_install == ' ':
        
        print('\nFavor inserir opção desejada!\n')
        os.system('pause')
        os.system('cls')
        ins_office()
                
    elif op_install == '1':
                    
        print('\nInstalando Office 365 - Configuração x64\n')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office365-x64.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
        
    elif op_install == '2':
                    
        print('\nInstalando Office 365 - Configuração x86\n')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office365-x86.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
    
    elif op_install == '3':
                    
        print('\nInstalando Office 2019 - Enterprise\n')
        os.system('cd "Conf_Office365" && setup.exe /configure configuration-Office2019Enterprise.xml')
        os.system('pause')
        os.system('cls')
        ins_office()
        
    elif op_install == '4':
                    
        print('\nInstalando Office 2021 - Enterprise\n')
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

# Printing the welcome message when opening the system.
print(f'\n{text:^{width}}\n')
os.system('pause')
os.system('cls')
       
menu()