def begin():
    print('Antes mesmo da história surgir, os titãs dominavam a Terra.')
    print('O maior deles,Cronos,teve 5 filhos: Demétra,Hera,Zeus,Poseidon e Hades.\nCronos havia comido 4 de seus filhos,porém foi enganado por sua esposa,Reia que com pena de ver mais um de seus filhos comido por Cronos,\no esconde com a ajuda da titã Gaia que cuida de Zeus até que o mesmo ficasse adulto.\n Em sua maioridade,Zeus faz uma mistura de mel e mostarda que Cronos viria a comer e vomitar seus irmãos que,como Deuses,\n estavam vivos durante todo o tempo em seu estômago.\n Ali,começaria a grande batalha entre Deuses e titãs.\n Por fim os Deuses venceram e para definir quem iria dominar os céus,os mares e o submundo os três irmãos Zeus,Poseidon e Hades \nescolhem um graveto e aquele que tirasse o maior pedaço dominaria os céus e quem tirasse o menor ficaria responsável pelo submundo.\nZeus escolhe o maior graveto e torna-se o imperador do Olimpo, os céus e os Deuses,Poseidon tornou-se o Rei dos mares e de todas as suas criaturas e seu irmão Hades torna-se o Imperador dos mortos e do submundo.')
    print('Apesar dos titãs terem sido derrotados,os grandes irmãos continuam a brigar entre si pela dominação do mundo e cabe a você decidir o vencedor.')
#inicio do game
def selectCharacter():
    global player
    player = input('Escolha qual dos três grandes irmãos você vai querer jogar:Zeus,Hades ou Poseidon\n ')    
    player = player.lower()
    if (player == 'zeus' ):
                print('Boa escolha,Panteão. Você escolheu Zeus, Rei dos céus e pai dos deuses.')
                batalhaZeus()
                battlefield()
    elif(player == 'poseidon'):
                print('Boa escolha,Panteão. Você escolheu Poseidon, Rei dos mares e de todas suas criaturas.')
                batalhaPoseidon()
                battlefield()
    elif(player == 'hades'):
                print('Boa escolha,Panteão. Você escolheu Hades, Rei do submundo e dos mortos.')
                batalhaHades()
                battlefield()
#selecione seu personagem       
def batalhaZeus():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Digite o nome de quem você irá enfrentar:\n 1-Humanos 2-Hades 3-Poseidon')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
def batalhaHades():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Zeus 3-Poseidon') 
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()   
def batalhaPoseidon():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Hades 3-Zeus')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    
#escolha contra quem irá lutar e onde
def battlefield():
    global campo
    campo = input('Escolha onde quer enfrentar seus inimigos:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
    campo = campo.lower()
    if (campo == 'olimpo' and enemy == 'zeus'):
        print(f'Zeus está em sua casa,neste local ele reina e nada supera seu poder. Você venceu {player} e agora domina tudo aquilo que estava sob seu poder.')
    elif(campo == 'creta' and enemy == 'humanidade'):
        print(f'A humanidade está em sua casa,neste local ela reina e você perdeu.')
    elif(campo == 'oceano' and enemy == 'poseidon'):
        print('Você entrou no reino do deus dos mares e por tamanha insolência morrerá. Você perdeu.')
    elif(campo == 'mundo inferior' and enemy == 'hades'):
         print('Você desafiou o Senhor dos mortos em seu palácio. Agora se tornará um daqueles que está sob seu poder. Você perdeu.')   
    elif(campo == 'oceano' and enemy != 'poseidon'):
         print(f'Você derrotou {enemy} e agora está em posse de seus domínios.') 
    elif(campo == 'olimpo' and enemy != 'zeus'):
         print(f'Você derrotou {enemy} e agora está em posse de seus domínios.')     
    elif(campo == 'mundo inferior' and enemy != 'hades'):
        print(f'Você derrotou {enemy} e agora está em posse de seus domínios.')    


begin()
selectCharacter()