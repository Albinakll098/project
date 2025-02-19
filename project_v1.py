import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Шифрование")
root.geometry("1000x600")
my_font = ctk.CTkFont(family="Roboto", size=20)


widget_button = ctk.CTkButton(master=root)
widget_button.configure(text="Готово", font=my_font,  width=600)

widget_entry = ctk.CTkEntry(master=root)
widget_entry.configure(font=my_font, placeholder_text="Шаг/Кодовое слово", height=80, width=250)


widget_textbox = ctk.CTkTextbox(master=root)
widget_textbox.configure(font=my_font, height=250, width=600)


widget_unactive_textbox = ctk.CTkTextbox(master=root)
widget_unactive_textbox.configure(font=my_font, height=200,  width=970)
widget_unactive_textbox.insert(0.0, "Ответ")
widget_unactive_textbox.configure(state="disabled")


elems = ["Шифр Цезаря", "Шифр с кодовым словом", "Солёный язык", "Азбука Морзе"]
widget_combobox = ctk.CTkComboBox(master=root)
widget_combobox.configure(font=my_font, width=300, values=elems, state="readonly")
widget_combobox.set("Азбука Морзе")


rows, columns = 6, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
widget_combobox.grid(row=0, column=0)
widget_entry.grid(row=2, column=0, rowspan=2)
widget_button.grid(row=3, column=1, columnspan=2)
widget_textbox.grid(row=0, column=1, rowspan=3, columnspan=2)
widget_unactive_textbox.grid(row=4, column=0, rowspan=2, columnspan=3)


root.mainloop()
