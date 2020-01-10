# ML workshop MolSim 2020

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jaRBPC3u-ianxiUGLsfZqMgYirEKfn_j)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kjappelbaum/ml_molsim2020.git/master?filepath=molsim_ml)
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/download/releases/3.7.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## How to run it
This exercise will need in some parts more computational resources than most of
the other exercises. If you have a modern laptop and want to use it, we
recommend to use it. If you do not want to use your machine or the cluster, you
can also run the exercises on Google Colab or Binder.

### Run it locally (recommended) 
We recommend that you run the exercises locally on your on machine. For this you
need to create a conda environment using the `envrionment.yml` file we provide
    in this repository. 

If you do not already have anaconda installed, head over to
https://docs.conda.io/en/latest/miniconda.html and install a python 3.7 version
for your operarting system. 

Then, create a new folder and clone this repository
```(bash) 
mkdir molsim_ml 
git clone https://github.com/kjappelbaum/ml_molsim2020.git
cd ml_molsim2020
```
Now, you can create a new conda environment.

```(bash) 
conda env create --name molsim_ml --file=environment.yml
```
After this completed, active the environment and start a jupyter notebook

```(bash)
conda activate molsim_ml
jupyter notebook
```

### Use it on Google CoLab 
Here, you can use relatively powerful computing resources from Google for free. 
For this click the "Open in CoLab" button on the top.
Use run the first three cells to install the dependencies. Then you should be
able to use the notebook in CoLab. Make sure that you make a copy into your
Google Drive and that you work on this copy.

If you have a Google Account from your organization, e.g. university, you might
need to log out and use your personal account as many organizations block
third-party applications. 

### Use it on Binder
It can take some time to build the instance and the computing resources are
limited. For this, just click on the Binder button.

If you see a 404 error, click on the juypter symbol and you will be redirected
to a filebrowser where you can select `molsim_ml.ipynb`.


