import customtkinter as ctk
from PIL import Image
import numpy as np

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, file_path):
        super().__init__(master)
        self.master = master
        self.file_path = file_path

        # Placeholder for result
        label = ctk.CTkLabel(self, text="Dominant Colors:", font=ctk.CTkFont(size=20))
        label.pack(pady=20)

        # Extract dominant colors (simplified example)
        img = Image.open(file_path).convert("RGB")
        img_array = np.array(img)
        pixels = img_array.reshape(-1, 3)
        unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
        top_3_indices = np.argsort(counts)[-3:][::-1]
        dominant_colors = unique_colors[top_3_indices]

        # Display colors (placeholder)
        for color in dominant_colors:
            color_hex = '#%02x%02x%02x' % tuple(color)
            color_label = ctk.CTkLabel(self, text=f"Color: {color_hex}", text_color=color_hex)
            color_label.pack(pady=5)

        # Back button
        back_button = ctk.CTkButton(self, text="Back to Menu", command=self.go_back)
        back_button.pack(pady=20)

    def go_back(self):
        self.pack_forget()
        self.master.main_menu.pack(fill="both", expand=True)