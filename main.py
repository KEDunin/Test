import datetime
import os
from pathlib import Path
t_dir=os.getcwd()
print(t_dir)
p_dir=Path(t_dir) / "Files"
print(Path(t_dir).exists())

print(datetime.datetime(2022, 1, 1))
t_dir = os.getcwd()
with open("Project.py", "w")as file:
    file.write("123")
a = os.path.join(t_dir, "Project.py")
