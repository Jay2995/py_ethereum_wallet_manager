from tkinter import *
from wallet_generator import *
import csv;
from tkinter import messagebox;
BLACK = '#000000';
GREEN = "#355E3B";




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def update_labels():
    wallet_info = generate_ethereum_wallet();
    wallet_address_result.config(text=wallet_info["address"]);
    wallet_PK_result.config(text=wallet_info["private_key"]);

def clear():
    wallet_address_result.config(text='');
    wallet_PK_result.config(text='');
    wallet_name_entry.delete(0,'end');
    wallet_usecase_entry.delete(0,'end');



# # ---------------------------- SAVE WALLET ------------------------------- #
def add_wallet():
    wallet_name_text = wallet_name_entry.get();
    wallet_usecase_text = wallet_usecase_entry.get();
    wallet_address_text = wallet_address_result.cget('text'); 
    wallet_PK_text = wallet_PK_result.cget('text'); 

    if len(wallet_name_text) == 0 or len(wallet_usecase_text) == 0 or len(wallet_address_text) == 0 or len(wallet_PK_text) == 0:
        messagebox.showerror(title="ERROR", message="missing fields");
    else:
        is_ok = messagebox.askokcancel(title=wallet_name_text, message=f"Verify data: \n{wallet_name_text}, {wallet_usecase_text} \nIs it ok to save?")
        if is_ok:
            with open('wallets.txt', mode='a') as file:
                file.write(f"Wallet Name: {wallet_name_text}, Wallet use-case: {wallet_usecase_text}, Wallet address: {wallet_address_text}, Wallet Pk: {wallet_PK_text} \n")
            clear();

# ---------------------------- UI SETUP ------------------------------- #

window = Tk();
window.title("Ethereum wallet manager");
window.config(padx=40, pady=20, bg=BLACK);
canvas = Canvas(height=100, width=180, bg=BLACK, highlightthickness=0);
logo = PhotoImage(file="logo.png");
canvas.create_image(100,50, image=logo);
canvas.grid(column=1,row=1);

title_label = Label(text="Ethereum wallet manager", fg=GREEN, bg = BLACK, font=("Arial", 15));
title_label.grid(column=1, row=0);


# Labels
wallet_name = Label(text="Wallet name: ", fg=GREEN, bg = BLACK, font=("Arial", 10));
wallet_name.grid(column=0, row=2);
wallet_usecase = Label(text="Wallet usecase: ", fg=GREEN, bg = BLACK, font=("Arial", 10));
wallet_usecase.grid(column=0, row=3);
wallet_address = Label(text="Wallet address: ", fg=GREEN, bg = BLACK, font=("Arial", 10));
wallet_address.grid(column=0, row=4);
wallet_PK = Label(text="Wallet PK: ", fg=GREEN, bg = BLACK, font=("Arial", 10));
wallet_PK.grid(column=0, row=5);

#result label
wallet_address_result = Label(text="", fg=GREEN, bg = BLACK, font=("Arial", 8));
wallet_address_result.grid(column=1, row=4);

wallet_PK_result = Label(text="", fg=GREEN, bg = BLACK, font=("Arial", 8));
wallet_PK_result.grid(column=1, row=5);

#buttons
generate_button = Button(text="Generate Wallet", command=update_labels);
generate_button.grid(column=0, row=6);

# clear_button = Button(text="Clear", command=clear);
# clear_button.grid(column=4, row=4);

add_button = Button(text="Add", width=36, command=add_wallet);
add_button.grid(column=1, row=6);
#entries
wallet_name_entry = Entry(width=35, bg=BLACK, fg=GREEN);
wallet_name_entry.focus();
wallet_name_entry.grid(column=1, row=2, columnspan=2);
wallet_usecase_entry = Entry(width=35, bg=BLACK, fg=GREEN)
wallet_usecase_entry.grid(column=1, row=3, columnspan=2);

window.mainloop()