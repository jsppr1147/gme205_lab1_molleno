#LabEx Title  
Computational Thinking Foundations: Python, VS Code, and GitHub  

#Setting Up  
- In this laboratory exercise, project folders were created and configurations for this python environment was setup in VS code.  
- Hello world was also run to check if everything is running smoothly.   
- Github account was also connected for this exercise.   
- Familiarization of git config, git init, git push, git commit, git pull.    
- To further increase familiarity, a script was encoded to practice pushing and pulling in GitHub.   
-----------------------------------------------------------------  

#Data Inspection Script:  
This exercise was performed to understand the basic structure, quality and limits of a dataset before further computations.   

## Current Features  
- Imports Pandas, Matplotlib, JSON, and OS modules. 
- Loads spatial point data from `data/pts.csv`.  
- Print basic dataset shape (row, columns) and column names   
- Validation of required lat and lon columns.  
- Check for invalid coordinate ranges (lon: -180,180 and lat -90,90)  
- Added bounding box for maximizing the display of the points  

## Added Features
1. Generates output files: a.) summary JSON for quality metrics and bounding box data and b.) a scatter plot preview of coordinates

## Reflection

This pipeline inspects row counts, null values, and basic spatial boundaries to ensure spatial datasets are structural before further processing. It assumes that the CSV contains valid numeric `lon` and `lat` values framed within standard WGS84 geographic boundaries (-180 to 180 longitude, -90 to 90 latitude). Also, it automatically checks for missing columns, nulls, and out-of-bound coordinates to prevent pipeline crashes down the line, but a human must still verify if points physically make sense. Finally, if the dataset scales to millions of rows, reading the entire CSV into memory with Pandas will cause high RAM usage, and plotting every point with Matplotlib will cause massive rendering slowdowns. Scaling up would require bulk processing tools alongside spatial indexing or binning for visualization.