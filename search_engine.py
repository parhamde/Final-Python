# ===============  Importing Suitable Libraries =========================
from tkinter import *
import tkinter as tk
import webbrowser 
from PIL import ImageTk, Image
import googlesearch  #pip install google
# ================== .............. End..........============================

# ================== .......... Window Components........ ============================
#creating main window
root = tk.Tk()

#title of window
root.title("Google")

#window size
root.geometry("800x500")
root.resizable(0,0)

#window icon
root.iconbitmap('Google.ico')

# ========================== ............. End............ =====================
#==============================Action Fuction Code Start here=================================
def callback(url):
       webbrowser.open(url)

def search_query():
        
        query = text.get("1.0","end-1c")
        s = googlesearch.search(query, tld="co.in", num=1, stop=4, pause=7)
        # print(s)
        for j in s:
                # print(j)
                webbrowser.open(j)
#============================== .............. End ................. ===================
# =============================main Desing window ===================================

#lable to Great top to Desing
I1 = Label(root,bg="black",width=500,height=2)
I1.grid(sticky="w")


#apps logo
app_logo=ImageTk.PhotoImage(Image.open('google.png'))
d = Label(root, image=app_logo,borderwidth=0)
d.place(x=15,y=11)
#apps lable
app = Label(root,text="Apps",bg="black",fg="white",cursor="hand2")
app.place(x=40 , y=10)
app.bind("<Button-1>",lambda e: callback("https://www.google.com/webhp?hl=fa"))

#drive logo
d_logo = ImageTk.PhotoImage(Image.open('google drive.png'))
d = Label(root, image= d_logo,borderwidth=0)
d.place(x=95,y=11)
#drive Lable
drive = Label(root,text="Drive",bg="black",fg="white",cursor="hand2")
drive.place(x=120 , y=10)
drive.bind("<Button-1>",lambda e: callback("https://drive.google.com/"))

#Youtube logo
yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
y = Label(root, image= yt_logo,borderwidth=0)
y.place(x=180,y=14)
#drive Lable
yt = Label(root,text="Youtube",bg="black",fg="white",cursor="hand2")
yt.place(x=200 , y=10)
yt.bind("<Button-1>",lambda e: callback("https://youtube.com/"))

#Gmail logo
gm_logo = ImageTk.PhotoImage(Image.open('Gmail.png'))
l2 = Label(root, image = gm_logo,borderwidth=0)
l2.place(x=280 , y=11)

#Gmail label
gmail = Label(root,text="Gmail",bg="black",fg="white",cursor="hand2")
gmail.place(x=320 , y=10)
gmail.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))

#Gmail label
g = Label(root,text="Gmail",cursor="hand2")
g.place(x=620,y=50)
g.bind("<Button-1>",lambda e: callback("https://mail.google.com/mail/"))

#Images label
i = Label(root,text="Images",cursor="hand2")
i.place(x=670,y=50)
i.bind("<Button-1>",lambda e: callback("https://mail.google.co.in/imghp?=en&tab=wi&ogb1/"))

#Singin button
signin = Button(root,text="sign in",font=('roboto',10,'bold'),bg="#4583EC",fg="white",cursor="hand2")
signin.place(x=730,y=50) 
signin.bind("<Button-1>",lambda e: callback("http://google.com"))

#Google logo
g_logo = ImageTk.PhotoImage(Image.open('google logo.png'))
l2 = Label(root, image = g_logo)
l2.place(x=260,y=190)

#search box
text = Text(root,width=75,height=1,relief=RIDGE,font=('roboto',10,'bold'),borderwidth=2)
text.place(x=120,y=300)

#search button
search = Button(root, text="Google Search",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2",command=search_query)
search.place(x=280,y=360)

#Lucky Button
lucky = Button(root, text="i' m Felling Lucky",relief=RIDGE,font=('arial',10),bg="#F3F3F3",fg="#222222",cursor="hand2")
lucky.place(x=400,y=360)
lucky.bind("<Button-1>",lambda e: callback("https://www.google.com/doodles"))

#offered label
offered = Label(root,text="Google offered in:")
offered.place(x=120,y=410)
lang = Label(root,text="Creat white mohammmad_parham",fg="blue")
lang.place(x=230,y=410)

root.mainloop()
