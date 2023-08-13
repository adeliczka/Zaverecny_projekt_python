from pojisteny import Pojisteny


class AkcePojistenych:
    """
    Třída reprezentující jednotlivé akce/úkony,
    které budou vykonané s evidencí pojištěných.
    """

    def __init__(self):
        self.seznam_pojistencu = []    # Seznam pojištěnců

    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        """
        Přidá zadaného pojištěného od uživatele (inputem)
        do kolekce (seznamu pojištěnců).
        :param jmeno: Jméno pojištěného
        :param prijmeni: Příjmení pojištěného
        :param vek: Věk pojištěného
        :param telefon: Telefon pojištěného
        """
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam_pojistencu.append(pojisteny)

    def vypis_pojistene(self):
        """
        Vypíše pojištěného nebo seznam všech
        dříve zadaných pojištěných.
        """
        if self.seznam_pojistencu:
            print("Seznam pojištěných v evidenci: ")
            for pojisteny in self.seznam_pojistencu:
                print(pojisteny)
            print()
        else:
            print("V evidenci pojištěných není vložený ani jeden záznam.")
            print("Nejdříve je nutné přidat nového pojištěného.\n")

    def vyhledej_pojistene(self, jmeno, prijmeni):
        """
        Vyhledá pojištěného nebo seznam všech
        dříve zadaných pojištěných.
        :param jmeno: Jméno pojištěného
        :param prijmeni: Příjmení pojištěného
        :return: Vyhledaný pojištěný
        """
        for pojisteny in self.seznam_pojistencu:
            if pojisteny._jmeno == jmeno and pojisteny._prijmeni == prijmeni:
                return pojisteny