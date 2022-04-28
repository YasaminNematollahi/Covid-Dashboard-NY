[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:fac487184e2093375cd9f306e8d02238b6f96b47/)](https://archive.softwareheritage.org/swh:1:dir:fac487184e2093375cd9f306e8d02238b6f96b47;origin=https://github.com/YasaminNematollahi/Covid-Dashboard-NY;visit=swh:1:snp:a4566ff7168f5b257f9e395459914f6e4d24bdba;anchor=swh:1:rev:e34aa7658b50df87b7997dd2cff0557b2eb93b38)

# Covid-Dashboard-NY
#### It is a project that aims to visualize the covid dataset. The dataset we are visualizing is available [here](https://github.com/owid/covid-19-data/tree/master/public/data).

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

## For running the dashboard locally, follow the steps below:
1. In Anaconda Navigator, open a terminal in your environment. You can open anaconda prompt from your search bar. In this case when the terminal opens, first you need to activate by writing: 
```
streamlit activate CovidNY
```

2. In the terminal that appears, write this code: 
```
streamlit run Dashboard.py
```
There you go. In your browser you can see the dashboard. Voila.

You can find the streamlit cloud [here](https://share.streamlit.io/yasaminnematollahi/covid-dashboard-ny/main/Dashboard.py).