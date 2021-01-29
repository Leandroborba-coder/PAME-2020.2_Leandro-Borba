class Torneio:
    def __init__(self, nome_do_torneio='', arte_macial='', faixa='', peso=0):
        self.nome = nome_do_torneiro
        self.arte = arte_macial
        self.faixa = faixa
        self.peso = peso

    def dados(self):
        print(self.nome)
        print(self.arte)
        print(self.faixa)
        print(self.peso)

class Lutador:
    def __init__(self, nome='', idade=0, peso=0, força=0, faixa='', arte_macial=''):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.força= força
        self.faixa = faixa
        self.arte = arte_macial

    def dados(self):
        print(self.nome)
        print(self.idade)
        print(self.peso)
        print(self.força)
        print(self.faixa)
        print(self.arte)

temp_lutadores = []
lutadores = []

def menu():
    
    print('1- Menu de Torneio')
    print('2- Menu de Lutador')
    print('3- Criar Torneio Aleatório')
n = input('Entre com a opção desejada[1]- Menu de Torneiro,[2]- Menu de Lutador ou [3]- Criar Torneio Aleatório: ')


while True:
    if n in '1 2 3':
        break
        
    else:
        print('Opção inválida. Digite apenas um número')
        n = input('Entre com a opção desejada[1/2/3]: ')

if n == '1':

    print('1- Criar torneio'
             '\n2- Inscrever lutador'
             '\n3- Ver torneios existentes'
             '\n4- Ver ranking de torneio'
             '\n5- Ver lutadores inscritos em torneio existente'
             '\n6- Realizar luta')
        
    n1 = input('Escolha uma opção entre 1 e 6: ')

    if n1 == '1':
        print('Preencha as informaçõs para criar um torneio:')
        nome_do_torneio = input('Digite o nome do torneiro: ')

        arte_macial = input('Digite a arte macial desejada: ')

        faixa = input('Digite a faixa da arte macial desejada: ')

        peso = input('Escolha a faixa de peso do torneio:\n[1] 80kg - 90kg'
                  '\n[2]90kg - 100kg')

        print('PARABÉNS! Seu torneio foi cadastrado com sucesso! Abaixo, segue as informações registradas'
                '\n{}'
                '\n{}'
                '\n{}'
                '\n{}'.format(nome_do_torneio, arte_macial, faixa, peso))
        print('Você deseja voltar para o MENU PRINCIPAL?')
        n1 = input('[S]- Sim ou [N]- Não: ')
        if n1 == 'S':
            menu()
                
        elif n1 == 'N':
            print('Obrigado por usar nosso sistema!')
        

elif n == '2':
    print ('1- Cadastrar lutador'
           '\n2- Ver lutadores'
           '\n3- Ver detalhes de lutadores')

    n1 = input('Escolha uma opção entre 1 e 3: ') 

    if n1 == '1': #CADASTRAR LUTADOR #FALTA OS WHILES
        print('Preencha as informaçõs para cadastrar um lutador:')

        while True:

            temp_lutadores.append(str(input('nome: ')))

            temp_lutadores.append(int(input('Idade: ')))

            temp_lutadores.append(int(input('Peso: ')))

            temp_lutadores.append(int(input('Força: ')))
                
            temp_lutadores.append(str(input('Faixa: ')))

            temp_lutadores.append(str(input('Arte Macial: ')))

            lutadores.append(temp_lutadores[:])
            temp_lutadores.clear()
            

            resp = str(input('Deseja cadastrar outro lutador? [S/N]: '))
            if resp == 'N':
                print('Deseja retornar para o MENU PRINCIPAL?')
                resp_menu = input('[S]- Sim [N]- Não: ')
                
                    
                if resp_menu == 'S':
                   menu()
                
                        
                elif resp_menu == 'N':
                    print('Obrigado por utilizar nosso sistema!')
                    break

            elif resp == 'S':
                print(f'Os dados foram {lutadores}')
                
             
    
                           
                    
                

            


           
