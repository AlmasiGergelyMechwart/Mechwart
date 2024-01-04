import tkinter as tk

class CustomTooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_visible = False

        # Bind events to show/hide the tooltip
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        if not self.tooltip_visible:
            # x, y, _, _ = self.widget.bbox("insert")
            x, y = 0, 0
            x += self.widget.winfo_x() + event.x
            y += self.widget.winfo_y() + event.y
            self.tooltip_label = tk.Label(text=self.text, background="lightyellow", relief="solid", borderwidth=1)
            self.tooltip_label.place(x=x, y=y)
            self.tooltip_visible = True

    def hide_tooltip(self, event):
        if self.tooltip_visible:
            self.tooltip_label.place_forget()
            self.tooltip_visible = False

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Tooltip Example")
    button = tk.Button(root, text="Hover Me")
    button.pack(padx=20, pady=20)
    tooltip = CustomTooltip(button, "This is a custom tooltip")
    root.mainloop()
