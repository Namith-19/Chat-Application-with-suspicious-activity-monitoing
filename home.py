import tkinter as tk
import customtkinter as ctk
import mysql.connector as conn
import App

def render(name):
    global root
    root=ctk.CTk()

    root.title("Chat Application")
    root.geometry("700x700")
    root.config(bg="grey20")

    titleLb=ctk.CTkLabel(
        root,
        text=f"""🏠 Home Page\n Welcome {name}""",
        bg_color="grey20",
        text_color="sandy brown",
        font=("Comic Sans MS",19)
        )
    titleLb.grid(row=0,column=0,sticky="w")

    logoutBt=ctk.CTkButton(
        root,text="Logout",
        fg_color="grey20",
        font=("Comic Sans MS",19),
        bg_color="grey20",
        command=logout,
        corner_radius=20,
        text_color="black",
        hover_color="dim grey"
        )
    logoutBt.grid(row=0,column=0,sticky="e")
    root.grid_columnconfigure(0,weight=1)
    root.grid_rowconfigure(1,weight=1)
    mainFrame=ctk.CTkFrame(root,bg_color="grey20",border_width=1,corner_radius=15,width=100,height=600)
    mainFrame.grid(row=1,column=0,sticky="nsew",padx=8,pady=8)
    mainFrame.columnconfigure(0,weight=1)
    contactBt=ctk.CTkButton(mainFrame,text="Contact 1",command=lambda :App.application_start(2645,"10.9.21.8","client"))
    contactBt.grid(row=0,column=0,sticky="ew")
    root.mainloop()

def logout():
    root.destroy()
# render("xyz")


