# # 1. Escreva uma função que receba uma lista de arquivos de acordo com uma pasta
# # 2. Escreva uma função que valide se o arquivo é uma png ou jpg / imagem
# # 3. Use essa função de validação no método de listar os arquivos
# # 4. Escreva uma função que coloque uma imagem na tela
# # 5. Escreva uma função que pegue todos as imagens e crie uma task para executar 
# # a função de colocar a imagem na tela

# # import os 
# # import asyncio
# #import opencv     : trabalhar com as imagens
# #import tkinter   :  perguntar quantos segundos por imagem

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2

screen = Tk()
screen.title("Digital Signage")

images_folder = None
list_files = None
minutes = None
telinha_aberta = True

def select_folder():
    global images_folder
    global list_files

    images_folder = filedialog.askdirectory()
    list_files = os.listdir(images_folder)
    print(f"Caminho da imagem: {list_files}")
    verify_end_all()
    
def verify_end_all():
    global image_file
    image_file = None
    for img_file in list_files:
        if img_file.lower().endswith(('.png', '.jpg', '.jpeg','.avif','.webp')):
            image_file = os.path.join(images_folder,img_file)
            print(f"Caminho da imagem: {image_file}")
    if not image_file:
            none_image=Tk()
            none_image.withdraw()
            messagebox.showerror("Erro", "Arquivo sem imagem ")
            none_image.destroy()
                    
def in_validate(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False
    
def start_loop():
    try:
        global images_folder
        global list_files
        aberto=True

        minutes = int(time_entry.get())

        screen.destroy()  ######### fechar telinha

        while aberto == True:
            for img_file in list_files:
                if img_file.lower().endswith(('.png', '.jpg', '.jpeg','.avif','.webp')):
                    image_file = os.path.join(images_folder, img_file)
                    print(image_file)
                    
                    mostrar = cv2.imread(image_file)

                    cv2.namedWindow('Fullscreen', cv2.WINDOW_NORMAL)
                    cv2.setWindowProperty('Fullscreen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('Fullscreen', mostrar)

                    key = cv2.waitKey(minutes * 60000) & 0xFF

                    if key == 27: #ESC
                        aberto = False
                        break
            if aberto==False:
                cv2.destroyAllWindows()
    except cv2.error as e:
        image_erro = Tk()
        image_erro.withdraw()
        messagebox.showerror("Erro", "Nome da imagem com Caracter Especial")
        image_erro.destroy()
    except ValueError as e:
        falta_erro = Tk()
        falta_erro.withdraw()
        messagebox.showerror("Erro", "Faltam informações")
        falta_erro.destroy()

validation = screen.register(in_validate)

folder_btn = Button(screen, text="Selecionar Pasta de Imagens", command=select_folder, padx=20)
folder_btn.grid(column=0, row=0, pady=(50,20), padx=50)

quest_lbl = Label(screen, text="Tempo entre as telas:")
quest_lbl.grid(column=0, row=1, padx=100, pady=(20,0))

in_minutes_lbl = Label(screen, text="(em minutos)")
in_minutes_lbl.grid(column=0, row=2)

time_entry = Entry(screen,font=('Arial', 16), validate="key", validatecommand=(validation, "%P"))
time_entry.grid(column=0, row=3, pady=10)

confirm_btn = Button(screen, text="OK", command=start_loop, padx=20)
confirm_btn.grid(column=0, row=4, pady=10)

screen.mainloop() ############ Não fechar telinha