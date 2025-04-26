import random

def jogar_forca():
    # 1. Lista de palavras secretas:
    lista_de_palavras = [
        "PYTHON", "CODE", "PROGRAMAR", "GAME", "COMPUTADOR", "ALGORITMO",
        "VARIAVEL", "FUNCAO", "LOOP", "INTERFACE", "API", "FRAMEWORK",
        "DEBUGGING", "COMPILER", "CLASSE", "LINGUAGEM", "JAVA",
        "BANCO DE DADOS", "GIT", "JSON", "HTTP", "FRAMEWORK WEB"
    ]
    # Criamos uma lista contendo várias palavras que o jogo pode escolher aleatoriamente.
    # Todas as palavras estão em MAIÚSCULO para facilitar a comparação com a entrada do jogador.

    # 2. Escolha da palavra secreta:
    palavra_secreta = random.choice(lista_de_palavras)
    # A função random.choice() escolhe aleatoriamente um elemento (neste caso, uma palavra) da lista lista_de_palavras e a armazena na variável palavra_secreta. Esta é a palavra que o jogador tentará adivinhar.

    # 3. Inicialização da palavra amostra:
    palavra_amostra = ["_"] * len(palavra_secreta)
    # Criamos uma lista chamada palavra_amostra. Ela terá o mesmo número de elementos que a palavra secreta.
    # Cada elemento inicial é um underscore ("_"), representando uma letra não adivinhada da palavra secreta.
    # Usamos uma lista porque strings em Python são imutáveis, e precisaremos atualizar as letras adivinhadas.

    # 4. Conjunto de letras tentadas:
    letras_tentadas = set()
    # Criamos um conjunto (set) chamado letras_tentadas. Conjuntos são úteis para armazenar coleções de itens únicos.
    # Usaremos este conjunto para guardar todas as letras que o jogador já tentou, evitando que ele tente a mesma letra várias vezes.

    # 5. Número de vidas:
    vidas = 6
    # Definimos um número inicial de tentativas (vidas) que o jogador tem para adivinhar a palavra.

    # 6. Mensagens de boas-vindas e estado inicial:
    print("BEM-VINDO AO JOGO DA FORCA!")
    print(f"A PALAVRA TEM {len(palavra_secreta)} LETRAS.")
    print(f"VOCÊ TEM {vidas} TENTATIVAS.")
    print("PALAVRA: ", " ".join(palavra_amostra))
    # Imprimimos mensagens de boas-vindas, informando o comprimento da palavra secreta e o número de vidas do jogador.
    # " ".join(palavra_amostra) junta os elementos da lista palavra_amostra em uma string, separando-os por espaços para melhor visualização (ex: _ _ _ _ _).

    # 7. Loop principal do jogo:
    while vidas > 0 and "_" in palavra_amostra:
        # Este loop continua enquanto o jogador tiver vidas restantes (vidas > 0) E ainda houver underscores na palavra amostra (ou seja, letras não adivinhadas).

        # 8. Entrada da tentativa do usuário:
        tentativa_usuario = input("DIGITE UMA LETRA: ").upper()
        # Pedimos ao jogador para digitar uma letra usando a função input().
        # Convertemos a entrada para MAIÚSCULO usando .upper() para garantir a consistência com a palavra secreta.

        # 9. Validação da entrada:
        if len(tentativa_usuario) == 1 and tentativa_usuario.isalpha():
            # Verificamos se o jogador digitou apenas um caractere (len(tentativa_usuario) == 1) e se esse caractere é uma letra do alfabeto (tentativa_usuario.isalpha()).

            # 10. Verificação se a letra já foi tentada:
            if tentativa_usuario in letras_tentadas:
                print("VOCÊ JÁ TENTOU ESSA LETRA. TENTE OUTRA.")
            # Se a letra digitada já estiver no conjunto letras_tentadas, informamos ao jogador.

            # 11. Verificação se a letra está na palavra secreta:
            elif tentativa_usuario in palavra_secreta:
                print("LETRA CORRETA!")
                # Se a letra estiver na palavra secreta, informamos ao jogador.
                for i, letra in enumerate(palavra_secreta):
                    if letra == tentativa_usuario:
                        palavra_amostra[i] = letra
                # Percorremos cada letra da palavra secreta com seu índice (enumerate()).
                # Se a letra secreta na posição atual (letra) for igual à tentativa do usuário,
                # atualizamos a palavra_amostra na mesma posição (i) com a letra correta.
                letras_tentadas.add(tentativa_usuario)
                # Adicionamos a letra correta ao conjunto de letras_tentadas.

            # 12. Se a letra não está na palavra secreta:
            else:
                vidas -= 1
                print(f"LETRA INCORRETA! VOCÊ PERDEU UMA VIDA. RESTAM {vidas} VIDAS.")
                letras_tentadas.add(tentativa_usuario)
                # Se a letra não estiver na palavra secreta, decrementamos o número de vidas do jogador.
                # Informamos ao jogador que a letra está incorreta e quantas vidas restam.
                # Adicionamos a letra incorreta ao conjunto de letras_tentadas.

            # 13. Exibição do estado atual do jogo:
            print("PALAVRA: ", " ".join(palavra_amostra))
            print("LETRAS TENTADAS:", ", ".join(sorted(list(letras_tentadas))))
            # Mostramos a palavra amostra atualizada e as letras que o jogador já tentou (em ordem alfabética para melhor visualização).

        # 14. Se a entrada do usuário não for válida:
        else:
            print("POR FAVOR, DIGITE APENAS UMA LETRA.")
            # Se o jogador não digitar uma única letra, mostramos uma mensagem de erro.

    # 15. Fim do jogo - verificação de vitória ou derrota:
    if "_" not in palavra_amostra:
        print("PARABÉNS! VOCÊ ADIVINHOU A PALAVRA:", palavra_secreta)
    else:
        print("VOCÊ PERDEU! A PALAVRA SECRETA ERA:", palavra_secreta)
    # Após o loop principal terminar (porque as vidas acabaram ou não há mais underscores),
    # verificamos se ainda há underscores na palavra amostra.
    # Se não houver, o jogador venceu. Caso contrário, ele perdeu e revelamos a palavra secreta.

# 16. Loop para jogar novamente:
while True:
    jogar_forca()
    jogar_novamente = input("DESEJA JOGAR NOVAMENTE? (S/N): ").upper()
    if jogar_novamente != 'S':
        break
# Este loop permite que o jogador jogue múltiplas rodadas.
# Após cada rodada (chamada da função jogar_forca()), perguntamos se o jogador quer jogar novamente.
# Se a resposta (convertida para maiúsculo) não for 'S', o loop é interrompido e o programa termina.

# 17. Mensagem de agradecimento:
print("OBRIGADO POR JOGAR!")
# Mensagem final exibida quando o jogador decide parar de jogar.