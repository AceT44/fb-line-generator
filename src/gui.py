from logic import GeneticAlgorithm, FileSaving
from tkinter import messagebox
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

        self.saved_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.ga_frame = tk.Frame(
            self.root,
            bg="white"
        )
        self.left_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )
        self.right_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )
        self.bottom_frame = tk.Frame(
            self.ga_frame,
            bg="white"
        )

        self.create_ga_screen()
        self.create_saved_screen()
        self.main_menu()

    def create_ga_screen(self):  # creates the screen but doesn't load it yet
        self.left_frame.grid(row=0, column=0, padx=5, pady=5)
        self.right_frame.grid(row=0, column=1, padx=5, pady=5)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, pady=5)

        self.line_length_scale = tk.Scale(
            self.left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=2,
            to=10,
            orient=tk.HORIZONTAL,
            label="Number of tricks",
            length=250
        )
        self.line_length_scale.grid(row=0, pady=10)

        self.population_scale = tk.Scale(
            self.left_frame,
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
        self.population_scale.grid(row=1, pady=10)

        self.breedpool_scale = tk.Scale(
            self.left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=2,
            to=3,
            orient=tk.HORIZONTAL,
            label="Breeding pool size",
            length=250
        )
        self.breedpool_scale.grid(row=2, pady=10)

        self.crossover_scale = tk.Scale(
            self.left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="Crossover rate (%)",
            length=250
        )
        self.crossover_scale.grid(row=3, pady=10)

        self.mutation_scale = tk.Scale(
            self.left_frame,
            font=("Arial", 14),
            bg="white",
            fg="black",
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            label="Mutation rate (%)",
            length=250
        )
        self.mutation_scale.grid(row=4, pady=10)

        self.ga_output = tk.Text(
            self.right_frame,
            font=("Arial", 12),
            height=25,
            width=70,
            bg="white",
            fg="black",
            state=tk.DISABLED
        )
        self.ga_output.grid()

        self.generate_btn = tk.Button(
            self.bottom_frame,
            text="GENERATE",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=self.generate
        )
        self.generate_btn.grid(row=0, column=0, padx=10, pady=20)

        self.save_btn = tk.Button(
            self.bottom_frame,
            text="SAVE",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=None
        )
        self.save_btn.grid(row=0, column=1, padx=10, pady=20)

        self.back_btn = tk.Button(
            self.bottom_frame,
            text="BACK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=lambda: self.back_to_menu("ga_screen")
        )
        self.back_btn.grid(row=0, column=2, padx=10, pady=20)

    def create_saved_screen(self):  # creates the screen but doesn't load it yet
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

        back_btn = tk.Button(
            self.saved_frame,
            text="BACK",
            font=("Arial", 16),
            bg="white",
            fg="black",
            height=2,
            width=10,
            command=lambda: self.back_to_menu("saved_screen")
        )
        back_btn.grid(row=1, column=2, padx=10)

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
        self.ga_frame.pack()

    def saved_screen(self):
        self.main_frame.pack_forget()
        self.saved_frame.pack()

    def update_breedpool_scale(self, value):
        population = int(value)

        self.breedpool_scale.config(
            to=population
        )

        if self.breedpool_scale.get() > population:
            self.breedpool_scale.set(population)

    def back_to_menu(self, current_screen):
        if current_screen == "ga_screen":
            self.ga_frame.pack_forget()
            self.main_frame.pack()
        elif current_screen == "saved_screen":
            self.saved_frame.pack_forget()
            self.main_frame.pack()

    def disable_btns(self):
        self.generate_btn.config(
            state=tk.DISABLED
        )
        self.save_btn.config(
            state=tk.DISABLED
        )
        self.back_btn.config(
            state=tk.DISABLED
        )

    def enable_btns(self):
        self.generate_btn.config(
            state=tk.NORMAL
        )
        self.save_btn.config(
            state=tk.NORMAL
        )
        self.back_btn.config(
            state=tk.NORMAL
        )

    def generate(self):
        num_of_tricks = self.line_length_scale.get()
        population_size = self.population_scale.get()
        breeding_pool = self.breedpool_scale.get()
        crossover_rate = self.crossover_scale.get() / 100
        mutation_rate = self.mutation_scale.get() / 100

        if crossover_rate == 0 and mutation_rate == 0:
            messagebox.showerror(
                "Error", "Crossover rate and mutation rate cannot both be zero!"
            )
            return

        self.ga_output.config(
            state=tk.NORMAL
        )
        self.ga_output.delete("1.0", tk.END)
        self.ga_output.config(
            state=tk.DISABLED
        )

        self.disable_btns()

        self.ga.start_ga(
            num_of_tricks,
            population_size,
            breeding_pool,
            crossover_rate,
            mutation_rate,
            self.display_generation
        )

        self.enable_btns()

    def display_generation(self, generation: int, best_line: list, best_fitness: int) -> None:
        self.ga_output.config(
            state=tk.NORMAL
        )

        self.ga_output.insert(
            tk.END, f"Generation {generation}:\n{', '.join(best_line)}\nFitness: {best_fitness}\n\n"
        )
        self.ga_output.see(tk.END)

        self.ga_output.config(
            state=tk.DISABLED
        )

        self.root.update()
