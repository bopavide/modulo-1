#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("HELLO, WORD!")


# In[2]:


print("HELLO, WORD!", 8*8)


# In[3]:


nome = input("inserisci il tuo nome:")
print("ciao,", nome , "!")


# In[4]:


via=input("inserisci il nome della via")
print("hai inserito",via)


# In[5]:


nome = input("inserisci il tuo nome: ")
for contatore  in range(10):
    print("so che non è il tuo nome ora sto per farti auto-distruggere il tuo windows")


# In[6]:


numero1 = int(input("inserisci il primo numero: "))
numero2 = int(input("inserisci il secondo numero: "))
somma = numero1 + numero2
print("la somma è:", somma)


# In[7]:


sottrazione = numero1 - numero2
print("la sottrazione è:", sottrazione)


# In[8]:


numero1 = int(input("inserisci il primo numero: "))
numero2 = int(input("inserisci il secondo numero: "))
moltiplicazione = numero1 * numero2
print("la moltiplicazione è:", moltiplicazione)


# In[9]:


for numero in range(90):
    print(numero)


# In[10]:


operazione = input("inserisci l'operazione(+, -, *, /):")


numero1 = float(input("inserisci il primo numero: "))
numero2 = float(input("inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1 + numero2
elif operazione == "-":
    risultato = numero1 - numero2
elif operazione == "*":
    risultato = numero1 * numero2
elif operazione == "/":
    risultato = numero1 / numero2
else:
    risultato = "operazione non valida"
print("il risultato è: ", risultato)


# In[11]:


operazione = input("inserisci l'operazione (+, -, *, /):")

numero1 = int(input("inserisci il primo numero: "))
numero2 = int(input("inserisci il secondo numero: "))

if operazione == "+":
    risultato = numero1+numero2
elif operazione == "-":
    risultato = numero1-numero2
elif operazione == "*":
    risultato = numero1*numero2
elif operazione == "/":
    risultato = numero1/numero2
else:
    risultato = "operazione non valida"
    
print("il risultato è:", risultato)


# In[12]:


n = int(input("inserisci un numero intero positivo: "))

for numero in range(1,n+1):
    print(numero)


# In[13]:


n = int(input("inserisci un numero intero positivo: "))
somma = 0 

for numero in range(1 , n+1):
    somma += numero 
print("la somma dei primi", n, "numeri interi è: ", somma)


# In[14]:


n = int(input("inserisci un numero intero positivo:"))
print("quadrati dei primi", n, "numeri:")

for numero in range(1,n+1):
    quadrato = numero **2
    print("il quadrato di", numero, "è", quadrato)


# In[15]:


numero = int(input("inserisci un numero: "))
if numero % 2 == 0:
    print(numero, "è un numero pari.")
else:
    print(numero, "è un numero dispari.")


# In[16]:


n = int(input("inserisci un numero positivo: "))
fattoriale = 1

for numero in range(1 , n+1):
    fattoriale *= numero
print("il fattoriale di", n, "è:", fattoriale)


# In[ ]:


numeri = []
n = int(input("quanti numeri vuoi inserire? "))

for i in range(n):
    numero = float(input("inserisci un numero: "))
    numeri.append(numero)

media = sum(numeri) / len(numeri)

print("la media dei numeri inseriti è: ", media, numeri)


# In[ ]:


import random

mosse = (" carta, forbice, sasso")

computer mossa = random.choise(mosse):
    
print("venvenuto al gioco della morra cinese")
scelta giocatore = input("scegli tra: carta, forbice, sasso:")


# In[ ]:


n = int(input("inserisci un numero intero positivo: "))

somma = 0

for numero in range(2, 2 * n)


# In[ ]:


n=int(input("inserisci un numero intero: "))

fattoriale=1

if n<0:
    print("numero negativo")
elif n==0:
    print("il fattoriale di zero è 1 per definizione")
else:
    for numero in range(1,n+1):
        fattoriale*=numero
print(f"il fattoriale di {n} è {fattoriale}")


# In[ ]:


n=int(input("inserisci un numero intero: "))

fattoriale=1

if n<0:
    print("numero negativo")
elif n==0:
    print("il fattoriale di zero è 1 per definizione")
else:
    for numero in range(1,n+1):
        fattoriale*=numero
        print(f"il fattoriale di {n} è {fattoriale}")
        # se il print va messo nel ciclo for scrivera tutti i passagi fino alla soluzione


# In[ ]:


# chiedere all utente di inderire un numero intero positivo N
N = int(input("inserisci un numero intero positivo N: "))

# inizializzare la sommma a zero
somma = 0

#calcolare la somma dei primi N numeri pari
for numero in range(2, 2* N + 1, 2):
    somma += numero
    
print(f"la somma dei primi {N} numeri pari è {somma}")


# In[ ]:


# chiedere all utente di inderire un numero intero positivo N
N = int(input("inserisci un numero intero positivo N: "))
lista=[]

#calcolare la somma dei primi N numeri pari
for numero in range(2, 2* N + 1, 2):
    lista.append(numero)
    
print(lista)


# In[ ]:


frase = input("inserisci una frase o una parola: ").lower()
conteggio_vocali = 0
vocali = "aeiou"
for carattere in frase:
    if carattere in vocali:
        conteggio_vocali += 1
print(f"Nella frase inserita ci sono {conteggio_vocali} vocali")


# In[ ]:


import random

numero_da_indovinare = random.randint(1, 100)
tentativi = 0

while True:
    tentativo = int(input("indovina il numero(1-100): "))
    tentativi += 1
    
    if tentativo == numero_da_indovinare:
        print("bravo! hai indovinato il numero", numero_da_indovinare, "in", tentativi, "tentativi")
        break
    elif tentativo < numero_da_indovinare:
              print("il numero è più grande.")
    else:
              print("il numero è più piccolo")
              


# In[ ]:


n = int(input("inserisci un numero intero: "))
fattoriale = 1
if n<0:
    print("numero negativo")
elif n==0:
    print("il fattoriale di zero è 1 per definizione")
else:
    for numero in range(1, n+1):
        fattoriale*=numero
print(f"il fattoriale di {n} è {fattoriale}")


# In[ ]:


N = int(input("inserisci un numero intero positivo N"))
somma = 0
for numero in range(2,2 * N + 1,2):
    somma+=numero
print(f"la somma dei primi {N} numeri pari è {somma}")


# In[ ]:


frase = input("inserisci una frase o una parola: ").lower()
conteggio_vocali = 0
vocali ="aeiou"
for carattere in frase:
    if carattere in vocali:
        conteggio_vocali+=1
print(f"nella frase inserita ci sono {conteggio_vocali} vocali.")


# In[ ]:


import random 
numero_dado = random.randint(1,6)
indovina = int(input("indovina il numero del dado (da 1 a 6): "))
if indovina< 1 or indovina > 6:
    print("numero non ammesso")
elif indovina == numero_dado:
    print(f" complimenti il numero del dado era {numero_dado}. Hai indovinato!")
else:
    print(f"mi dispiace, il numero del dado era {numero_dado}. Meglio fortuna alla prossima volta")


# In[ ]:


popolazione = int(input("inserire popolazione iniziale: "))
anni = int(input("inserisci numero di anni da simulare: "))
tasso_natalità = float(input("inserisci tasso di natalità: "))
tasso_mortalità = float(input("inserisci tasso mortalità: "))
for anno in range(anni):
    nascite = (popolazione * tasso_natalità) /100
    morti = (popolazione * tasso_mortalità) /100
    popolazione += (nascite - morti)
    print(f"anno {anno}: popolazione = {int(popolazione)}")
print("simulazione completata.")


# In[ ]:


import datetime 
today = datetime.datetime.today()
print(f" oggi è il giorno: {today: %d %m %Y} ore: {today: %H %M %S}")


# In[ ]:


print(" Benvenuto nel Convertitore di Unità di Misura!")
scelta = input("cosa desideri convertire? (metri/piedi/chilogrammi/libre): ").lower()
if scelta == "metri":
    valore = float(input("inserisci il valore in metri: "))
    print(f"{valore} metri corrispondono a {risultato} piedi")
elif scelta == "piedi":
    valore = float(input("inserisci il valore in piedi: "))
    print(f"{valore} piedi corrispondono a {risultato} metri")
elif scelta == "":
    valore = float(input("inserisci il valore in piedi: "))
    print(f"{valore} piedi corrispondono a {risultato} metri")


# In[ ]:


n = int(input("inserisci un numero n per calcolare l'n-esimo numero di fibonacci: "))
a=0
b=1
c=1
if n<= 0:
    print("il numero deve essere maggiore di zero.")
elif n == 1:
    risultato = a 
else: 
    for iterazione in range(n-3):
        a = b
        b = c
        c = a + b
    risultato = c
print("L' n-esimo numero di fibonacci è:", risultato)


# In[ ]:


def fibonacci(n):
    fib_series =[0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series  


# In[ ]:


import math
def calcola_area_cerchio(raggio):
    return math.pi * (raggio ** 2)
def calcola_area_rettangolo(base, altezza):
    return base*altezza
def calcola_area_triangolo(base, altezza):
    return (base * altezza) / 2


# In[ ]:


def calcola_bmi(peso, altezza):
    return peso / (altezza ** 2)
def valuta_bmi(bmi):
    if bmi < 18.5:
        return "sottopeso"
    elif 18.5 <= bmi < 24.9:
        return "normopeso"
    elif 25 <= bmi < 29.4:
        return "obeso"
def main():
    print("benvenuto nella calcolatrice bmi")
    peso = float(input("inserisci il tuo peso in chilogrammi:"))
    altezza = float(input("inserisci la tua altezza in metri:"))
    
    bmi = calcola_bmi(peso, altezza)
    valutazione = valuta_bmi(bmi)
    
    print(f"il tuo bmi è {bmi:.2f}, sei classificato come '{valutazione}'.")

if __name__ == "_main_":
    main()


# In[ ]:


def metri_a_piedi(metri):
    return metri * 3.28084
def piedi_a_metri(piedi):
    return piedi / 3.28084
def chilogrammi_a_libbre(libbre):
    return libbre / 2.20462

def selezione(scelta):
    if scelta == "metri":
        valore = float(input("inserici il valore in metri: "))
        risultato = metri_a_piedi(valore)
        print(f"{valore: .3f} metri acorrispondono a {risultato: .3f} metri.")
    elif scelta == "piedi"
        valore = float(input("inserici il valore in piedi: "))
        risultato = piedi_a_metri(valore)
        print(f"{valore: .3f} metri acorrispondono a {risultato: .3f} piedi.")
    elif scelta == "chilogrammi"
        valore = float(input("inserici il valore in chilogrammi: "))
        risultato = piedi_a_metri(valore)
        print(f"{valore: .3f} metri acorrispondono a {risultato: .3f} piedi.")


# In[ ]:


print("Benvenuto nella Calcolatrice di Aree!")

scelta = input("Vuoi calcolare L'area di un cerchio (c),rettangolo(r) o triangolo (t) ")

if scelta == "c":
    raggio = float(input("inserici il raggio del cerchio: "))
    area = calcola_area_cerchio(raggio)
    print(f"L'area del cerchio è {area: .2f}")
elif scelta == "r":
    base = float(input("inserici la base del rettangolo: "))
    altezza = float(input("inserisci l'altezza del rettangolo: "))
    area = calcola_area_rettangolo(base, altezza)
    print(f"L'area del rettangolo è {area: .2f}")
elif scelta == "t":
    base = float(input("inserici la base del triangolo: "))
    altezza = float(input("inserisci l'altezza del triangolo: "))
    area = calcola_area_triangolo(base, altezza)
    print(f"L'area del rettangolo è {area: .2f}")
else:
    print("Scelta non valida. Si prega di inserire c , r o t. ")


# In[ ]:


def calcola_interessi(importo_iniziale , tasso_interesse, periodi_investimento):
    importo_finale = importo_iniziale * (1 + tasso_interesse / 100) ** periodi_investimento
    return importo_finale


# In[ ]:


print("Benvenuto nel Calcolatore di Interessi!")
importo = float(input("inserisci l'importo iniziale: "))
tasso = float(input("inserisci il tasso di interesse annuale (%): "))
periodo = float(input("inserisci il periodo di investimento (anni): "))
importo_finale = calcola_interessi(importo , tasso , periodo)
print(f"L'importo finale dopo {periodo} anni è di {importo_finale: .2f} euro.")


# In[ ]:


calcola_interessi(10000000,400,10)


# In[ ]:


def forza_gravitazionale(m1, m2, r):
    #Costante gravitazionale
    G = 6.67430e-11 #N(m/kg)^2
    
    #calcolo della forza gravitazionale
    F = (G * m1 * m2) / (r ** 2)
    return F


# In[ ]:


massa_terra = 5.972e24
massa_luna = 7.342e22
distanza_terra_luna = 384400000
forza = forza_gravitazionale(massa_terra, massa_luna , distanza_terra_luna)
print(f"Forza gravitazionale tra la terra e la luna: {forza} Newton")


# In[ ]:


from itertools import permutations
k=0

def trova_anagrammi(parola):
    anagrammi = ["".join(p) for p in permutations(parola)]
    return anagrammi


print("Benvenuto nel Risolutore di Anagrammi!")
parola_input = input("inserisci una parola: ").strip().lower()
if len(parola_input) < 2:
    print("inserisci una parola con almeno 2 caratteri.")
else:
    anagrammi = trova_anagrammi(parola_input)
    for anagramma in anagrammi:
        if anagramma != parola_input:
            k+=1
            print(anagramma)
    print(f"Gli anagrammi di '{parola_input}' sono:'{k}'")


# In[ ]:


tassi_di_cambio = {
    "dollari":1.0,
    "euro":0.85,
    "yen":110.41,
}

importo = float(input("inserisci l'importo da convertire: "))
valuta_di_partenza = input("inserisci la valuta di partenza: ").lower()
valuta_destinazione = input("inserisci la valuta di destinazione: ").lower()
if valuta_di_partenza in tassi_di_cambio and valuta_destinazione in tassi_cambio:
    tasso_di_cambio = tassi_di_cambio[valuta_destinazione] / tassi_di_cambio[valuta_di_partenza]
    importo_convertito = importo * tasso_di_cambio

