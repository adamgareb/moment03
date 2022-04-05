#Samma struktur som a och b men har andra if satser som behövs för att beräkna c uppgiften av moment03

bruttolön = input("Ange din månadslön: ")

userlön = int(bruttolön)

kommunalskatt = (21.36 / 100) * userlön

landstingsskatt = (11.48 / 100) * userlön

slutlön = userlön - kommunalskatt - landstingsskatt

årslön = userlön * 12

statligskatt = (årslön - 468700) / 12 * 0.2

#För den här uppgiften har jag lagt till en elif statement, där om din årslön är mellan 468700kr
#och under 675700kr så printar koden ut den statliga skatten du skulle behöva betala med resten
#av de andra skatterna från föregående uppgifter.
if årslön <= 19247:
    print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "(Årslön:", int(årslön), "kr)" "\nKvar efter skatt  ", int(userlön), "kr" "\nEftersom du tjänar under brytpunkten betalar du ingen skatt")
elif årslön <= 468700 and årslön >= 19247:
    print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "(Årslön:", int(årslön), "kr)" "\nKommunal skatt    ", int(kommunalskatt), 
    "kr", "\nLandstingsskatt   ", int(landstingsskatt), "kr", "\nKvar efter skatt  ", int(slutlön), "kr")
elif årslön > 468700 and årslön <= 675700:
    print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "(Årslön:", int(årslön), "kr)" "\nKommunal skatt    ", int(kommunalskatt), 
    "kr", "\nLandstingsskatt   ", int(landstingsskatt), "kr", "\nStatlig skatt      ", int(statligskatt), "kr" "\nKvar efter skatt  ", int(slutlön), "kr")
#Jag lyckades inte med värnskatten i slutet av uppgiften pga tidsbrist