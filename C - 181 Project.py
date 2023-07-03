from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x500")
root.title("Language Translator")
root.config(bg = "#FFCBC4")

label_1 = Label(root , text = "Language Translator" , bg = "#FFCBC4" , fg = "Black" , font= ("Sylfaen" , 20 , "bold" , "italic"))
label_1.place(relx = 0.5 , rely = 0.1 , anchor= CENTER)

enter_text_label = Label(root , text = " Enter Text ", bg = "#FFCBC4" , fg = "Black" , font= ("Times New Roman" , 16 , "bold" ))
enter_text_label.place(relx = 0.1 , rely= 0.3 , anchor = CENTER)

output_label = Label(root , text = " Output ", bg = "#FFCBC4" , fg = "Black" , font= ("Times New Roman" , 16 , "bold" ))
output_label.place(relx = 0.75 , rely= 0.3 , anchor = CENTER)

entry_dropdown_list = ["English"  , "Hindi"]
entry_dropdown = ttk.Combobox(root, state = "read only" , values = entry_dropdown_list , justify= "right")
entry_dropdown.place(relx = 0.2  , rely= 0.3 , anchor = CENTER)

output_dropdown_list = ["Hindi"  , "English"]
output_dropdown = ttk.Combobox(root, state = "read only" , values = entry_dropdown_list , justify= "right")
output_dropdown.place(relx = 0.83  , rely= 0.3 , anchor = CENTER)

entry_area = Text(root , height= 20 , width= 65)
entry_area.place(relx = 0.2 , rely = 0.6, anchor = CENTER)

output_area = Text(root , height= 20 , width= 65)
output_area.place(relx = 0.8 , rely = 0.6, anchor = CENTER)

translate_btn = Button(root , text = "Translate" , bg = "pink" , fg = "Black" , height= 2 , width = 12 , font = ("Imprint MT Shadow" , 15 , "bold" , "italic"))
translate_btn.place(relx= 0.5 , rely = 0.9 , anchor = CENTER)






root.mainloop()