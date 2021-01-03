from cmd import *
from ID import ID, Prot_ID
from Blast import Blast
from Homologas import homologas
from FASTA_Multiple import Create_fasta
from Multiple_Alignment import Mutiple



class shell(Cmd):
    intro = ''' \n Comandos da Shell:
************************************************************************************************************************           
        procurar_id_nucleotide -> procurar id na database Nucleotide NCBI para uma pesquisa e guardar ficheiro
        procurar_id_protein -> procurar id na database Protein NCBI para uma pesquisa e guardar ficheiro
        guardar_nucleotide <nome_para_ficheiro> <id> -> guardar ficheiro apartir do id na database Nucleotide NCBI
        guardar_protein <nome_para_ficheiro> <id> ->guardar ficheiro apartir do id na database Protein NCBI
        procurar_id_swiss -> procurar id Na Swiss Prot e guardar ficheiro
        blast <nome_para_ficheiro> <input_file> <formato_do_input_file> -> realizar blast
        report_blast <nome_para_ficheiro> <input_file_blast> <E-value threshold> -> Obter o report do blast 
        homologia <nome_para_ficheiro> <input_file_blast> <E-value threshold(opcional)> -> obter os hits do blast
        homologo_AC <nome_para_ficheiro> <input_file_blast> <E-value threshold(opcional)> -> obter os AC dos hits
        fasta_homologos <nome_para_ficheiro> <input_file_blast> <(Nut/Ppt)> <E-value threshold(opcional)> obter a 
        sequencia total dos hits atraves dos AC
        alinhamento_multiplo <diretoria do clustalw2> <Input_file> -> 
        sair -> sair da função
                                                                        
                    Prima < ? comando > para mais informações acerca do comando                                          
************************************************************************************************************************
'''
    prompt = 'Lab > '
    def do_procurar_id_nucleotide(self,arg):
        ''''
        > Procura a sequência para uma query na base de dados Nucleotide do NCBI
        Variaveis : Recebidas ao longo execução da função
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print("tipo de ficheiro inválido")
            option = int(input('introduzir query a pesquisar: \n 1 - ORF3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
            if option == 1:
                ORF3a = ID('ORF3a', 'Nucleotide', 10, 'example@gmail.com', t_file)
                ID.SEARCH(ORF3a)
                ID.Save_file(ORF3a)
            elif option == 2:
                FGA = ID('FGA', 'Nucleotide', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGA)
                ID.Save_file(FGA)
            elif option == 3:
                FGB = ID('FGB', 'Nucleotide', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGB)
                ID.Save_file(FGB)
            elif option == 4:
                FGG = ID('FGG', 'Nucleotide', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGG)
                ID.Save_file(FGG)
            elif option == 5:
                y = input('Recomenda-se realizar a query por <Organismo><gene><RefSeq> \n Query a pesquisar: ')
                Random = ID(y, 'Nucleotide', 10, 'example@gmail.com', t_file)
                ID.SEARCH(Random)
                ID.Save_file(Random)
            else:
                print('Opção inválida')
        except: print('Erro de execução')

    def do_procurar_id_protein(self, arg):
        ''''
        > Procura a sequência para uma query na base de dados Protein do NCBI
        Variaveis : Recebidas ao longo execução da função
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print("tipo de ficheiro inválido")
            option = int(input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
            if option == 1:
                print('Pesquisa não fiável, recomenda-se a utilização da função procurar_id_swiss')
                ORF3a = ID('ORF3a', 'Protein', 10, 'example@gmail.com', t_file)
                ID.SEARCH(ORF3a)
                ID.Save_file(ORF3a)
            elif option == 2:
                FGA = ID('FGA', 'Protein', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGA)
                ID.Save_file(FGA)
            elif option == 3:
                FGB = ID('FGB', 'Protein', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGB)
                ID.Save_file(FGB)
            elif option == 4:
                FGG = ID('FGG', 'Protein', 10, 'example@gmail.com', t_file)
                ID.SEARCH(FGG)
                ID.Save_file(FGG)
            elif option == 5:
                y = input('Recomenda-se realizar a query por <Organismo><gene><RefSeq> \n Query a pesquisar: ')
                Random = ID(y, 'Protein', 10, 'example@gmail.com', t_file)
                ID.SEARCH(Random)
                ID.Save_file(Random)
            else:
                print('Opção inválida')
        except: print('Erro de execução')

    def do_guardar_nucleotide(self,arg):
        ''''
        > Procura a sequência pelo id da sequencia na base de dados Nucleotide do NCBI
        Variaveis : - nome a dar ao ficheiro devolvido -> <nome_para_ficheiro>
                    - id a pesquisar -> <id>
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print('Opção inválida')
            args = arg.split(' ')
            name = args[0]
            id = args[1]
            Random = ID(name, 'Nucleotide', 10, 'example@gmail.com', t_file, id)
            ID.Save_file(Random)
        except: print('Erro de execução')

    def do_guardar_protein(self, arg):
        '''
        > Procura a sequência pelo id da sequencia na base de dados Protein do NCBI
        Variaveis : - nome a dar ao ficheiro devolvido -> <nome_para_ficheiro>
                    - id a pesquisar -> <id>
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print('Opção inválida')
            args = arg.split(' ')
            name = args[0]
            id = args[1]
            Random = ID(name, 'Protein', 10, 'example@gmail.com', t_file, id)
            ID.Save_file(Random)
        except:
            print('Erro de execução')

    def do_procurar_id_swiss(self,arg):
        '''
        *** Apenas devolve ficheiros no formato .fasta ***
        > Procura a sequência pelo id da sequencia na base de dados Swiss Prot
        Variaveis : Recebidas ao longo execução da função
        Returns: Ficheiro .fasta com o resultado da procura na Swiss Prot
        '''
        print("Apenas devolve ficheiros no formato fasta")
        try:
            option = input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:')
            if option == '1':
                ORF3a = Prot_ID('P0DTC3')
                Prot_ID.get_prot(ORF3a)
            elif option == '2':
                FGA = Prot_ID('P02671')
                Prot_ID.get_prot(FGA)
            elif option == '3':
                FGB = Prot_ID('P02675')
                Prot_ID.get_prot(FGB)
            elif option == '4':
                FGG= Prot_ID('P02679')
                Prot_ID.get_prot(FGG)
            elif option == '5':
                print(" Necessário saber o id na base de dados na Swiss Prot ")
                id = input('Id a pesquisar: ')
                Random = Prot_ID(id)
                Prot_ID.get_prot(Random)
            else:
                print('Opção inválida')
        except:print('Erro de execução')

    def do_blast(self, arg1):
        '''
        ***É necessario possuir um ficheiro .fasta ou .gb com a sequência para realizar esta operação ***
        > Realiza o blast no NCBI à escolha do utilizador
        Variaveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>
                    - Ficheiro .fasta ou .gb que contém a sequência <input_file>
                    - Formato do ficheiro com a sequência <formato_do_input_file>
        Returns: Ficheiro .xml com o resultado do blast
        '''
        try:
            args = arg1.split(' ')
            name = args[0]
            file = args[1]
            format = args[2]
            Random = name + '_1'
            print(name, file, format)
            option = int(input('introduzir Blast a realizar: \n 1 - Blastp \n 2 - Blastn \n 3 - Blastx \n Opção:'))
            if option == 1:
                Random = Blast(name, str(file), 'blastp', str(format))
                Blast.blast(Random)
            elif option == 2:
                Random = Blast(name, file, 'blastn', format)
                Blast.blast(Random)
            elif option == 3:
                Random = Blast(name, file, 'blastx', format)
                Blast.blast(Random)
            else:
                print('Opção inválida')
        except:
            print('Erro de execução')

    def report_blast(self,arg):
        '''
        ***É necessario possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai para um ficheiro .txt com o report inteiro do blast
        Variaveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>
                    - Ficheiro .xml que contém o output do blast <input_file>
                    - Valor recebido para filtrar os resultador pelo e-value, (parametro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>
        Returns: Ficheiro .txt com o report do blast
        '''
        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = args[2]
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = name + '_1'
            Random = homologas(name,file,E_value)
            homologas.BLAST_REPORT(Random)
        except: print('Erro de execução')

    def homologia(self, arg):
        '''
        ***É necessario possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai a sequencia dos blast hits para um ficheiro .fasta
        Variaveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>
                    - Ficheiro .xml que contém o output do blast <input_file>
                    - Valor recebido para filtrar os resultador pelo e-value, (parametro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>
        Returns: Ficheiro .fasta contendo a sequência hit do blast
        '''
        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = args[2]
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = name + '_1'
            Random = homologas(name, file, E_value)
            homologas.File_hits(Random)
        except:
            print('Erro de execução')

    def homologo_AC(self, arg):
        '''
        ***É necessario possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai os Acession Number dos blast hits para um ficheiro .txt
        Variaveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>
                    - Ficheiro .xml que contém o output do blast <input_file>
                    - Valor recebido para filtrar os resultador pelo e-value, (parametro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>
        Returns: Ficheiro .txt com os Acession Numbers dos Blast Hits
        '''
        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = args[2]
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = name + '_1'
            Random = homologas(name, file, E_value)
            homologas.File_AC_hits(Random)
        except:
            print('Erro de execução')

    def fasta_homologos(self, arg):
        '''
        ***É necessario possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Procura as sequências dos blast hits pelos respetivos Acession Numbers na base de dados apropriada do NCBI
        Variaveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>
                    - Ficheiro .xml que contém o output do blast <input_file>
                    - Tipo sequencia utilizada no blast executado: Cadeias de nucleotidos >> Nut ou Cadeias de
                    aminoàcidos >> Ppt
                    - Valor recebido para filtrar os resultador pelo e-value, (parametro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>
        Returns: Ficheiro .fasta contendo as sequencias inteiras dos Hits resultantes do Blast.
        '''
        try:
            args = arg.split(' ')
            if len(args) == 4:
                name = args[0]
                file = args[1]
                tipo = args[2]
                E_value = args[3]
            elif len(args) == 3:
                name = args[0]
                file = args[1]
                tipo = args[2]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = name + '_1'
            Random = homologas(name, file, E_value)
            File2 = homologas.File_AC_hits(Random)
            if tipo == 'Nut':
                Random = Create_fasta(name, File2, 'Nucleotide')
            elif tipo == 'Ppt':
                Random = Create_fasta(name, File2, 'Protein')
            else:
                print('Argumentação errada!')
        except:
            print('Erro de execução')

    def do_alinhamento_multiplo(self, arg):
        '''
        ***É necessário possuir um ficheiro .fasta com sequencias para realizar esta operação ***
        > Realiza o Alinhamento Multiplo entre várias sequencias
        Variaveis : - Caminho para a diretoria onde está instalado o Clustalw2 <diretoria do clustalw2>
                    - Ficheiro .fasta que contém as varias sequencias para efetuar alinhamento <input_file>
        Returns: ***Tiago da aqui input***
        '''
        try:
            print(" É necessario possuir um ficheiro .fasta com as sequencias a alinhar para realizar esta operação")
            args = arg.split(' ')
            dir = args[0]
            file = args[1]
            Random = Mutiple(dir, file)
            Mutiple.alignment(Random)
        except:
            print('Erro de execução')

    def do_menu(self):
        print(self.intro)

    def do_sair(self, arg):
        print('Até depois!')
        return True
if __name__ == '__main__':
    shell().cmdloop()
