'''
CUSTOM OFFICE INSTALLER IN PYTHON

This project is a simplified installer for different versions of Microsoft Office, developed in Python. It was created to facilitate and centralize the Office installation process, using the Office Deployment Tool (ODT) and custom XML configuration files.

The main objective is to provide a user-friendly command-line interface (CLI) that guides the user through choosing the desired Office version (Office 365 x64/x86, Office 2019 Enterprise, or Office 2021 Enterprise) and then automatically executes the appropriate installation command. This eliminates the need for the user to memorize or type lengthy ODT commands.

This project is ideal for system administrators or corporate environments that need a quick and standardized way to install specific versions of Microsoft Office.

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
    
    # Conditional structure in Python that processes user input in the menu, ensuring that the user enters a valid option, and if the field is empty or displays an error due to a wrong option, redirects the user back to the menu, displaying the error message.
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

print(f'\n{text:^{width}}\n')
os.system('pause')
os.system('cls')
       
menu()