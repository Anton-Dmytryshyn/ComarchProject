def printStep (StepNumber, ReadList):


    #-----Step 1----- Otwieram plik
    ReadList = open("input.txt", "r")    
    Lista = []
    for x in ReadList:
        Lista.append(x[:-1]) # za pomoca "-1" usuwam znak "\n" (inaczej wyczytuje naprzyklad "25/n" zamiast "25")
    ReadList.close()

    Lista = list(filter(None, Lista)) # usuwam puste znaczenia
    print ("STEP 1 - List: \n ", Lista)


    #-----Step 2----- Usuwam duplikaty
    Lista = list(dict.fromkeys(Lista)) # przetwarzam liste w dictionary i odwrotnie, kazdy unikalny element zostaje
    print ("STEP 2 - List: \n ", Lista)


    #-----Step 3----- Sortowanie malejaco
    Lista = sorted(Lista, key=len) # sortowanie za pomoca "key"
    print ("STEP 3 - List: \n ", Lista)


    #-----Step 4----- Przetwarzam na float
    NewLista =[] 
    for x in Lista:  
        try:
            NewLista.append(float(x))  # przetwarzam elementy w float
        except:
            print(x, "nie jest numerem") # nieprawidlowe numery
    Lista = NewLista
    print ("STEP 4 - List: \n ", Lista)


    #-----Step 5----- Sortowanie po wartosci liczby
    Lista.sort()
    print ("STEP 5 - List: \n ", Lista)


    #-----Step 6----- Parzyste indeksy
    ListaBezParzystych = []
    for x in range(len(Lista)):
        if x % 2 != 0: # zostawiam tylko elementy o parzystych indeksach
            ListaBezParzystych.append(Lista[x])
    Lista = ListaBezParzystych
    print ("STEP 6 - List: \n ", Lista)
        

    #-----Step 7----- Usuwanie (10, 500)
    NewLista = []
    for x in Lista:
        if not 10 < x < 500:
            NewLista.append(x) # jesli element nie nalezy do tego przedzialu - zostaje

    Lista = NewLista
    print ("STEP 7 - List: \n ", Lista)


    #-----Step 8----- Liczby pierwsze
    PrimeNumbers = [] 
    PrimeLista = []
    for x in range(int(Lista[0]),int(Lista[-1]+1)): # znajde wszystkie liczby pierwsze na odcinku pierwszy - ostatni elementy listy
        for y in range (2,x): 
            if x%y==0:
                break
            else:
                PrimeNumbers.append(x)

    for g in Lista:
        if g in PrimeNumbers: # jesli element jest w liscie liczb pierwszych oraz w naszej liscie - zostaje
            PrimeLista.append(g)

    Lista = PrimeLista
    print ("STEP 8 - List: \n ", Lista)

    return 
    
printStep(True, True)