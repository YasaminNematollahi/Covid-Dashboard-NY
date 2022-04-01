# Covid-Dashboard-NY
#### It is a project that aims to visualize the covid dataset.

1. Instal **Conda** on your computer, you can install **Anaconda** or **Miniconda** for that.

   <ins>Conda</ins> is a language-agnostic tool for package management and environment management. 

   <ins>Anaconda</ins> is the most popular Python distribution. <ins>By installing Anaconda, you get Miniconda, Anaconda Navigator (i.e. a graphical user interface) and curated selection of packages installed</ins>.

   <ins>Miniconda</ins> is a mini-scale version of Anaconda. It is also a Python distribution. <ins>By installing Miniconda, you get Conda, Python and a small number of packages installed</ins>.

   **As we can see, Conda is included in both Anaconda and Miniconda.** 

2. Create the virtual environment:

   - Open the command-line interface for your operating system with the following instructions:

         - Windows: Press windows key ➡️ Type Anaconda prompt ➡️ Press enter
         - Mac: Press cmd + space bar ➡️ Type Terminal ➡️ Press enter
   
   - Create the environment by using commands
      ```
      $ conda create -n CovidNY python=3.8 -y
      $ conda activate CovidNY
      ```

3. Install all the requirements, run the line:
```
 python -m pip install -r requirements.txt
```
