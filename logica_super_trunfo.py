pergunta = "Se a carta A tem maior força que a carta B, e a carta B maior que a carta C, quem tem maior força?"
resposta_correta = "A"

print(pergunta)
resposta = input("Digite sua resposta: ")

if resposta.upper() == resposta_correta:
    print("Correto!")
else:
    print(f"Errado! A resposta correta é: {resposta_correta}")