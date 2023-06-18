from tkinter import *
from Screen.Login_window import LoginScreen

if __name__ == '__main__':
    root = Tk()  # Tworzenie okna głównego
    root.iconbitmap("favicon.ico")  # Ustawienie ikony dla okna

    login_screen = LoginScreen(root)  # Tworzenie instancji LoginScreen

    login_screen.pack(fill=BOTH, expand=True)  # Dodanie LoginScreen do okna głównego i rozszerzenie na całe okno

    root.mainloop()  # Uruchomienie głównej pętli aplikacji




