## About
These instructions are to be followed to recreate the figures from @adepennart Lund University Masters research project.

This program is fully run on the terminal.
## Before starting

A **Catmaid account** and a **neuPRINT account** are needed for this code.

Before downloading this repository it should be stated that without a Catmaid and neuPRINT account following the instructions below becomes obsolete. These accounts allow access to the neuron databases.

For a **Catmaid account**, please contact me at adepennnart@gmail.com, stating you would like to open an account to access our Catmaid database.

For a neuPRINT account, an account can easily be created with the following link. https://neuprint.janelia.org/



Additionaly, two different conda environments (conda environments explained below) are created for this code due to the nature of working with two different databses. One conda environment is created for accessing the catmaid database(all the insect neurons except drosophila) and one for the neuprint database(drosophila).

# (PART I): insect (except drosophila) neuron plotting
## Installation
The code can be directly installed from github (green Code button, top right).

Make sure to change into the downloaded directory, the code should resemble something like this.
```bash=
cd Downloads/report_figure_make
```
### Conda environment
First make sure conda is installed. If you do not have conda, refer to online resources on how to install conda.
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

Once installed, we can make a conda environment.

```bash=
#create new
conda create --name pymaid
#activate
conda activate pymaid
```

### Python version
The python version for running this script is python=3.6
```bash=
conda install python=3.6
```

### Dependencies
The script runs with pip\==21.3.1 and python-catmaid==2.0.4

Update your dependencies, if you do not already have the versions for these dependencies.

```bash=
pip install --upgrade pip==21.3.1 wheel==0.37.1 setuptools==59.6.0

pip install python-catmaid==2.0.4 -U
```

### Make environmental variables


The environmental variables are the login credentials required to access catmaid online. Which include, the catmaid server, and your API token (the API token replaces your username and password to the server). Your API token can be found following the instructions on this website:
https://catmaid.readthedocs.io/en/stable/api.html#api-token

There are two ways to access catmaid online. The deemed safer version will be covered here, for the other option refer to this link:
https://pymaid.readthedocs.io/en/latest/source/intro.html

Add your new environmental variables via the bash_profile file.

```bash=
nano ~/.bash_profile
```
When in nano, add the following lines to your code, with  respect to your account. 
```bash=
export CATMAID_SERVER='https://www.your.catmaid-server.org'
export CATMAID_API_TOKEN='your_token'
```
Don't forget to source.
```bash=
source ~/.bash_profile
```
Verify after sourcing that you are still in your pymaid conda environment.

a bash script will be used to produce 3 figures, but firstly the script needs to be activated.
```bash=
#activate the bash script
chmod +x plot.sh
```

The script should be all ready to run.
```bash=
./plot.sh
```
3 plots should have appeared in a new folder called output.

# (PART II): Drosophila neuron plotting 
## Installation
### Conda environment
A second conda environment can now be made. 
```bash=
conda create -n neuprint
#activate
conda activate neuprint
```

### Python version
The python version for running this script is python=3.9.12
```bash=
#first deactivate old conda environment
conda deactivate

conda install python=3.9.12
```

### Dependencies
Uses conda to download neuprint-python==0.4.21 package


```bash=
conda install -c flyem-forge neuprint-python==0.4.21
```

Additionally the script runs with matplotlib\==3.5.2 and navis==2.0.4

```bash=
pip install matplotlib==3.5.2 navis==2.0.4
```

### Make environmental variables

The environmental variables are the login credentials required to access the neuprint server. Here a token is the environmental variable needed. Your token can be found following the instructions on this website:
https://connectome-neuprint.github.io/neuprint-python/docs/quickstart.html

There are two ways to access the neuprint server. The deemed safer version will be covered here, for the other option refer to this link:
https://connectome-neuprint.github.io/neuprint-python/docs/quickstart.html

Add your new environmental variables via the bash_profile file.

```bash=
nano ~/.bash_profile
```
When in nano, add the following lines to your code, with  respect to your account. 
```bash=
export NEUPRINT_APPLICATION_CREDENTIALS='my-token'
```
Don't forget to source.
```bash=
source ~/.bash_profile
```
Verify after sourcing that you are still in your neuprint conda environment.

The script should be all ready to run.
```bash=
python3 plot_neuprint.py
```
