# Covid-Dashboard-NY
It is a project that aims to visualize the covid dataset.
Instal **Conda** on your computer, you can install **Anaconda** or **Miniconda** for that.

Conda is a language-agnostic tool for package management and environment management. 

Anaconda is the most popular Python distribution. By installing Anaconda, you get Miniconda, Anaconda Navigator (i.e. a graphical user interface) and curated selection of packages installed.

Miniconda is a mini-scale version of Anaconda. It is also a Python distribution. By installing Miniconda, you get Conda, Python and a small number of packages installed.

**As we can see, Conda is included in both Anaconda and Miniconda.** 

Create the virtual environment:

- Open the command-line interface for your operating system with the following instructions:

   - Windows: Press windows key ➡️ Type Anaconda prompt ➡️ Press enter
   - Mac: Press cmd + space bar ➡️ Type Terminal ➡️ Press enter
   
 - Create the environment by using commands
    ```
    $ conda create -n CovidNY python=3.8 -y
    $ conda activate CovidNY
    ```

Install all the requirements, run the line:
```
 pip install -r requirements.txt
```
