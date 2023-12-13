from pathlib import Path
import re
input_folder = Path("input")
input_file = input_folder / "day3.txt"
file = open(input_file,"r")
special_chars = re.compile(r"[/=\-!@#$%^&*+]")
engine_schematic = []
for line in file:
    engine_schematic.append(line)
file.close()
print(f"special chars are {special_chars}")