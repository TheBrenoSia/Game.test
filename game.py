import random
import time

print("=" * 40)
print("🔥 BATALHA DEV CONTRA O BUG 🔥")
print("=" * 40)

vida_jogador = 100
vida_bug = 120

ataques = {
    "1": ("Código Limpo", 18),
    "2": ("Stack Overflow", 25),
    "3": ("Deploy em Produção", 40)
}

while vida_jogador > 0 and vida_bug > 0:

    print(f"\n🧑‍💻 Sua vida: {vida_jogador}")
    print(f"🐛 Vida do Bug: {vida_bug}")

    print("\nEscolha seu ataque:")
    print("1 - Código Limpo")
    print("2 - Stack Overflow")
    print("3 - Deploy em Produção")

    escolha = input(">> ")

    if escolha not in ataques:
        print("Você apertou algo inválido.")
        continue

    nome_ataque, dano = ataques[escolha]

    dano_real = random.randint(dano - 5, dano + 5)

    print(f"\n⚔️ Você usou: {nome_ataque}")
    time.sleep(1)

    vida_bug -= dano_real

    if vida_bug <= 0:
        vida_bug = 0
        print(f"💥 Você causou {dano_real} de dano!")
        print("\n🏆 O BUG FOI ELIMINADO!")
        break

    print(f"💥 Você causou {dano_real} de dano!")

    ataque_bug = random.randint(8, 20)

    print("\n🐛 O bug está atacando...")
    time.sleep(1)

    vida_jogador -= ataque_bug

    if vida_jogador < 0:
        vida_jogador = 0

    print(f"☠️ O bug causou {ataque_bug} de dano!")

if vida_jogador <= 0:
    print("\n💀 Você morreu.")
    print("O bug foi para produção.")
