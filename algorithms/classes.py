import customtkinter as ctk
import re


#Class for rotating list
class RotateList(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #Top text
        label = ctk.CTkLabel(self, text="Rotate/Shift the list k times", font=('Helvetica', 20))
        label.pack(pady=20)

        input_label = ctk.CTkLabel(self, text='The format of list should use , or . as seperators\n\nThe format of k is just an int')
        input_label.pack(pady=20)

        self.list_input = ctk.CTkEntry(self, placeholder_text="Enter list here")
        self.list_input.pack(pady=10)

        self.k_input = ctk.CTkEntry(self, placeholder_text="Enter k here")
        self.k_input.pack(pady=10)
        

        # Run script button
        run_button = ctk.CTkButton(self, text="Run Script", command=self.execute_script)
        run_button.pack(pady=10)

        #Output label
        self.output_label = ctk.CTkLabel(self, text='The output is: ')
        self.output_label.pack(pady=50)


        back_button = ctk.CTkButton(self, text="Back to Main Menu", 
                                    command=lambda: controller.show_frame('MainMenu'))
        back_button.pack(side='bottom', pady=20, fill='x')

    #Executing the script
    def execute_script(self):

        #Using a lazy import. Is not very pythonic, but keeps memory lower when only running some scripts
        from algorithms.scripts import rotate_list

        in_list = re.split(r'[.,]', self.list_input.get())
        in_list = list(map(int, in_list))

        k = int(self.k_input.get())
        
        rotated_list = rotate_list.rotate(in_list, k)
        self.output_label.configure(text=f'The output is: {rotated_list}')
        