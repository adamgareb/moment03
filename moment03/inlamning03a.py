#Variabeln "bruttolön" har en input vilket man använder för att skriva in sin bruttolön som koden senare räknar ut avdragningen på kommunalskatt och landstingsskatt för den lönen du har angett
bruttolön = input("Ange din månadslön: ")

#Här konverterar jag bruttolön variabeln till en interger med nya variabeln "userlön"
userlön = int(bruttolön)

#Det här är uträkningen för mängden kronor kommunalskatten drar av lönen (21,36% för att vara exakt) med variabeln "kommunalskatt"
kommunalskatt = (21.36 / 100) * userlön

#Och detta är uträkningen för mängden landstingsskatten drar av. Denna drar av 11,48% och har variabeln "landstingsskatt"
landstingsskatt = (11.48 / 100) * userlön

#Detta är uträkningen för pengarna kvar efter skatt efter den har dratt av mängden pengar från båda skatterna. Denna variabeln heter "slutlön"
slutlön = userlön - kommunalskatt - landstingsskatt

print("\nUtskrift \nMånadslön         ", int(userlön), "kr", "\nKommunal skatt    ", int(kommunalskatt), 
"kr", "\nLandstingsskatt   ", int(landstingsskatt), "kr", "\nKvar efter skatt  ", int(slutlön), "kr")