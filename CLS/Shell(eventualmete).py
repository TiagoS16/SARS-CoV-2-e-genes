from cmd import *
import ID
import Blast
import Homologas
import FASTA_Multiple
import Multiple_Alignment


class shell(Cmd):
    intro = ''' \n Comandos da Shell:
     *********************************************************************************************************************            
        procurar_id_nucleotide -> procurar id na database Nucleotide NCBI para uma pesquisa e guardar ficheiro
        procurar_id_protein -> procurar id na database Protein NCBI para uma pesquisa e guardar ficheiro
        procurar_id_swiss -> procurar id Na Swiss Prot e guardar ficheiro
        blast -> realizar blast
        alinhamento_multiplo -> 
        sair -> sair da função
                                                                        
                    Prima < ? comando > para mais informações acerca do comando                                          
     *********************************************************************************************************************
'''
    prompt = 'Lab > '
    def do_procurar_id_nucleotide(self):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            file = input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: ')
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
            if file == '1':
                    pass
            elif file == '2':
                    pass

        except: print('Opção não valida')

    def do_procurar_id_protein(self):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            file = input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: ')
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
            if file == '1':
                pass
            elif file == '2':
                pass
        except: print('Opção não valida')

    def do_procurar_id_swiss(self):
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            file = input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: ')
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                pass
            elif option == '5':
                print(" Necessário saber o id na base de dados na Swiss Prot ")
                pass
            if file == '1':
                    pass
            elif file == '2':
                    pass

        except:
            print('Opção não valida')

    def do_blast(self):
        print(" É necessario possuir um ficheiro .fasta ou .gb para realizar esta operação")
        try:
            option = input('introduzir Blast a realizar: \n 1 - Blastp \n 2 - Blastn \n 3 - Blastx \n Opção:')
            if option == '1':
                pass
            elif option == '2':
                pass
            elif option == '3':
                pass
        except:
            print('Opção não valida')

    def do_alinhamento_multiplo(self):
        print(" É necessario possuir um ficheiro .xml resultante de um Blast para realizar esta operação")
        pass

    def do_menu(self):
        print(self.intro)

    def do_sair(self, arg):
        print('Até depois!')
        return True
if __name__ == '__main__':
    shell().cmdloop()
