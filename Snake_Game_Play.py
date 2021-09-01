# UNIVERSIDADE FEDERAL DO CEARÁ - Campus Russas
# Grupo Píton:

# Antônio Carolino Araújo Neto - 508768
# Guilherme Pereira Germano - 507902
# Júlia Freitas Santos - 511176
# Rhaiane de Sousa Silva - 514831
# Vitoria Ana Lima Crispim - 508674

# Bibliotecas e módulos utilizados

import pygame # Módulo pygame (para desenvolvimento de jogos)
from pygame.locals import * # Biblioteca interna do pygame
from sys import exit # Biblioteca utilizada para trabalhar com as configurações estabelecidas no código, importando a função exit()
from random import randint # Módulo random, importando a função randint()

# Inicialização do programa através da configuração do ambiente da partida e da jogabilidade selecionada pelo jogador

print('====================================================== Que comecem os jogos! =============================================================')

while True: # looping para estabelecer o nível de dificuldade do jogo

    try: # tratamento de erro

        pergunta_modo_de_jogo = int(input('Por favor Bro, escolha o modo de jogo (digite 1 p/ fácil, 2 p/ médio e 3 p/ difícil).')) # variável para receber o modo de jogo
        if pergunta_modo_de_jogo < 1 or pergunta_modo_de_jogo > 3:
            print("Por favor, escolha um nível de dificuldade existente!")

        else:
            break

    except (ValueError, TypeError): # teste para avaliar se o valor selecionado corresponde a um número inteiro

        print("Por favor, digite um número inteiro entre 1 a 3.")

while True: # looping para selecionar o plano de fundo do jogo

    try: # tratamento de erro

        pergunta_cenario_de_jogo = int(input('Por favor Bro, escolha o cenário do jogo (digite 1 p/ pântano normal, 2 p/ pântano noturno, 3 p/ zoológico, 4 p/ ilha, 5 p/ neve, 6 p/ deserto 7 p/ cavernas).')) # variável para receber o cenário do jogo
        if pergunta_cenario_de_jogo < 1 or pergunta_cenario_de_jogo > 7:
            print("Por favor, escolha uma paisagem existente!")

        else:
            break

    except (ValueError, TypeError): # teste para avaliar se o valor selecionado corresponde a um número inteiro

        print("Por favor, digite um número inteiro entre 1 a 7.")

while True: # looping para escolher a cor da cobra

    try: # tratamento de erro

        pergunta_cor_da_cobra = int(input('Por favor Bro, escolha a cor da cobra (digite 1 p/ verde, 2 p/ vermelho, 3 p/ amarelo e 4 p/ azul).')) # variável para receber a coloração da cobra
        if pergunta_cor_da_cobra < 1 or pergunta_cor_da_cobra > 4:
            print("Por favor, escolha uma cor válida!")

        else:
            break

    except (ValueError, TypeError): # teste para avaliar se o valor selecionado corresponde a um número inteiro

        print("Por favor, digite um número inteiro entre 1 a 4.")

# Funções auxiliares para configurar as condições de jogabilidade e de ambientação

def escolher_modo(pergunta): # Método para implementar o modo de dificuldade selecionado
    modo = []
    vel = comprimento = 0 # variáveis de velocidade e comprimento inicial da cobra, respectivamente
    if pergunta == 1:
        vel = 10
        comprimento = 15
        modo.append((vel, comprimento))
    elif pergunta == 2:
        vel = 15
        comprimento = 10
        modo.append((vel, comprimento))
    elif pergunta == 3:
        vel = 20
        comprimento = 5
        modo.append((vel, comprimento))

    return modo[0] # retorna a tupla de valores selecionados para a velocidade e o coprimento inicial da cobra

def escolher_cenario(cenarios, pergunta): # Método para implementar o cenário selecionado
    cenario = cenarios[pergunta - 1]
    return cenario # retorna o nome do cenário escolhido pelo usuário

def escolher_cor(pergunta): # Método para implementar a coloração determinada pelo jogador
    cor = []
    if pergunta == 1:
        cor.append((0, 255, 0))
    elif pergunta == 2:
        cor.append((255, 0, 0))
    elif pergunta == 3:
        cor.append((255, 255, 0))
    elif pergunta == 4:
        cor.append((0, 0, 255))

    return cor[0] # retorna a tupla com os valores da cor escolhida para a cobra

def rand_petisco(lista_comidas): # Método para selecionar aleatoriamente o próximo alimento a ser devorado pela cobra (podendo ser uma das 4 frutas ou um rato)
    tamanho = []
    petisco = randint(1, 5) # função randint() para sortear 1 dos 5 alimentos para aparecer na tela do jogo (1 = maçã, 2 = banana, 3 = uvas, 4 = melancia e 5 = rato)
    if petisco == 1:
        tamanho.append((35, 35)) # tupla com as dimensões da maçã sendo inserida na lista "tamanho"
    elif petisco == 2:
        tamanho.append((35, 35)) # tupla com as dimensões da banana sendo inserida na lista "tamanho"
    elif petisco == 3:
        tamanho.append((35, 35)) # tupla com as dimensões das uvas sendo inserida na lista "tamanho"
    elif petisco == 4:
        tamanho.append((35, 35)) # tupla com as dimensões da melancia sendo inserida na lista "tamanho"
    elif petisco == 5:
        tamanho.append((40, 30)) # tupla com as dimensões do roedor sendo inserida na lista "tamanho"

    comida = [lista_comidas[petisco - 1], tamanho[0]]
    return comida # retorna a lista contendo o nome do próximo alimento e o seu respectivo tamanho (tupla)

# Inicialização do jogo após a seleção e implementação das condições de contorno iniciais

pygame.init() # início do jogo

pygame.mixer.music.set_volume(0.3) # adequar o áudio do jogo
musica_do_jogo = pygame.mixer.music.load('Music-pygame.mp3') # estabelecer a trilha sonora do game
pygame.mixer.music.play() # ativando a faixa configurada

som_mordida = pygame.mixer.Sound('Bite.wav') # faixa selecionada para representar o som da mordida da cobra ao consumir uma comida
som_fim_de_jogo = pygame.mixer.Sound('Game over.wav') # faixa selecionada para representar o final da partida (quando o usuário perde)

largura = 640 # largura da tela
altura = 480 # altura da tela

x_cobra = int(largura / 2) # abscissa inicial da cobra
y_cobra = int(altura / 2) # ordenada inicial da cobra

velocidade = escolher_modo(pergunta_modo_de_jogo)[0] # variável para receber a velocidade selecionada pelo usuário (conforme a dificuldade escolhida)
x_controle = velocidade # variável de mobilidade da cobra no eixo "x" (eixo inicial de movimentação, na primeira partida do game)
y_controle = 0 # variável de mobilidade da cobra no eixo "y" (eixo inicial de repouso, na primeira partida do game)

x_food = randint(40, 600) # abscissa inicial da comida
y_food = randint(60, 430) # ordenada inicial da comida

pontuacao = 0 # pontuação inicial do jogador, zerando no final de cada partida
recorde = 0 # pontuação mais alta atingida pelo jogador durante todas as partidas realizadas durante a sessão do game

fonte1 = pygame.font.SysFont('arial', 30, bold=True) # fonte de escrita selecionada para escrever na tela durante a partida

tela = pygame.display.set_mode((largura, altura)) # variável de configuração da tela do jogo
pygame.display.set_caption('Jogo da Cobrinha') # título do game
relogio = pygame.time.Clock() # timer do jogo
comprimento_inicial = escolher_modo(pergunta_modo_de_jogo)[1] # tamanho inicial da cobra (quanto mais difícil, menor será o comprimento inicial)
perdeu = False # variável para sinalizar quando o jogador perder
lista_cobra = [] # lista para receber os elementos de formação da cobra (drawings = "desenhos")
lista_cenarios = ['Swamp.jpg', 'Noturno.jpg', 'zoo.jpg', 'Praia.jpg', 'Inverno.jpg', 'Deserto.jpg', 'Cave.jpg'] # lista contendo as paisagens disponíveis
lista_comidas = ["Apple-pygame.jpg", "Banana.jpeg", "Grapes.jpeg", "Watermelon.jpeg", "rat-pygame.jpg"] # lista de comidas possíveis de aparecer na tela (no formato de imagem)
petisco = rand_petisco(lista_comidas) # variável para receber o primeiro alimento a ser projetado na tela para a cobra colidir cada vez que o programa rodar
cor_selecionada = escolher_cor(pergunta_cor_da_cobra) # variável para receber a cor selecionada para a cobra no início de cada sessão
plano_fundo = pygame.image.load(escolher_cenario(lista_cenarios, pergunta_cenario_de_jogo)).convert() # variável contendo a paisagem escolhida para preencher tela do jogo
plano_fundo = pygame.transform.scale(plano_fundo, (largura, altura)) # alterando as dimensões do arquivo de imagem para preencher a tela inteira da partida
plano_endgame = pygame.image.load('Cobra over.jpg').convert() # variável contendo a paisagem escolhida para preencher a tela de fim de jogo (quando o usuário perder uma partida)
plano_endgame = pygame.transform.scale(plano_endgame, (largura, altura)) # alterando as dimensões do arquivo de imagem para preencher a tela inteira do fim da partida

# Métodos base para a execução da partida

def aumenta_cobra(lista_cobra, cor): # Função para preservar o corpo da cobra a cada colisão (ponto obtido), efetuando a atualização da posição de cada retângulo adicional ou pré-existente pela redefinição das respectivas coordenadas
    for ParXY in lista_cobra: # looping varrendo cada parcela constituinte do corpo da cobra, inseridos dentro da lista_cobra, conforme as cores próprias e os respectivos pares ordenados "ParXY" intrínsecos dos elementos projetados na tela do jogo

        pygame.draw.rect(tela, cor, (ParXY[0], ParXY[1], 20, 20)) # renderizando o novo corpo da cobra (aumentado pelo alimento consumido = ponto obtido)

def reiniciar_jogo(): # Função para reiniciar o jogo após o fim de cada partida, reconfigurando as variáveis globais e preservando os valores de entrada do início da sessão do game
    global pontuacao, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_corpo, x_food, y_food, perdeu, pergunta_modo_de_jogo # variáveis globais de interesse
    pontuacao = 0 # zerando a pontuação da partida passada
    comprimento_inicial = escolher_modo(pergunta_modo_de_jogo)[1] # preservando o comprimento inicial selecionado pelo modo de dificuldade escolhido
    x_cobra = int(largura / 2) # definindo a abscissa inicial da cobra para a próxima partida, caso tenha
    y_cobra = int(altura / 2) # definindo a ordenada inicial da cobra para a próxima partida, caso tenha
    lista_cobra = [] # "limpando" a lista_cobra para a próxima partida, caso tenha
    lista_corpo = [] # "limpando" a lista_cabeca para a próxima partida, caso tenha
    x_food = randint(40, 600) # sorteando a nova abscissa para o primeiro alimento da próxima partida, caso tenha
    y_food = randint(60, 430) # sorteando a nova ordenada para o primeiro alimento da próxima partida, caso tenha
    perdeu = False # "desativando" a condição de derrota (variável de fim do jogo), para possibilitar que uma nova partida possa começar

# Laço principal do jogo

while True:

    relogio.tick(30) # definição do timer do referencial de tempo/espaço do jogo

    tela.blit(plano_fundo, (0, 0)) # implantação do cenário selecionado para cada partida

    mensagem = f'Pontos: {pontuacao} & Recorde: {recorde}' # variável para receber o texto do "scoreboard" (placar)
    texto_formatado = fonte1.render(mensagem, True, (0, 0, 0)) # renderização do placar na tela do game com a fonte pré-selecionada e a cor preta

    for event in pygame.event.get(): # looping de eventos durante a partida

        if event.type == QUIT: # configuração que possibilita o usuário sair do jogo quando quiser
            pygame.quit()
            exit()

        if event.type == KEYDOWN: # quando as teclas do teclado forem pressionadas
            if event.key == K_LEFT: # para ir a esquerda tecle left (seta para a esquerda)
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT: # para ir a direita tecle right (seta para a direita)
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP: # para ir para cima tecle up (seta para cima)
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN: # para ir para baixo tecle down (seta para baixo)
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle # possibilitando a movimentação da cobra no eixo horizontal, incrementando sua abscissa conforme a mobilidade instantânea associada
    y_cobra += y_controle # possibilitando a movimentação da cobra no eixo vertical, incrementando sua ordenada conforme a mobilidade instantânea associada

    cobra_cabeca1 = pygame.draw.rect(tela, cor_selecionada, (x_cobra, y_cobra, 20, 20)) # parte retangular (quadrado de lado 20 unidades) da cabeça da cobra, colorido com a cor pré-selecionada
    cobra_cabeca2 = pygame.draw.circle(tela, cor_selecionada, (x_cobra + 5, y_cobra + 10), 20) # parte circular (círculo de raio 20 unidades) da cabeça da cobra, colorido com a cor pré-selecionada
    olho = pygame.draw.circle(tela, (0, 0, 0), (x_cobra, y_cobra), 5) # olho da cobra = círculo preto de raio igual a 5 unidades
    food = pygame.draw.rect(tela, (0, 0, 0), (x_food, y_food, petisco[1][0], petisco[1][1])) # variável do tipo "draw" (desenho) para receber a projeção da imagem de alimento sorteado
    alimento = pygame.image.load(petisco[0]).convert() # variável do tipo "image" (imagem) para carregar a imagem da comida sorteada
    alimento = pygame.transform.scale(alimento, petisco[1]) # redimensionando a imagem sorteada para ser projetada adequadamente sobre a variável de desenho "food"
    tela.blit(alimento, (x_food, y_food)) # projetando a imagem sorteada através do recebimento das mesmas coordenadas aleatórias de "food"

    if cobra_cabeca1.colliderect(food): # função para estabelecer as colisões entre a cobra e o alimento projetado em cima de "food", ilustrando o ato da cobra devorando a iguaria sorteada
        x_food = randint(40, 600) # redefinindo uma nova abscissa aleatória para a comida (food)
        y_food = randint(60, 430) # redefinindo uma nova ordenada aleatória para a comida (food)
        pontuacao += 1 # incrementando os pontos obtidos pelo jogador
        petisco = rand_petisco(lista_comidas) # efetuando o sorteio de uma nova imagem (comida)
        if pontuacao > recorde: # condicional para estabelecer o recorde de pontos obtidos pelo usuário em uma partida
            recorde = pontuacao

        som_mordida.play() # ativando o som da mordida quando a cobra encostar na comida (food)
        comprimento_inicial += 1 # incrementando o tamanho do corpo da cobra com um quadrado a mais (um alimento consumido)

    lista_corpo = [] # definindo a variável de recebimento do par ordenado de cada novo quadrado do corpo da cobra
    lista_corpo.append(x_cobra) # adicionando a abscissa do novo quadrado "rect" a lista_corpo
    lista_corpo.append(y_cobra) # adicionando a ordenada do novo quadrado "rect" a lista_corpo

    lista_cobra.append(lista_corpo) # adicionando cada par ordenado dos elementos "draw" (quadrados) a lista principal (lista_cobra), para utilizar na função de incrementação da cobra com a cor definida (aumenta_cobra())

    if lista_cobra.count(lista_corpo) > 1: # definindo a condição de derrota do usuário durante a partida (a cobra encostando nela mesma)
        fonte2 = pygame.font.SysFont('arial', 20, True, True) # nova fonte selecionada para a tela de 'game over'
        mensagem = 'Tente de novo, amigão! Pressione ESPAÇO para jogar novamente,' # novo texto para a variável "mensagem" receber
        mensagem_sair = 'ou pressione TAB para sair.' # texto adicional para a frase da tela de fim de jogo
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0)) # renderização da parte de cima do texto de derrota
        centro_texto = texto_formatado.get_rect() # variável de centralização da mensagem de derrota
        som_fim_de_jogo.play() # ativação do som de derrota
        texto_sair_jogo = fonte2.render(mensagem_sair, True, (0, 0, 0)) # renderização do restante do texto de derrota

        perdeu = True # condição de derrota efetuada

        while perdeu: # looping de derrota (somente enquanto estiver na tela de fim de jogo)

            tela.blit(plano_endgame, (0, 0)) # projeção da imagem de fundo para a tela de game over

            for event in pygame.event.get(): # laço dos eventos possíveis na tela de derrota
                if event.type == QUIT: # possibilidade de sair pelo comando exit(), na tela do jogo
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN: # eventos quando as teclas do teclado forem pressionadas
                    if event.key == K_SPACE: # quando espaço for pressionado, uma nova partida começa
                        reiniciar_jogo() # jogo reiniciado
                    if event.key == K_TAB: # quando a tecla tab for pressionada o jogador sai do jogo e o programa se encerra
                        pygame.quit()
                        exit()

# Formatação final do texto de derrota e atualização da tela do jogo

            centro_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, centro_texto)
            tela.blit(texto_sair_jogo, ((largura // 2) - 315, (altura // 2) + 10))

            pygame.display.update() # atualização da tela durante a tela de game over

# Condições de contorno ao colidir com as bordas

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial: # reinicializando o tamanho da lista principal para uma nova partida
        del lista_cobra[0]

    aumenta_cobra(lista_cobra, cor_selecionada) # incremento do corpo da cobra

    tela.blit(texto_formatado, (150, 0)) # alocação do placar na tela da partida

    pygame.display.update() # atualização da tela durante a tela da partida

# Obrigado por jogar conosco! Volte sempre
