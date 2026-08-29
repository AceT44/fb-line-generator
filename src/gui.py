from logic import GeneticAlgorithm, FileSaving
import tkinter as tk


class GUI:
    def __init__(self, root):
        self.ga = GeneticAlgorithm()
        self.fs = FileSaving()

        self.root = root
        self.root.config(
            bg="white"
        )
        self.root.geometry("1000x700")
        self.root.resizable(False, False)

        quit_btn = tk.Button(
            self.root,
            text="X",
            font=("Arial", 20),
            bg="white",
            fg="black",
            command=self.root.destroy
        )
        quit_btn.pack(anchor="nw", padx=10, pady=10)

        self.main_menu()

    def main_menu(self):
        self.main_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.main_frame.pack()

        top_label = tk.Label(
            self.main_frame,
            text="********************************",
            font=("Arial", 30),
            bg="white",
            fg="black"
        )
        top_label.grid(row=0, column=0, pady=20)

        menu_start_btn = tk.Button(
            self.main_frame,
            text="GENERATE LINES",
            font=("Arial", 20),
            bg="white",
            fg="black",
            height=2,
            width=18,
            command=self.ga_screen
        )
        menu_start_btn.grid(row=1, column=0, pady=10)

        saved_btn = tk.Button(
            self.main_frame,
            text="SAVED LINES",
            font=("Arial", 20),
            bg="white",
            fg="black",
            height=2,
            width=18,
            command=self.saved_screen
        )
        saved_btn.grid(row=2, column=0, pady=10)

        bottom_label = tk.Label(
            self.main_frame,
            text="\n\n\n\n\n********************************",
            font=("Arial", 30),
            bg="white",
            fg="black"
        )
        bottom_label.grid(row=3, column=0, pady=20)

    def ga_screen(self):
        self.main_frame.pack_forget()

        self.ga_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.ga_frame.pack()

        left_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )
        left_frame.grid(row=0, column=0, padx=5, pady=5)

        right_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )
        right_frame.grid(row=0, column=1, padx=5, pady=5)

        bottom_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )
        bottom_frame.grid(row=1, column=0, columnspan=2, pady=5)

        population_scale = tk.Scale(
            left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=3,
            to=1000,
            orient=tk.HORIZONTAL,
            label="Population size",
            length=250,
            command=self.update_breedpool_scale
        )
        population_scale.grid(row=0)

        self.breedpool_scale = tk.Scale(
            left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=2,
            to=3,
            orient=tk.HORIZONTAL,
            label="Breeding pool size",
            length=250
        )
        self.breedpool_scale.grid(row=1)

        crossover_scale = tk.Scale(
            left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="Crossover rate",
            length=250
        )
        crossover_scale.grid(row=2)

        mutation_scale = tk.Scale(
            left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="Mutation rate",
            length=250
        )
        mutation_scale.grid(row=3)

        ga_output = tk.Text(
            right_frame,
            font=("Arial", 16),
            height=20,
            width=55,
            bg="white",
            fg="black",
            state=tk.DISABLED
        )
        ga_output.grid()

        generate_btn = tk.Button(
            bottom_frame,
            text="GENERATE",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=None
        )
        generate_btn.grid(row=0, column=0, padx=10, pady=20)

        self.back_btn = tk.Button(
            bottom_frame,
            text="BACK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=lambda: self.back_to_menu("ga_screen")
        )
        self.back_btn.grid(row=0, column=1, padx=10, pady=20)

    def update_breedpool_scale(self, value):
        population = int(value)

        self.breedpool_scale.config(
            to=population
        )

        if self.breedpool_scale.get() > population:
            self.breedpool_scale.set(population)

    def saved_screen(self):
        self.main_frame.pack_forget()

        self.saved_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.saved_frame.pack()

        saved_lines_box = tk.Listbox(
            self.saved_frame,
            font=("Arial", 16),
            bg="white",
            fg="black",
            width=80,
            height=19
        )
        saved_lines_box.grid(row=0, column=0, columnspan=4, pady=30)

        del_btn = tk.Button(
            self.saved_frame,
            text="DELETE",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=None
        )
        del_btn.grid(row=1, column=1, padx=10)

        self.back_btn = tk.Button(
            self.saved_frame,
            text="BACK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=lambda: self.back_to_menu("saved_screen")
        )
        self.back_btn.grid(row=1, column=2, padx=10)

    def back_to_menu(self, current_screen):
        if current_screen == "ga_screen":
            self.ga_frame.pack_forget()
            self.main_frame.pack()
        elif current_screen == "saved_screen":
            self.saved_frame.pack_forget()
            self.main_frame.pack()
