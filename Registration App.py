# import customtkinter as ctk

# window = ctk.CTk()
# window.geometry("300x500")
# window.title("Registration App")

# def register():
#     file =open("users.text", "+a")
#     name =namee.get()
#     email =emaile.get()
#     phone =Phonee.get()
#     file.write(f"{name},{email},{phone}\n")
#     file.close()
#     status.configure(text="Registration SuccessFull")

# # namee = ctk.CTkEntry(window, placeholder_text="Enter Name")
# namee.pack(pady=10)
# emaile = ctk.CTkEntry(window, placeholder_text="Enter Email")
# emaile.pack(pady=10)
# Phonee = ctk.CTkEntry(window, placeholder_text="Enter Phone")
# Phonee.pack(pady=10)

# # regBut = ctk.CTkButton(window,text="Register", command=lambda:register()).pack()
# # status = ctk.CTkLabel(window, text="")
# # status.pack()

# # window.mainloop()

# import customtkinter as ctk

# window = ctk.CTk()
# window.geometry("300x500")
# window.title("Registration App")

# def register():
#     file = open("users.text","+a")
#     n =name.get()
#     e = email.get()
#     p = phone.get()
#     file.write(f"{n},{e},{p}\n")
#     file.close()
#     status.configure(text="Registration Sucessfull")


# name=ctk.CTkEntry(window , placeholder_text="Enter Name")
# name.pack(pady=10)

# email=ctk.CTkEntry(window , placeholder_text="Enter Email")
# email.pack(pady=10) 

# phone=ctk.CTkEntry(window , placeholder_text="Enter Phone")
# phone.pack(pady=10)   

# regbut=ctk.CTkButton(window, text="Register",command=lambda:register()).pack()
# status =ctk.CTkLabel(window, text="")
# status.pack()


# # window.mainloop()

# import customtkinter as ctk

# window = ctk.CTk()
# window.geometry("300x500")
# window.title("Registration App")

# def LoadData():
#     file = open("users.txt","+r")
#     data = file.readlines()
    
#     for i in data:
#         label = ctk.CTkLabel(window, text=f"{i.replace(",","\t")}", font=("Vardana",10)).pack()



# def registration():
#     file =open("users.txt", "+a")
#     n=name.get()
#     e=email.get()
#     p=phone.get()
#     file.write(f"{n},{e},{p}\n")
#     file.close()
#     status.configure(text="Registration Sucessfull")
#     LoadData()

# name = ctk.CTkEntry(window,placeholder_text="Enter name")
# name.pack(pady=10)

    
# email = ctk.CTkEntry(window,placeholder_text="Enter Email")
# email.pack(pady=10)

    
# phone = ctk.CTkEntry(window,placeholder_text="Enter Phone")
# phone.pack(pady=10)

# regbut=ctk.CTkButton(window, text="Register",command=lambda:registration()).pack()
# status =ctk.CTkLabel( window, text="")
# status.pack()

# # LoadData()
# # window.mainloop()


# import customtkinter as ctk

# window =ctk.CTk()
# window.geometry("500x500")
# window.title("Studen Registarion App")

# def LoadData():
#     file =open("users.txt", "+r")
#     data= file.readlines()
#     for i in data:
#         label =ctk.CTkLabel(window, text=f"{i.replace(",", "/t")}", font=("Arial",10)).pack()


# def registartion():
#     file= open("users.txt","+a")
#     n= name.get()
#     e= email.get()
#     p= phone.get()
#     file.write(f"{n},{e},{p}/n")
#     file.close()
#     status.configure(text="Registartion Sucessfull")
#     LoadData()

# name=ctk.CTkEntry(window,placeholder_text="Student Name")
# name.pack(pady=10)

# email=ctk.CTkEntry(window,placeholder_text="Enter Email")
# email.pack(pady=10)

# phone=ctk.CTkEntry(window,placeholder_text="Enter Number")
# phone.pack(pady=10)

# course=ctk.CTkOptionMenu(window, values=["Python","Web devlopment", "java"])
# course.pack()

# regbut=ctk.CTkButton(window, text="Register", command=lambda:registartion()).pack()
# command=lambda:registartion()
# status=ctk.CTkLabel(window,text="")
# status.pack()
# LoadData()

# window.mainloop()


# import customtkinter as ctk

# window = ctk.CTk()

# window.geometry("500x500")
# window.title("Student Registration App")


# # Student Name
# name = ctk.CTkEntry(
#     window,
#     placeholder_text="Student Name"
# )
# name.pack(pady=10)


# # Email
# email = ctk.CTkEntry(
#     window,
#     placeholder_text="Email"
# )
# email.pack(pady=10)


# # Phone Number
# phone = ctk.CTkEntry(
#     window,
#     placeholder_text="Phone Number"
# )
# phone.pack(pady=10)


# # Course
# course = ctk.CTkOptionMenu(
#     window,
#     values=["Python", "Java", "Web Development", "Data Science"]
# )
# course.pack(pady=10)


# # Register Button
# regbut = ctk.CTkButton(
#     window,
#     text="Register")
# regbut.pack(pady=10)


# window.mainloop()

from PIL import Image
import customtkinter as ctk

window = ctk.CTk()
window.geometry("500x500")
window.title("Student Registration App")

bg_image=ctk.CTkImage(light_image=Image.open("student app.png"), size=(200,500))
bg_label=ctk.CTkLabel(window,image=bg_image,text="")
bg_label.place(x=0,y=0)

def LoadData():
    file=open("users.txt", "+r")
    data= file.readlines()
    for i in data:
        label=ctk.CTkLabel(window, text=f"{i.replace(",","/t")})", font=("Arial",10)).pack()

def registration():
    file=open("users.txt","+a")
    n=name.get()
    e=email.get()
    p=phone.get()
    file.write(f"{n},{e},{p}/n")
    file.close()
    status.configure(text="Registration Sucessfull")
    LoadData()


name=ctk.CTkEntry(window,placeholder_text="Enter Name")
name.pack(pady=10)


email=ctk.CTkEntry(window,placeholder_text="Enter Email")
email.pack(pady=10)

phone=ctk.CTkEntry(window,placeholder_text="Enter phone")
phone.pack(pady=10)

course=ctk.CTkOptionMenu(window,values=["python","java","Data Science","Web Development"])
course.pack()
regbut=ctk.CTkButton(window,text="Register",command=lambda:registration()).pack()
command=lambda:registration()
status=ctk.CTkLabel(window,text="")
status.pack()
LoadData()


window.mainloop()






