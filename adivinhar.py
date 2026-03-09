# Jogo da Adivinhação

import random

def gerar_numero():
    """Gera um número aleatório entre 1 a 30"""
    return random.randint(1, 30)


def verificar_palpite(palpite, numero_secreto):
    """Verifica se o palpite está certo"""
    if palpite < numero_secreto:
        return "O número que estou pensando é acima deste palpite"
    if palpite > numero_secreto:
        return "O número que estou pensando é abaixo deste palpite"
    else: 
        return "Parabéns! Você acertou o número em que eu estava pensando"
    

def jogar():
    """A função principal do jogo"""
    print("=" * 40)
    print("  -  -  -  Jogo da Adivinhação  -  -  -  ")
    print("=" * 40)
    print("Estou pensando em um número entre 1 e 30")
    print("Tente adivinhar qual é!")
    print("=" * 40)

    numero_secreto = gerar_numero()
    tentativas = 0 
    max_tentativas = 5

    while tentativas < max_tentativas:
        try:
            palpite = int(input(f"\nTentativa {tentativas + 1}/{max_tentativas}: Digite seu palpite: "))

            if palpite < 1 or palpite > 30:
                print("O número que eu pensei está entre 1 a 30 apenas.")
                continue
            
            resultado = verificar_palpite(palpite, numero_secreto)
            tentativas += 1

            if resultado == "Parabéns! Você acertou o número em que eu estava pensando":
                print(f"\n🎉 Parabéns! Você acertou em {tentativas} Tentativas!")
                print(f"O número secreto era: {numero_secreto}")
                break
            else:
                print(f"📌 Dica: {resultado}")
                
        except ValueError:
            print("Ops! Por favor, digite um número válido")

    if tentativas == max_tentativas:
        print(f"\n😢 Essa não! Fim de jogo! O número em que eu estava pensando era: {numero_secreto}")

# Iniciar Jogo
if __name__ == "__main__":
    jogar()