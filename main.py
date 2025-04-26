import random

def jogar_forca():
    lista_de_palavras = [
        "PYTHON", "CODE", "PROGRAMAR", "GAME", "COMPUTADOR", "ALGORITMO",
        "VARIAVEL", "FUNCAO", "LOOP", "INTERFACE", "API", "FRAMEWORK",
        "DEBUGGING", "COMPILER", "CLASSE", "LINGUAGEM", "JAVA",
        "BANCO DE DADOS", "GIT", "JSON", "HTTP", "FRAMEWORK WEB"
    ]
    palavra_secreta = random.choice(lista_de_palavras)
    palavra_amostra = ["_"] * len(palavra_secreta)
    letras_tentadas = set()
    vidas = 6

    print("BEM-VINDO AO JOGO DA FORCA!")
    print(f"A PALAVRA TEM {len(palavra_secreta)} LETRAS.")
    print(f"VOCÊ TEM {vidas} TENTATIVAS.")
    print("PALAVRA: ", " ".join(palavra_amostra))

    while vidas > 0 and "_" in palavra_amostra:
        tentativa_usuario = input("DIGITE UMA LETRA: ").upper()

        if len(tentativa_usuario) == 1 and tentativa_usuario.isalpha():
            if tentativa_usuario in letras_tentadas:
                print("VOCÊ JÁ TENTOU ESSA LETRA. TENTE OUTRA.")
            elif tentativa_usuario in palavra_secreta:
                print("LETRA CORRETA!")
                for i, letra in enumerate(palavra_secreta):
                    if letra == tentativa_usuario:
                        palavra_amostra[i] = letra
                letras_tentadas.add(tentativa_usuario)
            else:
                vidas -= 1
                print(f"LETRA INCORRETA! VOCÊ PERDEU UMA VIDA. RESTAM {vidas} VIDAS.")
                letras_tentadas.add(tentativa_usuario)
            print("PALAVRA: ", " ".join(palavra_amostra))
            print("LETRAS TENTADAS:", ", ".join(sorted(list(letras_tentadas))))
        else:
            print("POR FAVOR, DIGITE APENAS UMA LETRA.")

    if "_" not in palavra_amostra:
        print("PARABÉNS! VOCÊ ADIVINHOU A PALAVRA:", palavra_secreta)
    else:
        print("VOCÊ PERDEU! A PALAVRA SECRETA ERA:", palavra_secreta)

while True:
    jogar_forca()
    jogar_novamente = input("DESEJA JOGAR NOVAMENTE? (S/N): ").upper()
    if jogar_novamente != 'S':
        break

print("OBRIGADO POR JOGAR!")