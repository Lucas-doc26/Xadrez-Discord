import pygame

def desenha_tabuleiro(screen, board, imagens_pecas):
    """
    Desenha o tabuleiro de xadrez e as peças na tela usando pygame,
    incluindo as coordenadas (A-H, 1-8).
    """
    cores = [pygame.Color("white"), pygame.Color("gray")]
    tamanho_tabuleiro = 80
    fonte = pygame.font.SysFont("arial", 24)  # Fonte para as coordenadas

    # Desenha o tabuleiro
    for linha in range(8):
        for col in range(8):
            cor = cores[(linha + col) % 2]
            pygame.draw.rect(screen, cor, pygame.Rect(col * tamanho_tabuleiro, linha * tamanho_tabuleiro, tamanho_tabuleiro, tamanho_tabuleiro))
    
    for i in range(8):
        text = fonte.render(chr(65 + i), True, pygame.Color("black"))  # A-H
        screen.blit(text, (i * tamanho_tabuleiro + tamanho_tabuleiro // 4, 0))  

        text = fonte.render(str(8 - i), True, pygame.Color("black"))  # 8-1
        screen.blit(text, (5, i * tamanho_tabuleiro + tamanho_tabuleiro // 4)) 

    # Desenha as peças
    for quadrado, peca in board.piece_map().items():
        imagem_peca = imagens_pecas[str(peca)]
        linha, col = divmod(quadrado, 8)
        screen.blit(imagem_peca, (col * tamanho_tabuleiro, (7 - linha) * tamanho_tabuleiro))


def load_imagens_pecas():
    """
    Carrega imagens das peças para pygame.
    """
    nome_pecas = ["p", "n", "b", "r", "q", "k", "P", "N", "B", "R", "Q", "K"]
    imagens_pecas = {}
    for nome in nome_pecas:
        if nome.isupper():
            peca = nome + '1'
        else: 
            peca = nome
        imagens_pecas[nome] = pygame.image.load(f"assets/{peca}.png")
    return imagens_pecas

def return_img(tabuleiro):
    pygame.init()
    image_size = 640 
    
    superfice = pygame.Surface((image_size, image_size))
    
    imagens_pecas = load_imagens_pecas()
    
    desenha_tabuleiro(superfice, tabuleiro, imagens_pecas)
    
    pygame.image.save(superfice, "tabuleiro_de_xadrez.png")
    pygame.quit()

