import math

def mietEinkommensProzent(anzahlGruppen: int, staffelung: int, einkommenMiete: list[list[int]]) -> list[int]:
    mieten, einkommen, prozente = ([0] * anzahlGruppen for _ in range(3)) # Using tuple unpacking
    for i in range(0, len(einkommenMiete)): # Iterating over the array einkommenMiete
        n = math.floor(einkommenMiete[i][0] / staffelung) # Calculate the einkommensgruppe
        if n > anzahlGruppen - 1:
            n = anzahlGruppen -1 # Set einkommen values to the highest group possible if einkommen 
                                 # is bigger than (anzahlGruppen - 1) * staffelung
        mieten[n] += einkommenMiete[i][1] # Add up mieten of each group
        einkommen[n] += einkommenMiete[i][0] # Add up einkommen of each group
    for i in range(0, anzahlGruppen):
        if einkommen[i] != 0:  # Avoid division by zero
            prozente[i] = round(mieten[i] / einkommen[i] * 100) # Round the percentages to integers
        else:
            prozente[i] = 0 # Set percentage to zero when einkommen = 0
    return(prozente)

def sortProzente(prozente: list[int])->list[list[int]]:
    prozente_sorted = [[i, prozente[i]] for i in range(len(prozente))] # Initiate new array with increasing indices and values of array prozente
    for i in range (0, len(prozente_sorted) - 1):
        for j in range (i, len(prozente_sorted)):
            if(prozente_sorted[i][1] > prozente_sorted[j][1]): # Bubble Sort Start
                for k in range(0,2): # Sort indices and values simultaneously
                    prozente_sorted[j][k], prozente_sorted[i][k] = prozente_sorted[i][k], prozente_sorted[j][k] # This is where the sorting is done
    return(prozente_sorted)



prozente = mietEinkommensProzent(5, 1000, [[4200, 1200], [900, 340], [1800, 600], [3600, 1100], [2700, 800], [5900, 1300]])

print("Nicht sortiert:")
for i in range (len(prozente)):
    print("Einkommensgruppe " + str(i) + " : " + str(prozente[i]))

print("\nSortiert:")
sorted_prozente= sortProzente(prozente)

for i in range (len(sorted_prozente)):
    print("Einkommensgruppe " + str(sorted_prozente[i][0]) + " : " + str(sorted_prozente[i][1]))