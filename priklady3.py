import random

# Definujte úlohy bez čísel
ulohy = [
    "Jaký je obvod čtverce se stranou ? cm?",
    "Jaký je obsah trojúhelníka s výškou ? cm a základnou ? cm?",
    # Přidejte další úlohy podle potřeby
]

# Nahraďte otazníky náhodnými čísly
nahodna_cisla = [random.randint(1, 100) for _ in range(len(ulohy))]
ulohy_s_nahodnymi_cisly = [uloha.replace("?", str(cislo)) for uloha, cislo in zip(ulohy, nahodna_cisla)]

# Uložte úlohy s náhodnými čísly do textového souboru
with open("ulohy2.txt", "w", encoding="utf-8") as soubor:
    for uloha in ulohy_s_nahodnymi_cisly:
        soubor.write(f"{uloha}\n")

print("Úlohy s náhodnými čísly byly uloženy do souboru 'ulohy.txt'.")

# Studenti mohou zde zadat odpovědi na úlohy
print("Nyní mohou studenti zodpovědět úlohy v souboru 'ulohy.txt'.")
print("Po dokončení studentů můžete provést kontrolu jejich odpovědí.")

# Po odeslání studentů můžete provést kontrolu odpovědí podle otázek v souboru "ulohy.txt"
with open("ulohy.txt", "r") as soubor:
    ulohy_s_nahodnymi_cisly = [radek.strip() for radek in soubor.readlines()]

# Zde byste měli provést kontrolu odpovědí studentů a zpracovat jejich výsledky
# Můžete použít proměnnou ulohy_s_nahodnymi_cisly, abyste získali otázky a přirozeně měli seznam studentových odpovědí.
