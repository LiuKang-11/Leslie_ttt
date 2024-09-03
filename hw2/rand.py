#This module provides a function to generate a random array using system commands.
import subprocess

def random_array(arr): #    Fills an array with random integers generated using the system's shuf command.
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
