import tkinter as tk # Importando para usar o criador de interfaces
import requests # importando requests que possibilita a captura da informação na API

janela = tk.Tk() # cria uma janela
janela.title("Painel de Decisão do Investidor") # Titulo da janela
janela.geometry("600x400")# tamanho que a janela vai abrir


descricao = tk.Label( # cria caixa de texto
    text="Clique abaixo para consultar o preço do dólar", # aqui vai o texto da caixa de texto
    font=("Arial",20), # configuraçoes da fonte ; tipo de fonte; tamanho da fonte
    fg="green"   # cor da fonte
)
descricao.pack(pady=90) # posiçao vertical da caixa de texto  



def main():# criando funçao que recebe e exibe preço do dolar
    print("Obtendo cotação atual do dolar... ")# print normal
    cotacao = cotacao_dolar()# variavel cotaçao recebe resultado da funcao cotacao_dolar
    if cotacao:
        print("A cotaçao do dolar hoje é: ", cotacao , "R$")# se der tudo certo mostra a cotação
    else:
        print("Nao foi possivel receber a cotação")  # caso haja algum problema no recebimento da cotacao

botao = tk.Button(# criando um botao
    text = "Preço do Dolar",# texto do botao
    command = main,# comando que o botao desencadeia
    bg = "green", # cor de fundo do botao
    fg = "black"# cor da letra do botao
)
botao.pack()# posicao do botao, esta sem nada so para ele ser permitido        


def cotacao_dolar(): # criando uma função
    url = "https://economia.awesomeapi.com.br/last/USD-BRL" # variavel url recebe o link da APi 

    try: # serve para caso o codigo aq dentro der erro, ele mostrar uma mensagem pra esse erro ao usuario usando o EXCEPT
        resposta = requests.get(url) # variavel resposta recebe o Valor do dolar usando o requests.get
        resposta.raise_for_status()   # verifica se a resposta possui algum erro de recebimento usando o .raise_for_status()
        dados = resposta.json() # armazena na variavel dados a resposta convertida pelo .json() em um dicionario python
        cotacao = dados["USDBRL"]["bid"] # pega o valor de "bid" é um valor que vem dentro do arquivo solicitado na url 
        return float(cotacao) # retorna o valor da funcao usando numero flutuante
    except Exception as qualerro:   # except identifica um erro # Exception é a classe que nos diz qual erro ocorreu # as qual erro armazena esse erro dentro da variavel qual erro
          print("Ocorreu um erro: " , qualerro) # escreve o erro na tela
          return None  # retorno da funcao
    

if __name__ == "__main__": ## tem que usar essa merda aq por algum motivo pra rodar
    main()  




janela.mainloop()