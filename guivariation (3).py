#average
window = Tk()
window.lift()
window.attributes("-topmost", True)
window.geometry("1000x600")
window.title('extremely intelligent, sentient program')
canvas = Canvas(
    window,
    bg="#DD5D5D",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    55.0,
    255.0,
    400.0487365722656,
    299.74695587158203,
    fill="#C4C4C4",
    outline="")

rect5 = canvas.create_rectangle(
    55.0,
    255.0,
    237.96531677246094,
    299.74695587158203,
    fill="#6FA545",
    outline="")

rect7 = canvas.create_rectangle(
    523.0,
    14.0,
    997.4132995605469,
    254.63917541503906,
    fill="#141414",
    outline="")

rect9 = canvas.create_text(
    535.0,
    19.0,
    anchor="nw",
    text="System Info:",
    fill="#FFFFFF",
    font=("Orienta Regular", 23 * -1)
)

canvas.create_text(
    535.0,
    50.0,
    anchor="nw",
    text=f"CPU: {cpuinfo.get_cpu_info()['brand_raw']}",
    fill="#FFFFFF",
    font=("PontanoSans Regular", 20 * -1)
)

# noinspection PyUnboundLocalVariable
canvas.create_text(
    535.0,
    80.0,
    anchor="nw",
    text=f"GPU: {gpu.name}" f" (" f"{gpu.memoryTotal / 1000}GB" f" VRAM)",
    fill="#FFFFFF",
    font=("PontanoSans Regular", 20 * -1)

)

canvas.create_text(
    535.0,
    110.0,
    anchor="nw",
    text=f"RAM: {get_size(svmem.total)}",
    fill="#FFFFFF",
    font=("PontanoSans Regular", 20 * -1)

)

canvas.create_text(
    535.0,
    140.0,
    anchor="nw",
    text=f"Motherboard: {my_system.Model}",
    fill="#FFFFFF",
    font=("PontanoSans Regular", 20 * -1)
)

canvas.create_text(
    535.0,
    170.0,
    anchor="nw",
    text=f"System Architecture: {my_system.SystemType}",
    fill="#FFFFFF",
    font=("PontanoSans Regular", 20 * -1)
)

canvas.create_rectangle(
    181.0,
    398.0,
    819.0,
    546.0,
    fill="#C4C4C4",
    outline="")

canvas.create_text(
    443.0,
    400.0,
    anchor="nw",
    text="Feedback:",
    fill="#000000",
    font=("PontanoSans Regular", 20 * -1)
)

canvas.create_text(
    193.0,
    430.0,
    anchor="nw",
    text="You're on the average side. You'll be fine for a few years at the least,\n"
         "but don't expect intensive tasks to work smoothly.\n",
    fill="#000000",
    font=("PontanoSans Regular", 20 * -1)
)

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("assets/tick.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1 = Label(image=test, borderwidth=0, highlightthickness=0)
# Position image
label1.place(x=92, y=9)

window.resizable(True, True)
window.mainloop()
