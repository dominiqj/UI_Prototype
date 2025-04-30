import tkinter
from tkinter import *
from tkinter import  ttk

root = tkinter.Tk()
root.geometry('400x260')
root.resizable(False, False)
root.title('Keanu Helper')
# root.configure(bg='skyblue')

button_clear_1 = Button(root,
                      text='Clear Desktop',
                      width=24,
                      pady=3,
                      )
button_clear_1.place(x=10, y=10)

button_clear_2 = Button(root,
                      text='Clear Downloads',
                      width=24,
                      pady=3,
                      )
button_clear_2.place(x=10, y=45)

button_move = Button(root,
                    text='Import Save',
                    width=24,
                    pady=3,
                    )
button_move.place(x=10, y=80)

button_build_final = Button(root,
                            text='Run Final',
                            width=24,
                            pady=3,
                            )
button_build_final.place(x=10, y=115)

button_build_ep1_final = Button(root,
                                text='Run Final + EP1',
                                width=24,
                                pady=3,
                                )
button_build_ep1_final.place(x=10, y=150)

button_build_release = Button(root,
                              text='Run Release',
                              width=24,
                              pady=3,
                              )
button_build_release.place(x=10, y=185)

button_build_ep1_release = Button(root,
                                  text='Run Release + EP1',
                                  width=24,
                                  pady=3
                                  )
button_build_ep1_release.place(x=10, y=220)

# build_branch = tkinter.Label(root, text='Build Branch')
# build_branch.place(x=200, y=120)

def check_value():
    checkbox_var.get()

checkbox_var = tkinter.BooleanVar()
delete_after = ttk.Checkbutton(root, text='Delete After Import', variable=checkbox_var

                               )
delete_after.place(x=200, y=84)

select_branch = ttk.Combobox(root,
                             values=['Main', 'Release', 'Staging'],
                             )
select_branch.set('Main')
select_branch.place(x=200, y=120)

# print(checkbox_var.get()) odczytanie wartości

root.mainloop()