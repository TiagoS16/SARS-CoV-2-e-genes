from cmd import *
from ID import ID, Prot_ID, Get_info, Pubmed
from Blast import Blast
from Homologas import homologas
from FASTA_Multiple import Create_fasta
from Multiple_Alignment import Mutiple
from PDB_F import PDB
from Phylo import Phylo
from Analise_multipla import Align, hist

class shell(Cmd):
    intro = ''' \n Comandos da Shell:
************************************************************************************************************************           
        * procurar_id_nucleotide -> Realizar uma procura na database Nucleotide NCBI e guardar ficheiro correspondente 
        ou guardar ficheiro através do id fornecido.
        * procurar_id_protein -> Realizar uma procura na database Protein NCBI e guardar ficheiro correspondente ou 
        guardar ficheiro através do id fornecido.
        * info_genbank <input_file> - Imprime na consola a informação contia no ficheiro genbank .
        * pubmed_search <nome> <query> <resultados> - Procurar no Pubmed por relevancia artigos associados à query.
        * procurar_id_swiss -> Guardar ficheiro fasta a partir do id na database Swiss Prot.
        * estrutura_proteina -> Obter a estrutura 3D da proteina através do id na database PDB.
        * blast <nome> <input_file> <formato_do_input_file> -> Realizar o blast (blastn, blastp, blastx).
        * report_blast <nome> <input_file_blast> <E-value threshold (opcional)> -> Obter um relatório resumo do Blast.
        * homologia <nome> <input_file_blast> <E-value threshold (opcional)> -> Obter os hits obtidos no 
        blast realizado.
        * homologo_AC <nome> <input_file_blast> <E-value threshold(opcional)> -> Obter os Acession Numbers 
        dos hits obtidos no blast realizado.
        * fasta_homologos <nome> <input_file_blast> <(nt/ppt)> <E-value threshold(opcional)> -> Obter a 
        sequência total dos hits através dos Acession Numbers dos hits obtidos no blast realizado.
        * alinhamento_multiplo <diretoria do Clustalw2(opcional)> <input_file> -> Alinhamento Multiplo entre sequências 
        contidas num ficheiro .fasta através do Clustalw2.
        * arvore_filogenetica <input_file> -> Construção da árvore filogenética apartir do ficheiro resultante do 
        Alinhamento Multiplo. 
        * analise_alinhamento <nome> <input_file> -> Análise do resultado do Alinhamento Multiplo.
        * tabela_substituição <nome> <input_file> -> Tabela de substituição do Alinhamento Multiplo.
        * histograma <input_file> -> Construção do histograma com a distribuição de comprimentos das sequências contidas 
        num ficheiro .fasta.
        
        * sair -> sair da função
                                                                        
                    Prima < ? comando > para mais informações acerca do comando                                          
************************************************************************************************************************
'''
    prompt = 'Lab > '
    def do_procurar_id_nucleotide(self,arg):
        ''''
        > Procura a sequência para uma query na base de dados Nucleotide do NCBI.
        Variáveis : Recebidas ao longo execução da função.
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função.
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print("Tipo de ficheiro inválido")
            SV_SRC = int(input('Operação a realizar: \n 1 - Procurar id na database Nucleotide NCBI para uma pesquisa e guardar ficheiro \n 2 - guardar ficheiro apartir do id na database Nucleotide NCBI \nOpção:'))
            if SV_SRC == 1:
                option = int(input('Introduzir query a pesquisar: \n 1 - ORF3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
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
            elif SV_SRC == 2:
                id = input('Introduzir id na database \n')
                name = id + '.txt'
                Random = ID(name, 'Nucleotide', 10, 'example@gmail.com', t_file, id)
                ID.Save_file(Random)
            else:
                print("Opção inválida!")

        except: print('Erro de execução')

    def do_procurar_id_protein(self, arg):
        ''''
        > Procura a sequência para uma query na base de dados Protein do NCBI.
        Variáveis : Recebidas ao longo execução da função.
        Returns: Ficheiro .fasta ou .gb dependendo da escolha do operador a executar a função.
        '''
        try:
            file = int(input('tipo de ficheiro a obter: \n 1- fasta \n 2 - genbank \n Opção: '))
            if file == 1:
                t_file = 'fasta'
            elif file == 2:
                t_file = 'gb'
            else:
                print("Tipo de ficheiro inválido")
            SV_SRC = int(input('Operação a realizar: \n 1 - Procurar id na database Nucleotide NCBI para uma pesquisa e guardar ficheiro \n 2 - guardar ficheiro apartir do id na database Nucleotide NCBI \nOpção:'))
            if SV_SRC == 1:
                option = int(input('Introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
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
            elif SV_SRC == 2:
                id = input('Introduzir id na database \n')
                name = id + '.txt'
                Random = ID(name, 'Protein', 10, 'example@gmail.com', t_file, id)
                ID.Save_file(Random)
            else:
                print('Opção inválida')

        except: print('Erro de execução')

    def do_Info_genbank(self, arg):
        '''
        *** É necessario um genbank para realizar esta operação ***
        Variáveis:  - Ficheiro no formato genbank <input_file>.
        Returns: Imprime na consola a informação presente no genbank.
        '''
        Random = Get_info(arg)
        Get_info.gb_inf(Random)

    def do_Pubmed_search(self,arg):
        '''
        Variáveis:  - Nome para o ficheiro devolvido pela função <nome>, extensão adicionada automaticamente. Pubmed_<nome>.txt
                    - query a pesquisar <query>.
                    - numero máximo de resultados a devolver pelo Pubmed <resultados>.
        Returns: Cria um .txt com a informação dos hits.
        '''
        try:
            print("Iniciar processo...")
            args = arg.split(' ')
            name = args[0]
            query = ''
            for i in range(1,len(args)-1):
                query = query + ' ' + args[i]
            res = args[len(args)-1]
            Random = Pubmed(name, query, res)
            Pubmed.procura(Random)
        except:
            print('Erro de execução')

    def do_procurar_id_swiss(self,arg):
        '''
        *** Apenas devolve ficheiros no formato .fasta ***
        > Procura a sequência pelo id da sequência na base de dados Swiss Prot.
        Variáveis : Recebidas ao longo execução da função.
        Returns: Ficheiro .fasta com o resultado da procura na Swiss Prot.
        '''
        print("Apenas devolve ficheiros no formato fasta")
        try:
            option = int(input('introduzir query a pesquisar: \n 1 - Orf3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
            if option == 1:
                ORF3a = Prot_ID('P0DTC3')
                Prot_ID.get_prot(ORF3a)
            elif option == 2:
                FGA = Prot_ID('P02671')
                Prot_ID.get_prot(FGA)
            elif option == 3:
                FGB = Prot_ID('P02675')
                Prot_ID.get_prot(FGB)
            elif option == 4:
                FGG= Prot_ID('P02679')
                Prot_ID.get_prot(FGG)
            elif option == 5:
                print(" Necessário saber o id na base de dados na Swiss Prot ")
                id = input('Id a pesquisar: ')
                Random = Prot_ID(id)
                Prot_ID.get_prot(Random)
            else:
                print('Opção inválida')
        except:print('Erro de execução')

    def do_estrutura_proteina(self,arg):
        '''
        *** Para utlizar esta função é necessário ter o software Pymol instalado localmente ***
        > Obtem imagem 3D da proteina através do PDB.
        Variáveis : Recebidas ao longo execução da função.
        Returns: Imagem da estrutura 3D.
        '''
        try:
            option = int(input('introduzir query a pesquisar: \n 1 - ORF3a \n 2 - FGA \n 3 - FGB \n 4 - FGG \n 5 - outro não predefinido \n Opção:'))
            if option == 1:
                ORF3a = PDB('6XDC')
                PDB.PDB(ORF3a)
            elif option == 2:
                FGA = PDB('1L39')
                PDB.PDB(FGA)
            elif option == 3:
                FGB = PDB('1FZA')
                PDB.PDB(FGB)
            elif option == 4:
                FGG = PDB('1DUG')
                PDB.PDB(FGG)
            elif option == 5:
                id = input('Id do PBD a pesquisar : ')
                Random = PDB(id)
                PDB.PDB(Random)
            else:
                print('Opção inválida')
        except: print('Erro de execução')

    def do_blast(self, arg1):
        '''
        *** É necessário possuir um ficheiro .fasta ou .gb com a sequência para realizar esta operação ***
        > Realiza o blast no NCBI à escolha do utilizador.
        Variáveis : - Nome para o ficheiro devolvido pela função <nome>, a extensão é adicionada automaticamente. <nome>.xml
                    - Ficheiro .fasta ou .gb que contém a sequência <input_file>.
                    - Formato do ficheiro com a sequência *(fasta ou gb)* <formato_do_input_file>.
        Returns: Ficheiro .xml com o resultado do blast.
        '''
        try:
            args = arg1.split(' ')
            if len(args) != 3:
                print('Argumentação errada')
            else:
                name = args[0]
                file = args[1]
                format = args[2]
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

    def do_report_blast(self,arg):
        '''
        ***É necessário possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai para um ficheiro .txt com o report inteiro do blast.
        Variáveis : - Nome para o ficheiro devolvido pela função <nome>, a extensão é adicionada automaticamente. Report_<nome>.txt
                    - Ficheiro .xml que contém o output do blast <input_file_blast>.
                    - Valor recebido para filtrar os resultados pelo e-value, (parâmetro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>.
        Returns: Ficheiro .txt com o report do blast.
        '''

        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = float(args[2])
                print(args)
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            print(name, file, E_value)
            Random = homologas(name,file, E_value)
            homologas.BLAST_REPORT(Random)
        except: print('Erro de execução')

    def do_homologia(self, arg):
        '''
        ***É necessário possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai a sequência dos blast hits para um ficheiro .fasta.
        Variáveis : - Nome para o ficheiro devolvido pela função <nome>, a extensão é adicionada automaticamente. SeqsHomo_<nome>.fasta
                    - Ficheiro .xml que contém o output do blast <input_file>.
                    - Valor recebido para filtrar os resultador pelo e-value, (parâmetro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>.
        Returns: Ficheiro .fasta contendo a sequência hit do blast.
        '''
        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = float(args[2])
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = homologas(name, file, E_value)
            homologas.File_hits(Random)
        except:
            print('Erro de execução')

    def do_homologo_AC(self, arg):
        '''
        ***É necessário possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Extrai os Acession Number dos blast hits para um ficheiro .txt.
        Variáveis : - Nome para o ficheiro devolvido pela função <nome>, a extensão é adicionada automaticamente. ACHomo_<nome>.txt
                    - Ficheiro .xml que contém o output do blast <input_file>.
                    - Valor recebido para filtrar os resultador pelo e-value, (parâmetro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>.
        Returns: Ficheiro .txt com os Acession Numbers dos Blast Hits.
        '''
        try:
            args = arg.split(' ')
            if len(args) == 3:
                name = args[0]
                file = args[1]
                E_value = float(args[2])
            elif len(args) == 2:
                name = args[0]
                file = args[1]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = homologas(name, file, E_value)
            homologas.File_AC_hits(Random)
        except:
            print('Erro de execução')

    def do_fasta_homologos(self, arg):
        '''
        ***É necessário possuir um ficheiro .xml com o resultado do blast para realizar esta operação ***
        > Procura as sequências dos blast hits pelos respetivos Acession Numbers na base de dados apropriada do NCBI.
        Variáveis : - Nome para o ficheiro devolvido pela função <nome_para_ficheiro>, a extensão é adicionada automaticamente. <nome>_complseqs_AC.fasta
                    - Ficheiro .xml que contém o output do blast <input_file>.
                    - Tipo sequência utilizada no blast executado: Cadeias de nucleotídos >> nt ou Cadeias de
                    aminoàcidos >> ppt.
                    - Valor recebido para filtrar os resultador pelo e-value, (parâmetro opcional) senão colocado
                    recebe o valor de 0.05 <E-value threshold>.
        Returns: Ficheiro .fasta contendo as sequências inteiras dos Hits resultantes do Blast.
        '''
        try:
            args = arg.split(' ')
            if len(args) == 4:
                name = args[0]
                file = args[1]
                tipo = args[2]
                E_value = float(args[3])
            elif len(args) == 3:
                name = args[0]
                file = args[1]
                tipo = args[2]
                E_value = None
            else:
                print('Argumentação errada!')
            Random = homologas(name, file, E_value)
            File2 = homologas.File_AC_hits(Random)
            if tipo == 'nt':
                Random2 = Create_fasta(name, File2, 'Nucleotide')
                Create_fasta.m_blast(Random2)
            elif tipo == 'ppt':
                Random3 = Create_fasta(name, File2, 'Protein')
                Create_fasta.m_blast(Random3)
            else:
                print('Argumentação errada!')
        except:
            print('Erro de execução')

    def do_alinhamento_multiplo(self, arg):
        '''
        *** É necessário possuir um ficheiro .fasta com sequências e possuir o Clustalw2 instalado localmente para realizar esta operação ***
        > Realiza o Alinhamento Multiplo entre várias sequências.
        Variáveis : - Caminho para a diretoria onde está instalado o Clustalw2 , parâmetro opcional senão colocado  recebe o caminho default
                    de instalação (OS - Windows10) <diretoria do clustalw2>.
                    - Ficheiro .fasta que contém as varias sequências para efetuar alinhamento <input_file>.
        Returns: Cria dois ficheiros (.aln e .dnd) com o resultado do alinhamento multiplo.
        '''
        try:
            args = arg.split(' ')
            if len(args) > 1:
                inp = args[0:len(args)-1]
                dir = ''
                for i in inp:
                    dir += i + ' '
                file = args[len(args)-1]
                Random = Mutiple(dir, file)
                Mutiple.alignment(Random)
            else:
                dir = 'C:\Program Files (x86)\ClustalW2\clustalw2.exe'
                file = args[0]
                Random = Mutiple(dir, file)
                Mutiple.alignment(Random)
        except:
            print('Erro de execução')

    def do_arvore_filogenetica(self, arg):
        '''
        ***É necessário possuir um ficheiro .dnd resultante de um alinhamento para realizar esta operação ***
        > Realiza o Alinhamento Multiplo entre várias sequências.
        Variáveis : - Ficheiro .dnd que contém o resultado do alinhamento alinhamento <input_file>.
        Returns: Imprime a árvore filogenética na consola e gera imagen .png correspondente.
        '''
        try:
            args = arg.split(' ')
            if len(args) != 1:
                print('Parâmetros errados')
            else:
                file = args[0]
                Random = Phylo(file)
                Phylo.obter_arvore(Random)
        except:
            print('Erro de execução')

    def do_analise_alinhamento(self,arg):
        '''
        ***É necessário possuir um ficheiro .aln resultante de um alinhamento para realizar esta operação ***
        > Realiza o Alinhamento Multiplo entre várias sequências.
        Variáveis : - Nome para o ficheiro obtido <name>, a extensão é adicionada automaticamente. <nome>_sumali.txt
                    - Ficheiro .aln que contém o resultado do alinhamento alinhamento <input_file>.
        Returns: Obtem ficheiro .txt com o resumo do alinhamento.
        '''
        try:
            args = arg.split(' ')
            if len(args) != 2:
                print('Parâmetros errados')
            else:
                nome = args[0]
                file = args[1]
                Random = nome + '_1'
                Random = Align(nome, file)
                Align.summary_alinhamento(Random)
        except:
            print('Erro de execução')

    def do_tabela_substituição(self,arg):
        '''
        ***É necessário possuir um ficheiro .aln resultante de um alinhamento para realizar esta operação ***
        > Realiza o Alinhamento Multiplo entre várias sequências.
        Variáveis : - nome para o ficheiro de output <name>, a extensão é adicionada automaticamente. <nome>_tabali.txt
                    - Ficheiro .aln que contém o resultado do alinhamento alinhamento <input_file>.
        Returns: obtem ficheiro .txt com a tabela de substituição do alinhamento.
        '''
        try:
            args = arg.split(' ')
            if len(args) != 2:
                print('Parâmetros errados')
            else:
                nome = args[0]
                file = args[1]
                Random = Align(nome, file)
                Align.table_alinhamento(Random)
        except:
            print('Erro de execução')

    def do_histograma(self, arg):
        '''
        > Realiza o Alinhamento Multiplo entre várias sequências.
        Variáveis : - Ficheiro .fasta que contém as sequências utilizadas alinhamento alinhamento <input_file>.
        Returns: Obtém-se o histograma do tamanho das sequências.
        '''
        try:
            args = arg.split(' ')
            if len(args) != 1:
                print('Parâmetros errados')
            else:
                Random = hist(args[0])
                hist.histogram(Random)
        except:
            print('Erro de execução')

    def do_menu(self,arg):
        print(self.intro)

    def do_sair(self, arg):
        print('Até depois!')
        return True
if __name__ == '__main__':
    shell().cmdloop()
