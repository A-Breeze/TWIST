<!-- To view this file rendered, try opening VSCode and clicking to open the "Preview" pane -->
# TWIST - Two-Way Interaction Simulator and Tester
An app to visualise how interactions in linear models work by allowing you to:
- **Simulate** data points from **two** explanatory variables (by specifying their joint distribution), and the response variable (by specifying the mean response).
- Fit a model to **test** what explanatory variables would be selected in a modelling process, and compare this to the true distribution.

Try adjusting the mean response surface by giving it a **twist** to add an interaction variable!

## Contents
<!-- This contents is kept up to date *manually* -->
1. [How to start up the development environment](#How-to-start-up-the-development-environment)
1. [Development resources](#Development-resources)

<div align="right"><a href="#contents">Back to top</a></div>

## How to start up the development environment
1. Clone the repo and navigate to the root directory (in Anaconda Prompt).
1. Set up the conda environment:
    ```cmd
    (base) > conda env create -f environment.yml
    ```
1. Activate the conda env and start PyCharm. This ensures that the PyCharm terminal window opens in the correct conda env.
    ```
    (base) > conda activate twist_env
    (twist_env) > "%LOCALAPPDATA%\JetBrains\PyCharm Community Edition 2019.3\bin\pycharm64.exe"  # Or wherever your PyCharm is installed
    ```
1. Create a new project in the root directory, with the project's interpreter set to the conda-env's interpreter, which you get into the clipboard by:
    ```
    (twist_env) > where python | clip
    ```

<div align="right"><a href="#contents">Back to top</a></div>

## Development resources
See the following files for more details about the project and development plan:
1. [`Project_Structure.md`](https://github.com/A-Breeze/TWIST/blob/master/Project_Structure.md): Manual documentation of the folders and files that make up the project.
1. [`TODO.md`](https://github.com/A-Breeze/TWIST/blob/master/TODO.md): Development plan for releases.

<div align="right"><a href="#contents">Back to top</a></div>
