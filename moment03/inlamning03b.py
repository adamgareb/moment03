#Det här är ungefär samma kod som i a uppgiften med vissa förändringar såsom att lägga till en if statement vilket ändrar slutfunktionen på koden

bruttolön = input("Ange din månadslön: ")

userlön = int(bruttolön)

kommunalskatt = (21.36 / 100) * userlön

landstingsskatt = (11.48 / 100) * userlön

slutlön = userlön - kommunalskatt - landstingsskatt

årslön = userlön * 12

#Här i den här if statementen ser den till ifall den årliga inkomsten ligger på 19247kr eller mindre
#Gör den det så ser koden till att användaren inte behöver betala skatt
#Är årsinkomsten högre än så skriver koden ut det som den skrev ut i a uppgiften, med avdragning med skatterna
if årslön <= 19247:
    print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "(Årslön:", int(årslön), "kr)" "\nKvar efter skatt  ", int(userlön), "kr" "\nEftersom du tjänar under brytpunkten betalar du ingen skatt")
else:
    print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "(Årslön:", int(årslön), "kr)" "\nKommunal skatt    ", int(kommunalskatt), 
    "kr", "\nLandstingsskatt   ", int(landstingsskatt), "kr", "\nKvar efter skatt  ", int(slutlön), "kr")
