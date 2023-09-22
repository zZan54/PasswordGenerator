import tkinter as tk
import pyperclip
import secrets
import string

class PasswordGenerator():
    def main():
        root = tk.Tk()
        root.title("Password Generator by zZan54")
        root.geometry("500x400")

        generation_info = {
            'pass_len': '',
            'use_inv1': '',
            'use_inv2': '',
            'custom_characters': '',
            'use_uppercase': '',
            'use_lowercase': '',
            'use_numbers': '',
            'copy': ''
        }

        def toggle_custom_characters_entry(*args):
            if custom_characters_var.get() == "True":
                custom_characters_entry.config(state=tk.NORMAL)
            else:
                custom_characters_entry.config(state=tk.DISABLED)

        password_label = tk.Label(root, text="Password: ", font=("", 15))
        password_label.pack()

        pass_len_label = tk.Label(root, text="Password length:")
        pass_len_label.pack()
        pass_len_entry = tk.Entry(root)
        pass_len_entry.pack()

        use_inv1_var = tk.StringVar()
        use_inv1_var.set("None")
        use_inv1_check = tk.Checkbutton(root, text="Use invalid characters 1? (!,@,#,$,%,...)", variable=use_inv1_var, onvalue="True", offvalue="False")
        use_inv1_check.pack()

        use_inv2_var = tk.StringVar()
        use_inv2_var.set("None")
        use_inv2_check = tk.Checkbutton(root, text="Use invalid characters 2? (~, \, |,...)", variable=use_inv2_var, onvalue="True", offvalue="False")
        use_inv2_check.pack()

        custom_characters_var = tk.StringVar()
        custom_characters_var.set("False")
        custom_characters_var.trace_add('write', toggle_custom_characters_entry)
        custom_characters_check = tk.Checkbutton(root, text="Use custom characters?", variable=custom_characters_var, onvalue="True", offvalue="False")
        custom_characters_check.pack()
        custom_characters_entry = tk.Entry(root, state=tk.DISABLED)
        custom_characters_entry.pack()

        use_uppercase_var = tk.StringVar()
        use_uppercase_var.set("None")
        use_uppercase_check = tk.Checkbutton(root, text="Use uppercase characters?", variable=use_uppercase_var, onvalue="True", offvalue="False")
        use_uppercase_check.pack()

        use_lowercase_var = tk.StringVar()
        use_lowercase_var.set("None")
        use_lowercase_check = tk.Checkbutton(root, text="Use lowercase characters?", variable=use_lowercase_var, onvalue="True", offvalue="False")
        use_lowercase_check.pack()

        use_numbers_var = tk.StringVar()
        use_numbers_var.set("None")
        use_numbers_check = tk.Checkbutton(root, text="Use numbers?", variable=use_numbers_var, onvalue="True", offvalue="False")
        use_numbers_check.pack()

        copy_var = tk.StringVar()
        copy_var.set("None")
        copy_check = tk.Checkbutton(root, text="Copy to clipboard?", variable=copy_var, onvalue="True", offvalue="False")
        copy_check.pack()

        def generate_button():
            if pass_len_entry.get() == '':
                generation_info['pass_len'] = 8
            else:
                generation_info['pass_len'] = pass_len_entry.get()

            if use_inv1_var.get() == 'True':
                generation_info["use_inv1"] = "!#$%&/()=?*+'-.,;:_@><}{][" + '"'
            elif use_inv1_var.get() == 'False':
                generation_info["use_inv1"] = ""
            else:
                generation_info["use_inv1"] = ""
            
            if use_inv2_var.get() == 'True':
                generation_info["use_inv2"] = "~ˇ^˘°˛`˙´˝¨¸|\\€"
            elif use_inv2_var.get() == 'False':
                generation_info["use_inv2"] = ""
            else:
                generation_info["use_inv2"] = ""

            if custom_characters_var.get() == 'True':
                generation_info['custom_characters'] = custom_characters_entry.get()
            elif custom_characters_var.get() == 'False':
                generation_info['custom_characters'] = ""
            else:
                generation_info['custom_characters'] = ""

            if use_uppercase_var.get() == 'True':
                generation_info['use_uppercase'] = string.ascii_uppercase
            elif use_uppercase_var.get() == 'False':
                generation_info['use_uppercase'] = ""
            else:
                generation_info['use_uppercase'] = ""

            if use_lowercase_var.get() == 'True':
                generation_info['use_lowercase'] = string.ascii_lowercase
            elif use_lowercase_var.get() == 'False':
                generation_info['use_uppercase'] = ""
            else:
                generation_info['use_uppercase'] = ""

            if use_numbers_var.get() == 'True':
                generation_info['use_numbers'] = string.digits
            elif use_numbers_var.get() == 'False':
                generation_info['use_numbers'] = ""
            else:
                generation_info['use_numbers'] = ""

            if copy_var.get() == 'True':
                generation_info['copy'] = copy_var.get()
            elif copy_var.get() == 'False':
                generation_info['copy'] = copy_var.get()
            else:
                generation_info['copy'] = 'False'
            
            final_password = PasswordGenerator.generate_password(int(generation_info['pass_len']), generation_info['use_inv1'], 
                                                                 generation_info['use_inv2'], generation_info['custom_characters'], 
                                                                 generation_info['use_uppercase'], generation_info['use_lowercase'], 
                                                                 generation_info['use_numbers'], generation_info['copy'])
            
            password_label.config(text = f"Password: {final_password}")

        generate_password_button = tk.Button(root, text="Generate password", command=generate_button, width=15, height=2, font=("", 10))
        generate_password_button.pack()

        root.mainloop()

    def generate_password(pass_len, use_inv1, use_inv2, custom_characters, use_uppercase, use_lowercase, use_numbers, copy):
        chars = use_inv1 + use_inv2 + custom_characters + use_uppercase + use_lowercase + use_numbers
        password = "".join(secrets.choice(chars) for _ in range(pass_len))

        if copy == 'True':
            pyperclip.copy(password)
            return password
        
        elif copy == 'False':
            return password
        
        else:
            pass

if __name__ == "__main__":
    PasswordGenerator.main()