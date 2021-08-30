import tkinter as tk
from PIL import Image,ImageTk
import pygame
from tkinter import messagebox
import qrcode

def generate():
    if len(name_entry.get()) < 3:
        messagebox.showerror("Try Again","Enter valid name")
    if len(country_entry.get()) == 0:
        messagebox.showerror("Error","Enter Country Name")
    if len(anime_entry.get()) == 0:
        messagebox.showerror("Error","Enter Anime Name")
    if len(manga_entry.get()) == 0:
        messagebox.showerror("Error","Enter Manga Name")
    if len(main_entry.get()) == 0:
        messagebox.showerror("Error","Enter Main Character Name")
    if len(side_entry.get()) == 0:
        messagebox.showerror("Error","Enter Side Character Name")
    if len(movie_entry.get()) == 0:
        messagebox.showerror("Error","Enter Anime Movie Name")
    if len(waifu_entry.get()) == 0:
        messagebox.showerror("Error","Enter Waifu Name")
    if len(male_va_entry.get()) == 0:
        messagebox.showerror("Error","Enter Male VA Name")
    if len(female_va_entry.get()) == 0:
        messagebox.showerror("Error","Enter Female VA Name")
    else:
        qr = qrcode.make("Name:{}\nCountry:{}\nFavourite Anime:{}\nFavourite Manga:{}\nFavourite Main Character:{}\nFavourite Side Character:{}\nWaifu:{}\nMovie:{}\nFavourite Male Voice Actor:{}\nFavourite Female Voice Actor:{}".format(name_entry.get(),country_entry.get(),anime_entry.get(),manga_entry.get(),main_entry.get(),side_entry.get(),waifu_entry.get(),movie_entry.get(),male_va_entry.get(),female_va_entry.get()))
        qr.save("{}'s_Anime_Profile.png".format(name_entry.get().strip()))
        messagebox.showinfo("Success","Well Your a certified weeb \n QRCODE saved")
        name_entry.delete(0,'end')
        country_entry.delete(0,'end')
        anime_entry.delete(0,'end')
        manga_entry.delete(0,'end')
        movie_entry.delete(0,'end')
        male_va_entry.delete(0,'end')
        female_va_entry.delete(0,'end')
        waifu_entry.delete(0,'end')
        main_entry.delete(0,'end')
        side_entry.delete(0,'end')

def main():
    root = tk.Tk()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music.ogg')
    pygame.mixer.music.play(-1,6)

    root.geometry("675x605+185+60")
    root.resizable(False,False)
    root.title("Anime-Weeb Profile")
    # adjust the opacity for background image
    img = Image.open('bg_img.png')
    data=img.getdata() #list of tuples
    img = img.resize((685,610), Image.ANTIALIAS)
    bg= ImageTk.PhotoImage(img)
    canvas= tk.Canvas(root)
    canvas.pack(expand=True, fill= "both")
    canvas.create_image(0,0,image=bg,anchor="nw")

    head = tk.Label(root,text="Create Your Anime QR Code",font=("arial",20,"bold"),bg="skyblue").place(x=125,y=12)

    name_label = tk.Label(root,text="Name",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=80)
    country_label = tk.Label(root,text="Country",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=130)
    anime_label = tk.Label(root,text="Favourite Anime",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=180)
    manga_label = tk.Label(root,text="Favourite Manga",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=230)
    main_label = tk.Label(root,text="Main Character",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=280)
    side_label = tk.Label(root,text="Side Character",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=330)
    waifu_label = tk.Label(root,text="Waifu",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=380)
    movie_label = tk.Label(root,text="Favourite Movie",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=430)
    male_va_label = tk.Label(root,text="Favourite Male VA",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=480)
    female_va_label = tk.Label(root,text="Favourite Female VA",font=("arial",15,"bold"),bg="skyblue").place(x=10,y=530)

    name =tk.StringVar()
    country =tk.StringVar()
    anime  = tk.StringVar()
    manga = tk.StringVar()
    movie = tk.StringVar()
    main_c= tk.StringVar()
    side= tk.StringVar()
    waifu =tk.StringVar()
    male_seiyuu= tk.StringVar()
    female_seiyuu =tk.StringVar()

    global name_entry,country_entry,anime_entry,manga_entry,main_entry,side_entry,waifu_entry,movie_entry,male_va_entry,female_va_entry

    name_entry = tk.Entry(root,textvariable=name,font=("arial",15),bd=4)
    name_entry.place(x=225,y=80)
    country_entry = tk.Entry(root,textvariable=country,font=("arial",15),bd=4)
    country_entry.place(x=225,y=130)
    anime_entry = tk.Entry(root,textvariable=anime,font=("arial",15),bd=4)
    anime_entry.place(x=225,y=180)
    manga_entry = tk.Entry(root,textvariable=manga,font=("arial",15),bd=4)
    manga_entry.place(x=225,y=230)
    main_entry = tk.Entry(root,textvariable=main_c,font=("arial",15),bd=4)
    main_entry.place(x=225,y=280)
    side_entry = tk.Entry(root,textvariable=side,font=("arial",15),bd=4)
    side_entry.place(x=225,y=330)
    waifu_entry = tk.Entry(root,textvariable=waifu,font=("arial",15),bd=4)
    waifu_entry.place(x=225,y=380)
    movie_entry = tk.Entry(root,textvariable=movie,font=("arial",15),bd=4)
    movie_entry.place(x=225,y=430)
    male_va_entry = tk.Entry(root,textvariable=male_seiyuu,font=("arial",15),bd=4)
    male_va_entry.place(x=225,y=480)
    female_va_entry = tk.Entry(root,textvariable=female_seiyuu,font=("arial",15),bd=4)
    female_va_entry.place(x=225,y=530)

    btn = tk.Button(root,text="Generate QRCODE",font=("arial",14,"bold"),bd=5,fg="white",bg="blue",command=generate).place(x=465,y=555)
    messagebox.showinfo("Ora Gumbare Gumare","Its difficult to choose just one, yet give your best 🤡")
    root.mainloop()

if __name__ == '__main__':
    main()