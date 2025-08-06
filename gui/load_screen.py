import customtkinter as ctk
from gui.result_screen import ResultScreen

class LoadScreen(ctk.CTkFrame):
    def __init__(self, master, file_path):
        super().__init__(master)
        self.master = master
        self.file_path = file_path

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container_frame = ctk.CTkFrame(self, fg_color="transparent")
        container_frame.grid(row=0, column=0)
        
        label = ctk.CTkLabel(container_frame, text="Processing Image...", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=(20, 10))

        self.progress_bar = ctk.CTkProgressBar(container_frame, mode="indeterminate", width=300)
        self.progress_bar.pack(pady=10)
        self.progress_bar.start()  

        self.after(2000, self.show_result)

    def show_result(self):
        self.progress_bar.stop()  # Hentikan animasi progress bar
        self.pack_forget()  # Sembunyikan load screen
        
        result_screen = ResultScreen(self.master, self.file_path)
        result_screen.pack(fill="both", expand=True)