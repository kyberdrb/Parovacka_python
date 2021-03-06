from tkinter import Tk, Text, Button, Label
import gui.tk_widget_operations as tk_ops
from assignment import assignment
import pyperclip


class GuiTk:
    def __init__(self, pa_root_window, pa_window_width, pa_window_height):
        self.master = pa_root_window
        self.window_width = pa_window_width
        self.window_height = pa_window_height
        self.set_up_window()
        self.add_widgets()
        self.assignments = None

    def set_up_window(self):
        self.master.title("Párovačka")
        window_dimensions = \
            (str(round(self.window_width))) + \
            "x" + \
            (str(round(self.window_height)))
        self.master.geometry(window_dimensions)
        self.master.grid()

    def add_widgets(self):
        self.button_make_couples = Button(
            self.master,
            text="Spáruj",
            width=10,
            command=self.make_couples
        )
        self.button_make_couples.grid(row=0, column=0, rowspan=2, sticky="NSEW")

        l_participants = Label(self.master, height=1, text="Učastníci")
        l_participants.grid(row=0, column=1, sticky="NSEW")

        l_couples = Label(self.master, height=1, text="Dvojice")
        l_couples.grid(row=0, column=2, sticky="NSEW")

        self.tw_participants = Text(self.master, width=30, height=25)
        self.tw_participants.grid(row=1, column=1, sticky="NSEW")
        self.tw_participants.bind("<Control-c>", lambda e: self.copy_text(e))

        self.tw_couples = Text(self.master, width=60, height=25, state='disabled')
        self.tw_couples.grid(row=1, column=2, sticky="NSEW")
        self.tw_couples.bind("<Control-c>", lambda e: self.copy_text(e))

        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)

    def copy_text(self, event):
        text_to_copy = self.tw_couples.selection_get()
        pyperclip.copy(text_to_copy)

    def make_couples(self):
        tk_ops.clear_text_widget(self.tw_couples)
        self.assignments = assignment.Assignments(
            self.retrieve_list_of_participants())
        self.display_participants_without_blank_chars(
            self.assignments.get_giftees_names())
        self.assignments.create_couples()
        self.display_couples()

    def retrieve_list_of_participants(self):
        participants = self.tw_participants.get("1.0", "end-1c")
        participants_names = participants.split()
        return participants_names

    def display_participants_without_blank_chars(self, pa_names):
        tk_ops.clear_text_widget(self.tw_participants)
        tk_ops.fill_text_widget(self.tw_participants, pa_names)

    def display_couples(self):
        tk_ops.clear_text_widget(self.tw_participants)
        tk_ops.fill_text_widget(
            self.tw_participants,
            self.assignments.get_gifters_names())
        tk_ops.fill_text_widget(
            self.tw_couples,
            self.assignments.list_of_couples())


if __name__ == "__main__":
    root_window = Tk()
    window_width = root_window.winfo_screenwidth() / 2
    window_height = root_window.winfo_screenheight() / 2
    GuiTk(root_window, window_width, window_height)
    root_window.mainloop()
