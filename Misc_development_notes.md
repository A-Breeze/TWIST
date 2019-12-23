<!-- To view this file rendered, try opening VSCode and clicking to open the "Preview" pane -->
# TWIST - Miscellaneous development notes
Other notes that have been accrued and might be helpful while developing. These might be broken out into another repo / blog post + links / etc. at some stage.

## Contents
<!-- This contents is kept up to date *manually* -->
1. [Using conda](#Using-conda)
1. [Issues with packages](#Issues-with-packages)

<div align="right"><a href="#contents">Back to top</a></div>

## Using conda
### Choosing a package to install
Find a list of the available versions of your package:
```
> conda search <name_of_package>
```
- You may want to search a specific channel, in which case include options `--channel conda-forge --override-channels`, for example.

### Adding / removing / updating a package
1. Amend the `environment.yml` as required.
1. In a Terminal, navigate to the project's root.
1. Clean the history<sup id="fn01text">[1](#fn01msg)</sup>, e.g. by:
    - Opening the history
    ```cmd
    > notepad %LOCALAPPDATA%\Continuum\miniconda3\envs\twist_env\conda-meta\history
    ```
    - Deleting the contents of the file and saving
1. Update the installed packages in the conda env to bring it in sync with the `environment.yml`:
    ```
    > conda env update --prune
    ```

<div align="right"><a href="#contents">Back to top</a></div>

## Issues with packages
- `numpy`: Takes a long time to install, specifically because of dependency `mkl` is almost 100KB. After some trial-and-error, I was unable to avoid this.
- `pytest`: Finally got it working by downgrading `pytest`. 
    - Error looked like: `OSError: [WinError 1] Incorrect function`
    - Did not work for version 5.3.2 (tried on various versions of Python, including 3.7.5, 3.6.9 and 3.8.0). 
    - Unable to find the exact error online, although there was some suggestion that it was specifically on Windows 7.

<div align="right"><a href="#contents">Back to top</a></div>

---
<span id="fn01msg">[1](#fn01text)</span>: This is necessary, due to: <https://github.com/conda/conda/issues/7279#issuecomment-389359679>
