from customtkinter import *
from tkinter import filedialog
import os

set_appearance_mode("dark")
set_default_color_theme("blue")

class Editor:
    def __init__(self, window: CTk):
        self.window = window
        self.window.title("PyEdit")
        self.window.geometry("1024x768")

        self.window.bind("<Control-o>", self.open_file)
        self.window.bind("<Control-s>", self.save_file)
        self.window.bind("<Control-Shift-s>", self.save_file_as)

        self.message_var = StringVar(value="")
        self.message_label = CTkLabel(self.window, textvariable=self.message_var, text_color="white", font=("monospace", 16))
        self.message_label.pack(pady=(0, 5))

        self.current_directory = os.path.dirname(os.path.abspath(__file__))

        self.display_elements()

    def display_elements(self):
        buttons_frame = CTkFrame(self.window)
        buttons_frame.pack()

        self.save_button = CTkButton(buttons_frame, corner_radius=5, text="Save File", font=("monospace", 17), command=self.save_file)
        self.save_button.grid(row=0, column=0, padx=10)

        self.save_as_button = CTkButton(buttons_frame, corner_radius=5, text="Save File As", font=("monospace", 17), command=self.save_file_as)
        self.save_as_button.grid(row=0, column=1, padx=10)

        self.open_button = CTkButton(buttons_frame, corner_radius=5, text="Open File", font=("monospace", 17), command=self.open_file)
        self.open_button.grid(row=0, column=2, padx=10)

        self.text_field = CTkTextbox(window, corner_radius=10, font=("monospace", 18))
        self.text_field.pack(fill=BOTH, expand=True, pady=10, padx=10)
        
    def show_message(self, text, color="white"):
        self.message_var.set(text)
        self.message_label.configure(text_color=color)
        self.window.after(2000, lambda: self.message_var.set(""))

    def open_file(self, event=None):
        self.file = filedialog.askopenfilename()
        with open(self.file, "r") as file:
            file_content = file.read()
            self.text_field.delete(0.0, "end")
            self.text_field.insert("0.0", file_content)

    def save_file(self, event=None):
        if hasattr(self, "file") and self.file:
            with open(self.file, "w") as file:
                file_content = self.text_field.get("0.0", "end-1c")
                file.write(file_content)
                self.show_message("File Saved", color="green")

        else:
            with open(f"{self.current_directory}/untitled", "w") as file:
                file_content = self.text_field.get("0.0", "end-1c")
                file.write(file_content)
                self.show_message("File Saved", color="green")

    def save_file_as(self, event=None):
        file = filedialog.asksaveasfilename()
        print(file)
        with open(file, "w") as file:
            file_content = self.text_field.get("0.0", "end-1c")
            file.write(file_content)
            self.show_message("File Saved", color="green")

if __name__ == "__main__":
    window = CTk()
    editor = Editor(window)
    window.mainloop()
