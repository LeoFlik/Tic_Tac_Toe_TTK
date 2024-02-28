# from typing import Tuple
# from customtkinter import CTk,CTkButton,CTkFrame,CTkLabel
# from tkinter import messagebox,ttk

# class MainWidget(CTk):
#   def __init__(self):
#     super().__init__()
#     self.geometry(f'{500}x{700}')
#     self.title('Tic-Tac-Toe Game')
#     self.setting_btn()
    
#   def setting_btn(self):
#         style = ttk.Style()
#         style.configure("TButton", padding=(60,60))
#         btn = ttk.Button(self, text="", style="TButton")
#         index =0
#         for c in range(3):
#            for r in range(3): 
#               btn[index]=btn.grid(column=c,row=r)
#               index +=1
#               print(index)
      


    



from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel
from tkinter import messagebox, ttk

class MainWidget(CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{500}x{500}')
        self.title('Tic-Tac-Toe Game')
        self.config(background='grey')

        self.button = self.setting_btn()
        
   

    def setting_btn(self):
        style = ttk.Style()
        style.configure("TButton", padding=(60, 60))

        buttons = []
        for c in range(3):
            for r in range(3):
                btn = ttk.Button(self, text="", style="TButton")
                btn.grid(column=c, row=r,padx=5,pady=4)
                if c == 0 :
                  btn.grid(padx=(20,0))  # Adjust the padx values as needed
                if r == 0:
                  btn.grid(pady=(20, 0))  # Adjust the pady values as needed
                buttons.append(btn)
                

        # Now you can access the buttons using the 'buttons' list.
        # For example, to access the button at row=0, column=1, you can use buttons[1].
   

if __name__ == '__main__':
    app = MainWidget()
    app.mainloop()
  