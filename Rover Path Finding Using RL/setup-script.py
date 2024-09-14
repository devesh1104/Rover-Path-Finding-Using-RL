# setup.py

import subprocess
import sys

def install_requirements():
    requirements = [
        "numpy",
        "tensorflow",
        "gym",
        "matplotlib",
        "tqdm"
    ]
    
    for package in requirements:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_requirements()
    print("All required packages have been installed.")
