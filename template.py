import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

proj_name = "LibManSys"

list_of_files=[
    f"src/{proj_name}/__init__.py",
    f"src/{proj_name}/Book.py",
    f"src/{proj_name}/Patron.py",
    f"src/logger.py",
    f"src/exception.py",
    f"src/utils.py",
    "setup.py",
    "requirements.txt",
    "main.py"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"folder {file_dir} created for file {file_name}")

    if (not os.path.exists(file_path) or os.path.getsize(file_path)==0):
        with open (file_path,"w") as f:
            pass
            logging.info("file created")
            

    else:
        logging.info("file created")