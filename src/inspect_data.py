import os
import json
import pandas as pd
import matplotlib.pyplot as plt
# -----------------------------
# Paths
# -----------------------------
DATA_PATH = "data/points.csv"
OUTPUT_DIR = "output"
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "summary.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "preview.png")

#step 1: read the data
try: 
    df = pd.read_csv(DATA_PATH)  
except FileNotFoundError: 
    print(f"Error: Cannot find file at '{DATA_PATH}'.") 
    print("Make sure you have: data/points.csv") 
    raise 