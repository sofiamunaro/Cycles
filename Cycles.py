import pygame
import time

#criar listas
nomeimg = ['backgroundportafechada', 'ffrente', 'ftras', 'fesquerda', 'fdireita', 'perguntacama', 'dormindo'] 
locimg = [r"imagens\pixil-frame-4.png", r"imagens\pixil-frame-ff.png", r"imagens\pixil-frame-ft.png", r"imagens\pixil-frame-fe.png", r"imagens\pixil-frame-fd.png", r"imagens\pixil-frame-ws.png",r"imagens\pixil-frame-5.png"]

#criando as imagens
for c in range(len(nomeimg)):
    globals()[nomeimg[c]] = pygame.image.load(locimg[c])

#ajustando o tamanho das imagens
ffrente = pygame.transform.scale(ffrente, (60, 80))
ftras = pygame.transform.scale(ftras, (60, 80))
fesquerda = pygame.transform.scale(fesquerda, (60, 80)) 
fdireita = pygame.transform.scale(fdireita, (60, 80))
perguntacama = pygame.transform.scale(perguntacama, (450, 130)) 

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

#mostrando as coordenadas(temporario)
pygame.font.init()
fonte = pygame.font.SysFont('Arial', 40)

while run:

    #porta fechada
    if estadotela == "portafechada":
        tela.fill((200,200,200))
        tela.blit(backgroundportafechada,(0,0))
        #captação cama
        if cordx == 100:
            if cordy >=100 and cordy <= 220:
                estadotela = "perguntacama"
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

    #fantasma frames
    if estadof == "frente":
        tela.blit(ffrente,((cordx,cordy)))
    if estadof == "tras":
        tela.blit(ftras,((cordx,cordy)))
    if estadof == "esquerda":
        tela.blit(fesquerda,((cordx,cordy)))
    if estadof == "direita":
        tela.blit(fdireita,((cordx,cordy)))

    #tela dormindo
    if estadotela == "dormindo":
        tela.fill((200,200,200))
        tela.blit(dormindo,(0,0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d or evento.key == pygame.K_s:
                    cordx = 120
                    estadotela = "portafechada"
    
    #mostrando temporariamente as coordenadas
    texto = fonte.render(f"{cordx},{cordy}", True, (0,0,0))
    textorect = texto.get_rect()
    textorect.center = ((200), (100))
    tela.blit(texto, textorect)


    #FPS
    clock.tick(50)

    #update
    pygame.display.update()

pygame.font.init()
pygame.quit()
