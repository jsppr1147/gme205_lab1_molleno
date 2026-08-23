#LabEx Title  
Computational Thinking Foundations: Python, VS Code, and GitHub  

#Setting Up  
In this laboratory exercise, project folders were created and configurations for this python environment was setup in VS code. 
Hello world was also run to check if everything is running smoothly.  
Github account was also connected for this exercise.  
Familiarization of git config, git init, git push, git commit, git pull.   
To further increase familiarity, a script was encoded to practice pushing and pulling in GitHub.   
-----------------------------------------------------------------  

#Data Inspection Script:  
This exercise was performed to understand the basic structure, quality and limits of a dataset before further computations.   

## Current Features  
- Imports Pandas, Matplotlib, JSON, and OS modules. 
- Loads spatial point data from `data/pts.csv`.  
- Print basic dataset shape (row, columns) and column names   
- Validation of required lat and lon columns.  
- Check for invalid coordinate ranges (lon: -180,180 and lat -90,90)  
## Added Features
1. Added bounding box for maximizing the display of the points