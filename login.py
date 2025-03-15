import tkinter as tk
import customtkinter as ctk
import mysql.connector as conn

# Pages
import home

# Functions
def loginAction():
    errLb.configure(text="")
    userval=usernm.get().strip()
    pwdval=pwd.get().strip()

    if(userval=="" or pwdval==""):
        print("The username or password cannot be empty")
        errLb.configure(text="The username or password cannot be empty")
    else:
        cur.execute(f"select * from logindet where uname='{userval}'and pwd='{pwdval}'")
        retval=cur.fetchall()
        print(retval)
        if(len(retval)==0):
            print("Incorrect  Username or Password")
            errLb.configure(text="Incorrect  Username or Password")

        else:
            cur.execute(f"select name from logindet where uname='{userval}'")
            name=cur.fetchall()
            print("Logged in correctly")
            root.iconify()
            home.render(name[0][0])
            
def createAcc():
    def render():
        usernmLb.grid(row=1,column=0,padx=2,pady=10)
        usernmEnt.grid(row=1,column=1,padx=2,pady=10)
        pwdLb.grid(row=2,column=0,padx=2,pady=10)
        pwdEnt.grid(row=2,column=1,padx=2,pady=10)
        cerrLb.grid(row=4,column=3,padx=2,pady=10,sticky="ew")
        createaccBt.grid(row=4,column=0,padx=2,pady=10)

    def createAction():
        cerrLb.configure(text="")
        userval=createUsrnm.get().strip()
        pwdval=createpwd.get().strip()

        if(userval=="" or pwdval==""):
            print("The username or password cannot be empty")
            cerrLb.configure(text="The username or password cannot be empty")
        else:
            cur.execute(f"select * from logindet where uname='{userval}'and pwd='{pwdval}'")
            retval=cur.fetchall()
            print(retval)
            if(len(retval)>0):
                print("The user already exist")
                cerrLb.configure(text="The user already exist")

            else:
                cur.fetchall()
                cur.execute(f"insert into logindet values('{userval}','{userval}','{pwdval}')")
                db.commit()
                print("User added")
                cerrLb.configure(text="User added")


    createaccPg=tk.Toplevel(root)
    createaccPg.title('Create Account')
    createaccPg.geometry("600x700")
    createaccPg.config(bg="grey20")
    usernmLb=ctk.CTkLabel(
            createaccPg,
            text="Username:  ",
            bg_color="grey20",
            text_color="sandy brown",
            font=("Comic Sans MS",19)
            )
    createUsrnm=tk.StringVar()
    usernmEnt=ctk.CTkEntry(
            createaccPg,
            corner_radius=19,
            bg_color="grey20",
            textvariable=createUsrnm,
            font=("Comic Sans MS",19)
            )
    pwdLb=ctk.CTkLabel(
            createaccPg,
            text="Password:  ",
            bg_color="grey20",
            text_color="sandy brown",
            font=("Comic Sans MS",19)
            )
    createpwd=tk.StringVar()
    pwdEnt=ctk.CTkEntry(
            createaccPg,
            corner_radius=19,
            bg_color="grey20",
            textvariable=createpwd,
            show="*",
            font=("Comic Sans MS",19)
            )
    cerrLb=ctk.CTkLabel(
    createaccPg,text="",
    bg_color="grey20",
    text_color="tomato3",
    font=("Comic Sans MS",19)
    )
    createaccBt=ctk.CTkButton(
        createaccPg,text="Create account",
        fg_color="bisque3",
        font=("Comic Sans MS",19),
        bg_color="grey20",
        command=createAction,
        corner_radius=20,
        text_color="black",
        hover_color="dim grey"
        )
    render()

# Database config
db=conn.connect(host="localhost",user="root",password="namith",database="chatapp")
cur=db.cursor()

# Root window config
root=ctk.CTk()
root.title("Chat Application")
root.geometry("600x700")
root.config(bg="grey20")

# Username
usernmLb=ctk.CTkLabel(
    root,
    text="Username:  ",
    bg_color="grey20",
    text_color="sandy brown",
    font=("Comic Sans MS",19)
    )
usernmLb.grid(row=1,column=0,padx=2,pady=10)

usernm=tk.StringVar()
usernmEnt=ctk.CTkEntry(
    root,
    corner_radius=19,
    bg_color="grey20",
    textvariable=usernm,
    font=("Comic Sans MS",19)
    )
usernmEnt.grid(row=1,column=1,padx=2,pady=10)

# Password
pwdLb=ctk.CTkLabel(
    root,
    text="Password:  ",
    bg_color="grey20",
    text_color="sandy brown",
    font=("Comic Sans MS",19)
    )
pwdLb.grid(row=2,column=0,padx=2,pady=10)

pwd=tk.StringVar()
pwdEnt=ctk.CTkEntry(
    root,
    corner_radius=19,
    bg_color="grey20",
    textvariable=pwd,
    show="*",
    font=("Comic Sans MS",19)
    )
pwdEnt.grid(row=2,column=1,padx=2,pady=10)

# Login button
loginBt=ctk.CTkButton(
    root,text="Login",
    fg_color="bisque3",
    font=("Comic Sans MS",19),
    bg_color="grey20",
    command=loginAction,
    corner_radius=20,
    text_color="black",
    hover_color="dim grey"
    )
loginBt.grid(row=3,column=0,padx=2,pady=10)

# Create account button
createaccBt=ctk.CTkButton(
    root,text="Create account",
    fg_color="bisque3",
    font=("Comic Sans MS",19),
    bg_color="grey20",
    command=createAcc,
    corner_radius=20,
    text_color="black",
    hover_color="dim grey"
    )
createaccBt.grid(row=4,column=0,padx=2,pady=10)

# Error label
errLb=ctk.CTkLabel(
    root,text="",
    bg_color="grey20",
    text_color="tomato3",
    font=("Comic Sans MS",19)
    )
errLb.grid(row=4,column=3,padx=2,pady=10,sticky="ew")
root.mainloop()