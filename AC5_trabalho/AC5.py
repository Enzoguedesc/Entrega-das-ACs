import random

def main():
    vida_av = 100
    defesa_av = random.randint(1, 5)
    ataque_av = random.randint(10, 20)

    vida_mons = random.randint(60,80)
    ataque_mons = random.randint(20, 30)

    print(f"Aventureiro: Vida = {vida_av} - Att = {ataque_av} - Def = {defesa_av}")
    print(f"Monstro: Vida = {vida_mons} - Att = {ataque_mons}")

    rodada = 1

    while vida_av > 0 and vida_mons > 0:
        print(f"RODADA {rodada}:")

        dano = random.randint(1, ataque_av)
        vida_mons -= dano

        dano = random.randint(1, ataque_mons) - defesa_av
        if dano > 0:
           vida_av -= dano

        print(f" Aventureiro: Vida = {vida_av}, Att = {ataque_av}, Def = {defesa_av}")
        print(f" Monstro: Vida = {vida_mons}, Att = {ataque_mons}")

        if vida_mons <= 0:
            print(f"O Monstro morreu!")
        if vida_av <= 0:
            print(f"Você morreu!")

        rodada += 1

if __name__ == "__main__":
    main()
