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
