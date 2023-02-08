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

### yawnoc.py

To launch the game of life you must run yawnoc at the anaconda prompt, there are several game modes available:

 - **Casual Mode (0)**: No additional sound associated with each game state will be played, this is traditional Conway game of life.
 
 - **Melodic Piano (1)**: Each state of the game will play a specific musical note within two octaves through a classical piano.
 
 - **Armonic Piano (2)**: Each state of the game will play a root state triad chord belonging to a specific major or minor key through a classical piano.
 
 - **Rhytmic Drums (3)**: Each state of the game will play a sound produced by a Roland TR 808 drums set, including bassDrum, snare, hihat, tum, or the silence itself.
 
 - **Melodic Violin (4)**: Each state of the game will play a specific musical note within two octaves through a classical piano.
 
 - **Melodic Bass (5)**: Each state of the game will play a specific musical note within two octaves through a TEK bass.
 
 
 
 The dimensions of the window and the board of the game of life must be indicated as a parameter in the following way:

```
python yawnoc.py [musical Approach] [window's Dimension] [universe's Dimension]
```
where:

-   [musical Approach] is the game mode chosen from those mentioned above.
-   [window's Dimension] is the dimensions in pixels that the window will have. For the time being, the X and the Y axis will have the same value, therefore creating a square window.
-   [universe's Dimension] is the amount of cells that the univere will contain on each side of the grid.

For instance, if you want to run the Game of Life in melodicPiano mode, on a  800×800  window and a  100×100  grid you should run:

```
python yawnoc.py 1 800 100
```


This program includes the following key and mouse commands to control and manage the game:

-   Left click: when clicking a cell you reverse its state from dead to alive and vice versa.

-   "C" key: performs a clear action,changing the state of all cells to dead .
-   "R" key: performs a random action, changing the states of all cells to a random one.
-   "Space" key: performs a blizzard action, turning dynamic mode on or off. In dynamic mode, the states are constantly updated, while in static mode actions can be carried out with more precision.

-   ⬆  key: speeds up the rate at which the next game state is updated.
-   ⬇  key: decelerates the rate at which the next game state is updated.
-   ➡  key: if the game is in static mode the cellular automaton will evolve to its following state.
