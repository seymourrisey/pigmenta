import customtkinter as ctk
from gui.result_screen import ResultScreen
import time

class LoadScreen(ctk.CTkFrame):
    def __init__(self, master, file_path):
        super().__init__(master)
        self.master = master
        self.file_path = file_path

        # Loading label
        label = ctk.CTkLabel(self, text="Processing Image...", font=ctk.CTkFont(size=20))
        label.pack(pady=20)

        # Simulate loading (replace with actual processing later)
        self.after(2000, self.show_result)

    def show_result(self):
        self.pack_forget()  # Hide load screen
        result_screen = ResultScreen(self.master, self.file_path)
        result_screen.pack(fill="both", expand=True)