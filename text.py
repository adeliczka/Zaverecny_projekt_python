from akce import AkcePojistenych
from vyjimka import OsetreniVyjimek

# Vytvoření instance náležící třídě AkcePojistenych
akce_pojistenych = AkcePojistenych()

# Vytvoření instance náležící třídě OsetreniVyjimek
osetreni_vyjimek = OsetreniVyjimek()


class TextKonzoloveAplikace:
    """
    Třída reprezentující texty a komunikaci
    konzolové aplikace s uživatelem.
    """

    def __init__(self):
        pass


    def vypis_text(self):
        """
        Vytiskne název aplikace a veškeré dostupné
        možnosti, které dokáže provést konzolová aplikace.
        """
        while True:
            # Název aplikace
            print("______________________________\nEvidence pojištěných\n______________________________\n")

            # Dostupné možnosti, které může uživatel zvolit
            print("Vyberte si jednu z následujících akcí: ")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Ukončit evidenci pojištěných \n")

            # Vstup od uživatele a uložení výsledku do proměnné volba
            volba = input("Zadejte svou volbu: \n")

            # Následuje blok kódu s podmínkami vztahujícímí se k volbě uživatele
            if volba == "1":
                # Přidání pojištěnce
                jmeno = input("Zadejte jméno pojištěného: ")
                prijmeni = input("Zadejte příjmení pojištěného: ")
                vek = osetreni_vyjimek.zadej_cislo("Zadejte věk pojištěného: ",
                                                   "Neplatné zadání. Je možné zadat pouze číslice (celá čísla), nikoliv písmena nebo desetinná čísla.\n")
                telefon = osetreni_vyjimek.zadej_cislo("Zadejte telefonní číslo pojištěného: ",
                                                       "Neplatné zadání. Je možné zadat pouze číslice (celá čísla), nikoliv písmena nebo desetinná čísla.\n")
                akce_pojistenych.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
                print(f"\nV pořádku, pojištěný {jmeno} {prijmeni} byl úspěšně vložený do evidence.\n")
# Jak provést, aby se při najetí myši na metodu zobrazila dokumentace jako v souboru akce.py??

            elif volba == "2":
                # Vypsání pojištěnce
                akce_pojistenych.vypis_pojistene()

            elif volba == "3":
                # Vyhledání pojištěnce
                jmeno = input("Zadejte jméno pojištěného: ")
                prijmeni = input("Zadejte příjmení pojištěného: ")
                vyhledany_pojisteny = akce_pojistenych.vyhledej_pojistene(jmeno, prijmeni)
                if vyhledany_pojisteny:
                    print("\nKompletní data vyhledaného pojištěného:")
                    print(vyhledany_pojisteny)
                    print()
                else:
                    print("\nPojištěný se zadaným jménem a příjmením nebyl nalezen.")
                    print("Zadali jste správně diakritiku a dodrželi velká a malá písmena?")
                    print("Případně je možné, že evidence pojištěných neobsahuje žádné pojištěné.\n")

            elif volba == "4":
                # Ukončení aplikace
                print("Program 'Evidence pojištěných' byl ukončen.")
                print("Děkujeme za využití služeb evidence.\n")
                break

            else:
                # Zadáno cokoliv kromě číslic 1 až 4
                print("Neplatná volba. Je možné zadat pouze číslice od 1 do 4. Zkuste to znovu.\n")