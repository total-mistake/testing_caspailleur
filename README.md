# A project to test and learn the Caspailleur math package
This is part of the student work for the Project Activities (Testing) course. The goal was to study the math package Caspailleur (https://github.com/EgorDudyrev/caspailleur) and write some BDD tests for it.

## Project structure
- **Example on test data.py**: contains a simple example of how to interact with Caspailleur.
- **features**: a directory with “.feature” files (Gherkin scripts).
- **features\steps**: a directory with python files that define script steps in featute.

## Installation and startup
### **1. Clone the repository** 
Use the git clone command to clone the repository to your computer:
```console
git clone https://github.com/total-mistake/testing_caspailleur
```

### **2. Install dependencies** 
Run the following command to install all required dependencies from the requirements.txt file:
```console
pip install -r requirements.txt
```

### **3. Run the tests**
To run all BDD tests use this command in terminal:
```console
behave
```
