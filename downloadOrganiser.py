import os 
import shutil 
import fnmatch
from pathlib import Path 

# Change to desired file path where files to be sorted are
path = '/home/jconner/Downloads'

# scans directory contents and sets to files variable
files = os.scandir(path)

# lists of different file types
imgTypes = ['*.png', '*.jpeg', '*.jpg', '*.gif']
dwldTypes = ['*.deb', '*.zip', '*.exe', '*.dmg']
docTypes = ['*.doc', '*.docx', '*.xlsx', '*.pptx', '*.pdf']
projTypes = ['*.md', '*.fig', '*.java', '*.py', '*.html', '*.css', '*.sql', '*.js']

# Loop for each file within the given directory 
for file in files:

    # checks if file matches imgTypes, and then moves into 'Images' folder
    if any(fnmatch.fnmatch(file, imgType) for imgType in imgTypes):
        p = Path('Images')
        p.mkdir(exist_ok=True)
        shutil.move(file, 'Images/')
    
    # checks if file matches dwldTypes, and then moves into 'Downloaded' folder
    elif any(fnmatch.fnmatch(file, dwldType) for dwldType in dwldTypes):
        p = Path('Downloaded')
        p.mkdir(exist_ok=True)
        shutil.move(file, 'Downloaded/')

    # checks if file matches docTypes items, and then moves into 'Documents' folder
    elif any(fnmatch.fnmatch(file, docType) for docType in docTypes):
        p = Path('Documents')
        p.mkdir(exist_ok=True)
        shutil.move(file, 'Documents/')

    # Checks if file matches projtypes items, and then moves into 'Project_Files' folder
    elif any(fnmatch.fnmatch(file, projType) for projType in projTypes):
        p = Path('Project_Files')
        p.mkdir(exist_ok=True)
        shutil.move(file, 'Project_Files/')

   # Moves any other category of file into a folder called 'Other'
    else:
        p = Path('Other')
        p.mkdir(exist_ok=True)
        shutil.move(file, 'Other/')
        
            
