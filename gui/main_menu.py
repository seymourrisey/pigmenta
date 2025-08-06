import customtkinter as ctk
from PIL import Image, ImageTk
from gui.load_screen import LoadScreen

class MainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Load logo
        logo_img = Image.open("assets/logo-pigmenta.png")
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(self, image=logo_photo, text="")
        logo_label.image = logo_photo  # Keep a reference!
        logo_label.pack(pady=20)


        # Select Image Button
        self.select_button = ctk.CTkButton(self, text="Select Image", command=self.on_select_image)
        self.select_button.pack(pady=20)

    def on_select_image(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            print(f"Image selected: {file_path}")
            self.load_screen = LoadScreen(self.master, file_path)
            self.pack_forget()  # Hide main menu
            self.load_screen.pack(fill="both", expand=True)
