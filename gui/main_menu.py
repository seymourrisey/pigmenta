import customtkinter as ctk
from PIL import Image, ImageTk
from gui.load_screen import LoadScreen
from utils import resource_path

class MainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(expand=True, fill="both")

        logo_img = Image.open(resource_path("assets/logo-pigmenta.png"))

        logo_img.thumbnail((400, 400), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(main_frame, image=logo_photo, text="")
        logo_label.image = logo_photo  
        logo_label.pack(pady=(240, 20))  

        self.select_button = ctk.CTkButton(main_frame, text="Select Image", command=self.on_select_image)
        self.select_button.pack(pady=0)

    def on_select_image(self):
        from tkinter import filedialog
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            print(f"Image selected: {file_path}")
            self.load_screen = LoadScreen(self.master, file_path)
            self.pack_forget()  
            self.load_screen.pack(fill="both", expand=True)