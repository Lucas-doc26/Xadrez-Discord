import discord
from discord.ext import commands
import chess
from img import return_img
from chess.engine import SimpleEngine
import os
from dotenv import load_dotenv

load_dotenv('disc.env')

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
STOCKFISH_PATH = os.getenv("STOCKFISH_PATH")

# Inicializa o engine
engine = SimpleEngine.popen_uci(STOCKFISH_PATH)
tabuleiro_xadrez = chess.Board()

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def start(ctx):
    global tabuleiro_xadrez
    tabuleiro_xadrez = chess.Board() 
    await ctx.send("Jogo de xadrez iniciado! Use `!mover origem destino` para jogar. Exemplo: `!mover e2 e4`.")
    await tabuleiro(ctx)

@bot.command()
async def mover(ctx, origem: str, destino: str):
    global tabuleiro_xadrez
    try:
        movimento = chess.Move.from_uci(origem + destino)
        if movimento in tabuleiro_xadrez.legal_moves:
            tabuleiro_xadrez.push(movimento)
            await ctx.send(f"Movimento realizado: {origem} para {destino}")
            
            # Verifica se o jogo terminou
            if tabuleiro_xadrez.is_checkmate():
                await ctx.send("Xeque-mate! O jogo terminou.")
            elif tabuleiro_xadrez.is_stalemate():
                await ctx.send("Empate! O jogo terminou.")
            else:
                await ctx.send(f"É a vez do bot!")
                # Jogada do bot (simples, escolhe o primeiro movimento possível)
                bot_move = engine.play(tabuleiro_xadrez, chess.engine.Limit(time=0.1)).move
                tabuleiro_xadrez.push(bot_move)
                await ctx.send(f"Bot moveu: {bot_move}")
        else:
            await ctx.send("Movimento inválido. Tente novamente.")
    except Exception as e:
        await ctx.send("Erro ao processar o movimento. Certifique-se de usar o formato correto (exemplo: `e2 e4`).")
    await tabuleiro(ctx)

@bot.command()
async def tabuleiro(ctx):
    return_img(tabuleiro_xadrez) 

    img_path = "tabuleiro_de_xadrez.png"

    try:
        await ctx.send(file=discord.File(img_path))
    except FileNotFoundError:
        await ctx.send("Imagem não encontrada!")
    except Exception as e:
        await ctx.send(f"Ocorreu um erro ao enviar a imagem: {e}")

# Inicia o bot
bot.run(os.getenv("DISCORD_TOKEN"))
