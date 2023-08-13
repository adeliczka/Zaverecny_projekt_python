class OsetreniVyjimek:
    """
    Třída reprezentující ošetření výjimky.
    """

    def __init__(self):
        pass

    def zadej_cislo(self, vstup_uzivatele, chybova_hlaska):
        """
        Zajistí, aby se program nezastavil s chybou,
        když uživatel zadá string při dotazu na věk
        a/nebo string při dotazu na telefonní číslo.
        :param vstup_uzivatele: Dotaz na uživatele a uložení do proměnné zadani
        :param chybova_hlaska: Text chybové hlášky; vysvětlení, co je špatně
        :return: Zadání od uživatele
        """
        chybne = True
        while chybne:
            try:
                # Kód, který může vyvolat výjimku
                zadani = int(input(vstup_uzivatele))
                chybne = False
            except ValueError:
                # Reakce na výjimku ValueError
                print(chybova_hlaska)
            else:
                # Provede se, pokud v bloku try nevznikla výjimka
                return zadani