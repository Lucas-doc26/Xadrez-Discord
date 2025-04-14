<p align="center">
  Um bot de Discord que permite jogar partidas de xadrez diretamente no chat com interface visual.
</p>

<div align=center>
    <img alt="Static Badge" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img alt="Static Badge" src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    <img alt="Static Badge" src="https://img.shields.io/badge/PyGame-Powered-blue?style=for-the-badge&logo=python&logoColor=white">
</div>

<p align="center">
  <a href="#Projeto">Projeto</a> •
  <a href="#Funcionalidades">Funcionalidades</a> •
  <a href="#ComoJogar">Como jogar</a> •
  <a href="#Instalação">Instalação</a>

</p>

---

<h2 id="Projeto">📫 Projeto</h2>

Este projeto consiste em um bot de Discord feito em Python que permite um usuário jogar xadrez interativamente via comandos no canal de texto contra uma inteligência artificial. O tabuleiro é atualizado graficamente a cada jogada.
<p aling="center>  <\p>

---


<h2 id="Funcionalidades">🎯 Funcionalidades</h2>

- Movimentos de peças válidos
- Geração de imagem do tabuleiro atualizada após cada jogada
- Regras básicas de xadrez implementadas
- Visual simples com peças estilizadas

---

<h2 id="ComoJogar">♟️ Como Jogar</h2>

- Para começar o jogo: `!start`
- Para movimento de peças: `!mover d2 d4`
  
---

<h2 id="Instalação">📦 Instalação</h2>

1. Clone o repositório:
```sh
git clone https://github.com/Lucas-doc26/Xadrez-Discord.git
cd Xadrez-Discord
pip install -r requirements.txt
```
2. Consiga seu TOKEN no site do <a hrfef='https://discord.com/developers/applications'>Discord</a> e escolha qual versão do <a href='https://stockfishchess.org/download/windows/'>Stockfish</a> você deseja, depois crie o arquivo disc.env:
```sh
#disc.env
DISCORD_TOKEN=seu-token
STOCKFISH_PATH=dir-stockfish

```
