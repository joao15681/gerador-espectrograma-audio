import matplotlib.pyplot as plt  #importa biblioteca de grafico, cria apelido plt para facilitar a chamada de funcoes 
import librosa # importa a biblioteca de processamento de audio e musica, diversas ferramentas de matematica 
import tkinter as tk # importa biblioteca para criar interface e apelida de tk 
from tkinter import filedialog # Da biblioteca tkinter importe a funcao filedialog que abre a janela para selecionar arquivos

root = tk.Tk() # inicia o tk = (tkinter) e chama a Classe oficial de criacao de janela (Tk())
root.withdraw() # root = nome escolhido para guardar a janela principal, . conecta variavel a funcao withdraw, withdraw diz a root sumir com a janela, toda funcao necessita de () para executar 

file_path = filedialog.askopenfilename( # File_path é a variavel que guarda o caminho do arquivo selecionado, MODULO filedialog chama uma ORDEM askopenfilename para que abra a janela de selecao e traga o caminho do arquivo selecionado
    title="Selecione um arquivo de áudio", # Customiza o titulo da janela que abrira
    filetypes=[("Arquivos de áudio", "*.wav *.mp3 *.flac")] # Customiza o tipo de arquivo que podera ser selecionado
)
y, sr = librosa.load(file_path) #abre o arquivo que selecionei FILEPATH, y guarda onda sonora, sr guarda taxa de amostragem(velocida/frequencia). R antes das aspas Windows nao confunde com barra do caminho

espectro = librosa.stft(y) # Aplica transformada de fourier de curta duração na onda sonora Y, fatia o audio esepara todas as frequencias

espectro_db = librosa.amplitude_to_db(abs(espectro)) # Converte numeros crus em decibeis, ajuda a visualizar melhor o espectro

librosa.display.specshow(espectro_db, sr=sr, x_axis='time', y_axis='hz') # Pega dados convertidos (espectro_db) usa a taxa de amostragem (sr) dimensiona o tempo e desenha o grafico na tela, Coloca TEMPO na HORIZONTAL, FREQUENCIA HZ na VERTICAL

plt.show() #abre a janela para visualizar o grafico