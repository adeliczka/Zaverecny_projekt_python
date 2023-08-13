class Pojisteny:
    """
    Třída reprezentující pojištěného.
    Protože zde nebylo nutné řešit
    editaci a odstranění dat,
    zvolila jsem neveřejné atributy.
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefon = telefon

    def __str__(self):
        """
        Vrací textovou reprezentaci pojištěného,
        jednotlivé atributy jsou oddělené mezerami.
        :return: Pojištěný (jméno, příjmení, věk, telefon)
        """
        return str("{0:<8} {1:<8} {2:<8} {3:<8}".format(self._jmeno, self._prijmeni, self._vek, self._telefon))