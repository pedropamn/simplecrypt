# START!

def media_n_notas():
    q = int(input('Quantas notas quer registrar? '))
    m = soma_provas = 0
    while m < q:
        nota = float(input(f'Digite a nota da P{m+1}: '))
        soma_provas += nota
        m += 1
    media = soma_provas / q
    return media

def confere_media(media):
    if media > 7:
        print(f'Parabéns, com a média {media:.1f}, você está Aprovado!')
    elif media >= 5 and media <= 6.9:
        print(f'Com a média {media:.1f}, você está de Recuperação!')
    elif media < 5:
        print(f'Com a média {media:.1f}, você está Reprovado!')

def main():
    media = media_n_notas()
    confere_media(media)

main()
