import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageTk
import numpy as np
from sklearn.cluster import KMeans
from tkinter import filedialog
from utils import resource_path

def hex_to_rgb(hex_str):
    """Konversi hex string (tanpa '#') ke tuple RGB."""
    hex_str = hex_str.lstrip('#') 
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

class ResultScreen(ctk.CTkFrame):
    def __init__(self, master, file_path):
        super().__init__(master)
        self.master = master
        self.file_path = file_path

        self.configure(fg_color="#2f2f2f")

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Logo Pigmenta
        logo_img = Image.open(resource_path("assets/logo-pigmenta.png"))
        logo_img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = ctk.CTkLabel(main_frame, image=logo_photo, text="")
        logo_label.image = logo_photo
        logo_label.pack(pady=(20, 20))

        # Preview Image
        self.preview_img = Image.open(file_path).convert("RGB")
        self.preview_img.thumbnail((200, 200), Image.Resampling.LANCZOS)
        preview_photo = CTkImage(self.preview_img, size=(200, 200))
        preview_frame = ctk.CTkFrame(main_frame, fg_color="#666666", width=200, height=200)
        preview_frame.pack(pady=(0, 20))
        preview_label = ctk.CTkLabel(preview_frame, image=preview_photo, text="")
        preview_label.image = preview_photo
        preview_label.pack(expand=True)

        
        select_button = ctk.CTkButton(
            master=main_frame,
            text="Select New Image",
            command=self.select_new_image,
            fg_color="#44579D",
            hover_color="#90A1DC"
        )
        select_button.pack(pady=(0, 30))

        palette_label = ctk.CTkLabel(main_frame, text="Dominant Color Palette", font=ctk.CTkFont(size=20, weight="bold"))
        palette_label.pack(pady=(0, 10))

        # Extract dominant colors KMeans
        img = Image.open(file_path).convert("RGB")
        img_array = np.array(img)
        pixels = img_array.reshape(-1, 3) / 255.0
        if len(pixels) > 0:
            kmeans = KMeans(n_clusters=3, random_state=42).fit(pixels)
            dominant_colors = kmeans.cluster_centers_ * 255
            dominant_colors = dominant_colors.astype(int)
        else:
            dominant_colors = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

        # Debug
        print("Dominant Colors (KMeans):", dominant_colors)

            
        palette_frame = ctk.CTkFrame(main_frame, fg_color="#ffffff", corner_radius=10)
        palette_frame.pack(pady=10, padx=20)
        self.color_hexes = []
        for i, color in enumerate(dominant_colors):
            color_hex = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
            self.color_hexes.append(color_hex)
            color_circle = ctk.CTkLabel(palette_frame, text="", fg_color=color_hex, width=40, height=40, corner_radius=20)
            color_circle.grid(row=0, column=i, padx=10, pady=10)
            color_text = ctk.CTkLabel(palette_frame, text=color_hex, font=ctk.CTkFont(size=12), text_color="#000000")
            color_text.grid(row=1, column=i, pady=(0, 5))
            download_button = ctk.CTkButton(
                palette_frame,
                text="Download",
                command=lambda idx=i: self.download_palette(idx),
                fg_color="#4a4a4a",
                hover_color="#5a5a5a",
                width=40
            )
            download_button.grid(row=2, column=i, pady=(0, 10))

        
        back_button = ctk.CTkButton(
            master=main_frame,
            text="Back to Menu",
            command=self.go_back,
            fg_color="#44579D",
            hover_color="#90A1DC"
        )
        back_button.pack(pady=20)

    def download_palette(self, index):
        color_hex = self.color_hexes[index]     
        
        rgb_color = hex_to_rgb(color_hex)                       # Konversi hex ke RGB tuple       
        img = Image.new('RGB', (100, 100), color=rgb_color)     # Buat gambar palet warna

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=f"palette_color_{index + 1}.png")
        if file_path:
            img.save(file_path)
            print(f"Downloaded palette color {index + 1} to {file_path}")

    def select_new_image(self):
        from tkinter import filedialog
        from gui.load_screen import LoadScreen
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            print(f"New image selected: {file_path}")
            self.destroy()
            self.master.load_screen = LoadScreen(self.master, file_path)
            self.master.load_screen.pack(fill="both", expand=True)

    def go_back(self):
        self.pack_forget()
        self.master.main_menu.pack(fill="both", expand=True)