<img width="993" height="695" alt="Screenshot 2026-09-04 at 10 31 11 AM" src="https://github.com/user-attachments/assets/f1892908-fbc3-4d04-9e6d-f16b717a05d3" />

This project experiments with genetic algorithms to generate realistic lines of fingerboard tricks.

This differs from real skateboard lines as some fingerboard rotations are limited by how far the wrist can turn (e.g. fs 180 to switch kickflip is essentially not possible). Thus, this idea was implemented in the GA.

The GA loops through four methods consisting of fitness, selection, crossover, and mutation. Fitness is awarded for lines that offer non-repeated tricks and trick difficulties, consistent stances (e.g. fakie -> switch, regular -> nollie), and varying categories of tricks. Crossover happens from a crossover point line[i] in line = [trick1, trick2, trick3, ...]. Mutation gives each trick in the line a possibility of being randomly swapped out for another trick.

Python 3.14.5
