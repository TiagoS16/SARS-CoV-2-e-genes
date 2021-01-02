from cmd import *
import ID
import Blast
import Homologas
import FASTA_Multiple
import Multiple_Alignment


class shell(Cmd):
    intro = ''' \n Comandos da Shell:
     *********************************************************************************************************************            
        procurar_id -> procurar id no NCBI para uma pesquisa e guardar fichero
        procurar_id_swiss -> procurar id Na Swiss Prot e guardar ficheiro
        blast -> realizar blast
        alinhamento_multiplo
                                                                        
                    Prima < ? comando > para mais informações acerca do comando                                          
     *********************************************************************************************************************
'''
    prompt = 'Lab > '
    def do_procurar_id(self,arg):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            file = input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank')
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
        except: print('Opção não valida')

    def do_procurar_id_swiss(self, arg):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            file = input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank')
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
    def do_blast(self,arg):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                pass
    def do_alinhamento_multiplo(selfself,arg):

if __name__ == '__main__':
    shell().cmdloop()
