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


## Useful Links
* [Jupyter Notebook](https://jupyter.org/)
* [Python](https://www.python.org/)
* [PyTorch](https://pytorch.org/)
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [Jet Measurement overveiw] (https://arxiv.org/pdf/1705.01974.pdf)
* [Jet Measurement paper] (https://arxiv.org/pdf/1802.00927.pdf)
* [Bash Scripting Tutorial] (https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
* [Bash scripting cheat sheet] (https://hpc.ua.edu/wp-content/uploads/2022/02/Linux_bash_cheat_sheet.pdf)