def konsonan(frasa):
    for i in vokal:
        frasa = frasa.replace (i,"")
    print(frasa)
    pass
vokal = ("a","A","i","I","u","U","e","E","o","O")
konsonan("Nurul Fikri")