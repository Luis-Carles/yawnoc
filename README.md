# Yawnoc
![unnamed](https://user-images.githubusercontent.com/124795845/217583084-e11eb1ec-15b2-4dc0-8c30-d68838f1fe52.gif)

Python Implementation of Conway's Game of Life in its traditional concept using PyOpenGL and its application as music visualizer using Fluidsynth and Pygame.

## Requirements
You need to have the Anaconda software installed with a Python version equal to or greater than 3.7.

If you are using **Windows** or **MAC OS X**:

 - First install Anaconda with **Python 3.7** or more recent, which you can find [here.](https://www.anaconda.com/products/distribution#windows)
 
 - Start the [Anaconda Prompt.](https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-prompt-win)

If you are using **Linux**:

 - For very old versions of Python, it may be advisable to install [miniconda.](https://docs.conda.io/en/latest/miniconda.html#linux-installers)

## Dependencies
Before launching the game or any file, some libraries will need to be previously installed.

### PyOpenGL
If you are on **Windows**, download [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl) the adecuate PyOpenGL version according to your PC specs and Python version. Then run the next command to complete installation:
```
pip install packagename.whl
pip install packagename_accelerate.whl

```

For example:

```
pip install PyOpenGL‑3.1.6‑cp38‑cp38‑win_amd64.whl
pip install PyOpenGL_accelerate‑3.1.6‑cp38‑cp38‑win_amd64.whl
```
For **Linux** users, you can follow [this](https://pypi.org/project/PyOpenGL/) guide.

### Mingus and Pygame
```
pip install mingus
pip install PyGame

```

### Fluidsynth
```
pip install PyFluidSynth

```
For **Windows** users, some versions of pyfluidsynth or the one included in the mingus library do not work correctly and give rise to some errors. 
I recommend following more precise instructions and downloading the most up-to-date portable version of Fluidsynth following this [guide.](https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html)

Although some warnings appear on the console whenever Fluidsynth instructions are executed, some of these traces can be solved in this [link.](https://github.com/nwhitehead/pyfluidsynth/issues/37)

### Sympy and Mpmath

```
pip install sympy
pip install mpmath

```
## How to Use
 
