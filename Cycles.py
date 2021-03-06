import pygame
import time

#criar listas
nomeimg = ['backgroundportafechada', 'ffrente', 'ftras', 'fesquerda', 'fdireita', 'perguntacama', 'dormindo', 'perguntalivro', 'livro', 'perguntaporta', 'portaaberta', 'espaço'] 
locimg = [r"imagens\pixil-frame-4.png", r"imagens\pixil-frame-ff.png", r"imagens\pixil-frame-ft.png", r"imagens\pixil-frame-fe.png", r"imagens\pixil-frame-fd.png", r"imagens\pixil-frame-ws.png",r"imagens\pixil-frame-5.png", r"imagens\pixil-frame-rd.png", r"imagens\pixil-frame-j.png", r"imagens\pixil-frame-od.png", r"imagens\pixil-frame-3.png", r"imagens\pixil-frame-e.png"]

#criando as imagens
for c in range(len(nomeimg)):
    globals()[nomeimg[c]] = pygame.image.load(locimg[c])

#ajustando o tamanho das imagens
ffrente = pygame.transform.scale(ffrente, (60, 80))
ftras = pygame.transform.scale(ftras, (60, 80))
fesquerda = pygame.transform.scale(fesquerda, (60, 80)) 
fdireita = pygame.transform.scale(fdireita, (60, 80))
perguntacama = pygame.transform.scale(perguntacama, (450, 130))
perguntalivro = pygame.transform.scale(perguntalivro, (450, 130))
livro = pygame.transform.scale(livro, (450, 380))
espaço = pygame.transform.scale(espaço, (600,600))

# configurando a tela
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cycles")

# criando o relógio
clock = pygame.time.Clock()

#iniciando
run = True
pygame.init()
estadotela = "portafechada"
estadof = "frente"
cordx = 280
cordy = 300

#colocando a música
pygame.mixer.init()
pygame.mixer.music.load("cyclesost.mp3")
pygame.mixer.music.play()

while run:

    #porta fechada
    if estadotela == "portafechada":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        #captação cama
        if cordx == 100:
            if cordy >=100 and cordy <= 220:
                estadotela = "perguntacama"
        #captação livro
        if cordx >= 420 and cordx <= 540:
            if cordy >= 120 and cordy <= 200:
                estadotela = "perguntalivro"
        #captação porta
        if cordx >= 260 and cordx <= 280:
            if cordy == 60:
                estadotela = "perguntaporta"
        #eventos de movimentação
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_w:
                    estadof = "tras"
                    if cordy < 250 and cordy > 70:
                        if cordx > 99:
                            cordy -= 20
                    if cordy >= 250:
                        cordy -= 20       
                if evento.key == pygame.K_a:
                    estadof = "esquerda"
                    if cordx < 110:
                        if cordy > 239:
                            cordx -= 20
                    if cordx >= 110:
                        cordx -= 20
                if evento.key == pygame.K_s:
                    estadof = "frente"
                    cordy += 20
                if evento.key == pygame.K_d:
                    estadof = "direita"
                    cordx += 20

    #pergunta se quer dormir
    if estadotela == "perguntacama":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        tela.blit(perguntacama, (20,450))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_n:
                    cordx = 120
                    estadotela = "portafechada"
                if evento.key == pygame.K_y:
                    estadotela = "dormindo"

    #pergunta se quer ler o diário
    if estadotela == "perguntalivro":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        tela.blit(perguntalivro, (20,450))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_n:
                    if cordx > 420 and cordx < 540:
                        if cordy >= 200:
                            cordy += 20
                        else:
                            cordy -= 20
                    elif cordx <= 420:
                        cordx -= 20
                    elif cordx >= 540:
                        cordx += 20

                    estadotela = "portafechada"
                if evento.key == pygame.K_y:
                    estadotela = "lendolivro"

    #fantasma frames
    if estadof == "frente":
        tela.blit(ffrente,((cordx,cordy)))
    if estadof == "tras":
        tela.blit(ftras,((cordx,cordy)))
    if estadof == "esquerda":
        tela.blit(fesquerda,((cordx,cordy)))
    if estadof == "direita":
        tela.blit(fdireita,((cordx,cordy)))

    #diário na tela
    if estadotela == "lendolivro":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        tela.blit(livro, (80,150))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_x:
                    if cordx > 420 and cordx < 540:
                        if cordy >= 200:
                            cordy += 20
                        else:
                            cordy -= 20
                    elif cordx <= 420:
                        cordx -= 20
                    elif cordx >= 540:
                        cordx += 20
                    estadotela = "portafechada"

    #tela dormindo
    if estadotela == "dormindo":
        tela.fill((200,200,200))
        tela.blit(dormindo,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d or evento.key == pygame.K_s:
                    cordx += 20
                    estadotela = "portafechada"

    #pergunta se quer abrir a porta
    if estadotela == "perguntaporta":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        tela.blit(perguntaporta, (20,450))
        #fantasma frames
        if estadof == "frente":
            tela.blit(ffrente,((cordx,cordy)))
        if estadof == "tras":
            tela.blit(ftras,((cordx,cordy)))
        if estadof == "esquerda":
            tela.blit(fesquerda,((cordx,cordy)))
        if estadof == "direita":
            tela.blit(fdireita,((cordx,cordy)))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_n:
                    cordy += 20
                    estadotela = "portafechada"
                if evento.key == pygame.K_y:
                    estadotela = "portaaberta"
    
    #tela com porta aberta
    if estadotela == "portaaberta":
        tela.fill((200,200,200))
        tela.blit(portaaberta,(0,0))
        #entra no espaço
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    if cordx >= 260 and cordx <=280 and cordy == 60:
                        estadotela = "espaço"
        #eventos de movimentação
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key== pygame.K_w:
                    estadof = "tras"
                    if cordy < 250 and cordy > 70:
                        if cordx > 99:
                            cordy -= 20
                    if cordy >= 250:
                        cordy -= 20       
                if evento.key == pygame.K_a:
                    estadof = "esquerda"
                    if cordx < 110:
                        if cordy > 239:
                            cordx -= 20
                    if cordx >= 110:
                        cordx -= 20
                if evento.key == pygame.K_s:
                    estadof = "frente"
                    cordy += 20
                if evento.key == pygame.K_d:
                    estadof = "direita"
                    cordx += 20
        #fantasma frames
        if estadof == "frente":
            tela.blit(ffrente,((cordx,cordy)))
        if estadof == "tras":
            tela.blit(ftras,((cordx,cordy)))
        if estadof == "esquerda":
            tela.blit(fesquerda,((cordx,cordy)))
        if estadof == "direita":
            tela.blit(fdireita,((cordx,cordy)))

    #tela do espaço
    if estadotela == "espaço":
        tela.fill((200,200,200))
        tela.blit(espaço,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                pygame.mixer.music.rewind()
                cordx = 280
                cordy = 300
                estadotela = "portafechada"

    #FPS
    clock.tick(50)

    #update
    pygame.display.update()

pygame.mixer.quit
pygame.font.init()
pygame.quit()
