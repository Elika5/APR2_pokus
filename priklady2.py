import random
import math

def generuj_ulohy(pocet_uloh):
    ulohy = []
    for i in range(pocet_uloh):
        # Náhodně vybereme typ úlohy (úhel, délka strany)
        typ_ulohy = random.choice(["uhel", "strana"])

        if typ_ulohy == "uhel":
            # Generujeme úlohu týkající se úhlu v trojúhelníku
            uhel = random.randint(1, 89)  # Náhodný úhel mezi 1 a 89 stupni
            a = random.randint(1, 100)   # Náhodná délka strany a
            b = random.randint(1, 100)   # Náhodná délka strany b

            # Vypočítáme chybějící úhel
            c = 180 - uhel - 90
            odpoved = c

            uloha = f"V trojúhelníku ABC, kde je úhel α = {uhel}° a úhel β = 90°, vypočtěte úhel γ."

        else:
            # Generujeme úlohu týkající se délky strany v trojúhelníku
            a = random.randint(1, 100)   # Náhodná délka strany a
            b = random.randint(1, 100)   # Náhodná délka strany b
            uhel = random.randint(1, 89)  # Náhodný úhel mezi 1 a 89 stupni

            # Převod úhlu na radiány
            uhel_radians = math.radians(uhel)

            # Vypočítáme chybějící délku strany c
            c = int((a ** 2 + b ** 2 - 2 * a * b * math.cos(uhel_radians)) ** 0.5)
            odpoved = c

            uloha = f"V trojúhelníku ABC, kde je strana a = {a}, strana b = {b} a úhel γ = {uhel}°, vypočtěte délku strany c."

        ulohy.append((uloha, odpoved))

    return ulohy

# Požádáme uživatele o počet úloh
pocet_uloh = int(input("Zadejte počet úloh: "))

ulohy = generuj_ulohy(pocet_uloh)

# Uložíme úlohy do textového souboru v kódování UTF-8
with open("ulohy.txt", "w", encoding="utf-8") as soubor:
    for i, (uloha, odpoved) in enumerate(ulohy, start=1):
        soubor.write(f"Úloha {i}:\n")
        soubor.write(uloha + "\n")
        soubor.write(f"Odpověď: {odpoved}\n\n")

print(f"Úlohy byly uloženy do souboru 'ulohy.txt' v kódování UTF-8.")
