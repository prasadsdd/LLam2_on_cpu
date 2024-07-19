import os
from pathlib import Path
import logging

# logging madhe aaplyala (asctime) --> current execution time aani (message)--> message display hoto.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

## aalyala je konte folder create karayche aahet tyanchi list dili aahe , tya folder madhe kontya file 
# pahije aahet tyanchi nave dili aahet.

list_of_files = [
    "src/__init__.py",
    "src/run_local.py",
    "src/helper.py",
    "model/instruction.txt",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb",

]

## folder aani file separate karnyasathi khalil code aahe

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    ## aapan ekhadya folder chya file madhe code lihila asel aani parat aapan python temmplate.py hi command 
    # run keli tr to folder part bannar nahi. karan khali aapan getsize use kel aahe size 0 asel trch to navin
    # folder kiva file create karel     

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")