import customtkinter as ctk
from PIL import Image, ImageTk
from gui.main_menu import MainMenu

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class PigmentaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pigmenta")
        self.geometry("460x640")
        self.resizable(False, False)

        self.iconbitmap("assets/pigmenta-icon.ico")

        self.main_menu = MainMenu(self)
        self.main_menu.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = PigmentaApp()
    app.mainloop()