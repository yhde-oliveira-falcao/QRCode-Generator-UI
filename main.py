from tkinter import *
import qrcode
from PIL import Image, ImageDraw
from tkinter import messagebox

# ---------------------------- SAVE QR Code ------------------------------- #
def save():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please make sure to input the URL address.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The URL address is: \nAddress: {website} \nIs it ok "
                                                              f"to save?")
        if is_ok:
            qr = qrcode.QRCode(version=1,
                               box_size=10,
                               border=5)
            qr.add_data(website)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black',
                                back_color='white')
            img.save('qrExport.png')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("QR Code Generator")
window.config(padx=10, pady=100)


# Labels
website_label = Label(text="URL:")
website_label.grid(row=2, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
add_button = Button(text="Generate QR Code", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
