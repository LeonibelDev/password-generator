import tkinter
import customtkinter
from passwordGenerator import getPassword

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x250")
app.title("generate random password")

class interface:
    def __init__(self, app):
        self.text = customtkinter.CTkTextbox(master=app, width=210, height=40, font=("Segoe UI", 20), state="disabled")
        self.text.place(relx=0.2, rely=0.2)
        
        
        self.button = customtkinter.CTkButton(master=app, text="Generate password", command=lambda:self.generate())
        self.button.place(relx=0.3, rely=0.4)
        
        self.withNumbers = customtkinter.CTkCheckBox(master=app, text="Add numbers", onvalue=True, offvalue=False, height=3, border_width=1)
        self.withNumbers.place(relx=0.2, rely=0.6)
        
        self.withUpper = customtkinter.CTkCheckBox(master=app, text="Add uppercase letters", onvalue=True, offvalue=False, height=3, border_width=1)
        self.withUpper.place(relx=0.2, rely=0.7)    
        
        self.withLower = customtkinter.CTkCheckBox(master=app, text="Add lowercase letters", onvalue=True, offvalue=False, height=3, border_width=1)
        self.withLower.place(relx=0.2, rely=0.8)
        
    def generate(self):
        self.password = getPassword().generateRandomPassword()
        self.text.configure(state="normal")
        self.text.delete("0.0", "end")
        self.text.insert("0.0", self.password)
        self.text.configure(state="disabled")
            
if __name__ == "__main__":
    interface(app)
    app.mainloop()