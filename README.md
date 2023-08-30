# Undergrad-Research
A repo for all of the tutorials and framework for undergrad research

## Getting Started
### Install Miniconda
1. Download Miniconda from https://docs.conda.io/en/latest/miniconda.html
2. Install Miniconda

### Create a Conda Environment
1. Open a terminal
2. Use the following command to create a conda environment from the environment.yml file
``` conda env create -f environment.yml ```
3. Activate the environment
``` conda activate myenv ```

### Add the Conda Environment to Jupyter Notebook
1. Open a terminal
2. Use the following command to add the conda environment to Jupyter Notebook
``` python -m ipykernel install --user --name myenv --display-name "Python (myenv)" ```
3. Open Jupyter Notebook
4. Select the kernel "Python (myenv)" from the Kernel menu
