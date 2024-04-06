import os
from pathlib import Path 
import logging


logging.basicConfig(level=logging.INFO,format="[%(asctime)s] : %(message)s")

list_of_files=[
    "src/__init__.py",
    "src/helper.py",
    "research/trails.ipynb",
    "static/style.css",
    "templates/index.html",
    ".env",
    "app.py",
    "store_index.py",
    "README.md"

]


for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path) # this will split directory and file name

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory:{file_dir} forthe  file name:{file_name}")
    
    if (not os.path.exists(file_path)) or(os.path.getsize(file_path)==0):
        with open(file_path,"w") as obj:
            pass
            logging.info(f"Creating empty files:{file_path}")

    else:
        logging.info(f"{file_name} is already exists")