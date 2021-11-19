
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
                batalhaZeusInicial()
                battlefield()
    elif(player == 'poseidon'):

                print('Boa escolha,Panteão. Você escolheu Poseidon, Rei dos mares e de todas suas criaturas.')
                batalhaPoseidonInicial()
                battlefield()
    elif(player == 'hades'):
                print('Boa escolha,Panteão. Você escolheu Hades, Rei do submundo e dos mortos.')
                batalhaHadesInicial()
                battlefield()
#selecione seu personagem    
 
#Bloco  batalhas Zeus
def batalhaZeusInicial():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Digite o nome de quem você irá enfrentar:\n 1-Humanos 2-Hades 3-Poseidon')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaZeusvenceHades():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Digite o nome de quem você irá enfrentar:\n 1-Humanos  2-Poseidon')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaZeusvencePoseidon():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Digite o nome de quem você irá enfrentar:\n 1-Humanos  2-Hades')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()  
    return enemy  

def batalhaZeusvenceHumanos():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Digite o nome de quem você irá enfrentar:\n 1-Hades  2-Poseidon')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy
#Bloco batalhas Zeus END

#Bloco Batalhas Hades
def batalhaHadesInicial():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Zeus 3-Poseidon') 
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaHadesVenceZeus():

    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Poseidon') 
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaHadesVenceHumanos():

    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Zeus 2-Poseidon') 
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaHadesVencePoseidon():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Zeus') 
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy
#Bloco Batalhas Hades Fim

#Bloco Batalhas Poseidon
def batalhaPoseidonInicial():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Hades 3-Zeus')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaPoseidonVenceHades():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Zeus')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaPoseidonVenceZeus():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Humanos 2-Hades')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy

def batalhaPoseidonVenceHumanos():
    global enemy
    print('Você irá enfrentar 3 batalhas contra seus irmãos e sua própria criação,os homens.')
    print('Escolha contra quem você quer lutar:\n 1-Hades 3-Zeus')
    enemy = input('')
    print(f'Você irá enfrentar {enemy}')
    enemy=enemy.lower()
    return enemy
    
        
#Bloco Batalhas Poseidon FINAL

    
    
#escolha contra quem irá lutar e onde
def battlefield():
    global campo
    campo = input('Escolha onde quer enfrentar seus inimigos:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
    campo = campo.lower()
    #OLIMPO
    if(campo == 'olimpo' and player == 'zeus' and enemy == 'hades'):#WIN
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaZeusvenceHades()
        if(campo == 'olimpo' or 'mundo inferior' or 'creta' and enemy == 'poseidon'):
            print('Você derrotou o Deus dos mares,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mares.')
            print('Restaram somente os Humanos para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'creta'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo=='olimpo' or 'mundo inferior' or 'oceano' and enemy == 'humanos'):
                print('Você derrotou sua criação e agora Creta também engrandece seu poder.')
                print('Você enfrentará seu irmão como último inimigo.')
                campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
                campoFinal = campoFinal.lower
                if(campoFinal != 'oceano'):
                    print('Você ganhou!')
                else:
                    print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo.')
    elif(campo == 'olimpo' and player == 'zeus' and enemy == 'poseidon'):#WIN
        print('Parábens,Você derrotou o senhor dos oceanos e todos os mares. Agora você também é fortalecido pelas águas.')
        batalhaZeusvencePoseidon()
        if(campo != 'mundo inferior'  and enemy == 'hades'):
            print('Você derrotou o Deus dos mortos,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mortos.')
            print('Restaram somente os Humanos para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'creta'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'creta' and enemy == 'humanos'):
                print('Você derrotou sua criação e agora Creta também engrandece seu poder.')
                print('Você enfrentará seu irmão Poseidon como último inimigo.')
                campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
                campoFinal = campoFinal.lower
                if(campoFinal != 'oceano'):
                    print('Você ganhou!')
                else:
                    print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo.')        
    elif(campo == 'olimpo' and player == 'zeus' and enemy == 'humanos'):#WIN
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaZeusvenceHumanos()
        if(campo != 'oceano' and enemy == 'poseidon'):
            print('Você derrotou o Deus dos mares,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mares.')
            print('Restou somente Hades para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'mundo inferior'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'mundo inferior'  and enemy == 'hades'):
            print('Você derrotou o Deus dos mortos,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mortos.')
            print('Restou Poseidon para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'oceano'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
    elif(campo == 'olimpo' and player == 'poseidon' and enemy == 'zeus'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'olimpo' and player == 'poseidon' and enemy == 'hades'):
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaPoseidonVenceHades()
        if(campo != 'oceano' and enemy == 'poseidon'):
            print('Você derrotou o Deus dos mares,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mares.')
            print('Restou somente sua criação para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'creta'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'mundo inferior'  and enemy == 'hades'):
            print('Você derrotou o Deus dos mortos,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mortos.')
            print('Restou Zeus para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'olimpo'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
    elif(campo == 'olimpo' and player == 'poseidon' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaPoseidonVenceHumanos()
        if(campo != 'olimpo' and enemy == 'zeus'):
            print('Você derrotou o Deus dos Deuses,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos Deuses.')
            print('Restou somente Hades para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'mundo inferior'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'mundo inferior'  and enemy == 'hades'):
            print('Você derrotou o Deus dos mortos,restando somente sua criação a ser derrotada. Você também tornou-se o novo Deus dos mortos.')
            print('Restou Zeus para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'olimpo'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')

    elif(campo == 'olimpo' and player == 'hades' and enemy == 'zeus'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'olimpo' and player == 'hades' and enemy == 'poseidon'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaHadesVencePoseidon()
        if(campo != 'olimpo' and enemy == 'zeus'):
            print('Você derrotou o Deus dos Deuses. Você também tornou-se o novo Deus dos Deuses.')
            print('Restou somente a humanidade para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'creta'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'creta'  and enemy == 'humanos'):
            print('Você derrotou sua criação.')
            print('Restou Zeus para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'olimpo'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
    elif(campo == 'olimpo' and player == 'hades' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaHadesVenceHumanos()
        if(campo != 'olimpo' and enemy == 'zeus'):
            print('Você derrotou o Deus dos Deuses. Você também tornou-se o novo Deus dos Deuses.')
            print('Restou somente Poseidon para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'Oceano'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')
        elif(campo != 'Oceano'  and enemy == 'Poseidon'):
            print('Você derrotou seu irmão.')
            print('Restou Zeus para enfrentar')
            campoFinal = input('Escolha onde quer enfrentar seus inimigos pela ultima vez:\n 1-Olimpo 2-Creta 3-Oceano 4-Mundo inferior: ')
            campoFinal = campoFinal.lower
            if(campoFinal != 'olimpo'):
                print('Você ganhou!')
            else:
                print('Você está poderoso,porém até mesmo Deuses caem. Fim de jogo')

    #OCEANO

    elif(campo == 'oceano' and player == 'poseidon' and enemy == 'hades'):
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaPoseidonVenceHades()
    elif(campo == 'oceano' and player == 'poseidon' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaPoseidonVenceZeus()
    elif(campo == 'oceano' and player == 'poseidon' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaPoseidonVenceHumanos()
    elif(campo == 'oceano' and player == 'hades' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaHadesVenceZeus()
    elif(campo == 'oceano' and player == 'hades' and enemy == 'poseidon'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'oceano' and player == 'hades' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaHadesVenceHumanos()
    elif(campo == 'oceano' and player == 'zeus' and enemy == 'hades'):
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaZeusvenceHades()
    elif(campo == 'oceano' and player == 'zeus' and enemy == 'poseidon'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'oceano' and player == 'zeus' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaZeusvenceHumanos()
    #MUNDO_INFERIOR

    elif(campo == 'mundo inferior' and player == 'hades' and enemy == 'poseidon'):
        print('Parábens,Você derrotou o senhor dos oceanos e todos os mares. Agora você também é fortalecido pelas águas.')
        batalhaHadesVencePoseidon()

    elif(campo == 'mundo inferior' and player == 'hades' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaHadesVenceZeus()
    elif(campo == 'mundo inferior' and player == 'hades' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaHadesVenceHumanos()
    elif(campo == 'mundo inferior' and player == 'poseidon' and enemy == 'hades'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'mundo inferior' and player == 'poseidon' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaPoseidonVenceZeus()
    elif(campo == 'mundo inferior' and player == 'poseidon' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaPoseidonVenceHumanos()
    elif(campo == 'mundo inferior' and player == 'zeus' and enemy == 'poseidon'):
        print('Parábens,Você derrotou o senhor dos oceanos e todos os mares. Agora você também é fortalecido pelas águas.')
        batalhaZeusvencePoseidon()
    elif(campo == 'mundo inferior' and player == 'zeus' and enemy == 'hades'):#ENDGAME
        print('Você enfrentou seu irmão em sua casa e por isto padeceu. Fim de jogo.')
        
    elif(campo == 'mundo inferior' and player == 'zeus' and enemy == 'humanos'):
        print('Parábens,Você derrotou sua criação. Agora tem mais força pelos tributos ofertados por ela.')
        batalhaZeusvenceHumanos()

    #CRETA
    elif(campo == 'creta' and player == 'hades' and enemy == 'poseidon'):
        print('Parábens,Você derrotou o senhor dos oceanos e todos os mares. Agora você também é fortalecido pelas águas.')
        batalhaHadesVencePoseidon()
    elif(campo == 'creta' and player == 'hades' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaHadesVenceZeus()
    elif(campo == 'creta' and player == 'hades' and enemy == 'humanos'):#ENDGAME
        print('Você enfrentou sua criação em seu território e por isto padeceu. Fim de jogo.')
    elif(campo == 'creta' and player == 'poseidon' and enemy == 'hades'):
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaPoseidonVenceHades()
    elif(campo == 'creta' and player == 'poseidon' and enemy == 'zeus'):
        print('Parábens,Você derrotou o Deus dos Deuses e agora também está muito mais forte no Olimpo.')
        batalhaPoseidonVenceZeus()
    elif(campo == 'creta' and player == 'poseidon' and enemy == 'humanos'):#ENDGAME
        print('Você enfrentou sua criação em seu território e por isto padeceu. Fim de jogo.')
    elif(campo == 'creta' and player == 'zeus' and enemy == 'hades'):
        print('Parábens,Você derrotou o senhor das trevas e agora também está muito mais forte no Mundo inferior.')
        batalhaZeusvenceHades()
    elif(campo == 'creta' and player == 'zeus' and enemy == 'poseidon'):
        print('Parábens,Você derrotou o senhor dos oceanos e todos os mares. Agora você também é fortalecido pelas águas.')
        batalhaZeusvencePoseidon()
    elif(campo == 'creta' and player == 'zeus' and enemy == 'humanos'):#ENDGAME
        print('Você enfrentou sua criação em seu território e por isto padeceu. Fim de jogo.')
        


            
    
    
        

        

    



begin()
selectCharacter()