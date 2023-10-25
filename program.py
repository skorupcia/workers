import pandas as pd

file = pd.read_excel('pracownicy.xlsx', sheet_name='Arkusz1')

def pracownicy_miesiaca():  
    df_sorted = file.sort_values('Utarg', ascending=False)
    n_pracownicy = df_sorted.head(15)
    print(n_pracownicy)

def czarna_lista():
    df_sorted = file.sort_values('Przepracowane godziny', ascending=True)
    cz_lista = df_sorted.head(5)
    print(cz_lista)

def najdluzszy_staz():
    df_sorted = file.sort_values('Data zatrudnienia', ascending=True)
    staz = df_sorted.head(1)
    print(staz)

def najwieksze_zarobki():
    df_sorted = file.sort_values('Wynagrodzenie', ascending=False)
    salary = df_sorted.head(5)
    print(salary)
