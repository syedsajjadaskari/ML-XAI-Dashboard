import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name='ML_XAI_DASHBOARD'

list_file=[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/__init__py",
    f"src/{package_name}/utlis/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integrtion/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params/yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "research/st_01_trails.ipynb"
]


for filepath in list_file:
    filepath=Path(filepath)
    #to seprate the filename and directory
    filedir, filename=os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory: {filename} for file {filename}")
        #if not exist file size is equal to zero creat a file 
        #To not to overright
    if(not os.path.exists(filepath)) or (os.path.getsize) == 0: 
            with open(filepath, "w") as f:
                pass #create a empty file
                logging.info(f"creating empty file{filedir}")
    else:
            logging.info(f"file already exists{filename}")