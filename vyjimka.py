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
        """
        chybne = True
        while chybne:
            try:
                zadani = int(input(vstup_uzivatele))
                chybne = False
            except ValueError:
                print(chybova_hlaska)
            else:
                return zadani