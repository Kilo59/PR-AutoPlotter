# Microplate reader Assistant
##Python-Google Spreadsheet-R Data pipeline

Despite limitations Excel remains one of the most widely used application for data analysis in many fields. This software uses a combination of spreadsheets, Python and procedurally generated R code to filter, analyze and visualize data from a Micro-plate reader machine.

###Still in ALPHA
If you run into an error while executing please contact me or create an issue.
Feedback is welcome.
###Documentation: WIP

##What is this?
A platform to automate the computation/analysis of data from a microplate reader.  

Allows for users with minimal to no knowledge of programming to import large raw csv datasets, automate computations, analysis, visualizations, add their own specialized computational functions (in R or Python). Users can access these results remotely minutes after the plate reader has finished taking it's final measurements.
Remotely accessible via Google Spreadsheets and plotly

Tested and Optimized for the BioscreenC 20 x 10 microplate reader

##Dependencies
* [gspread](https://github.com/burnash/gspread) | Google Spreadsheets Python API
* [oauth2client](https://github.com/google/oauth2client) | Python library for accessing resources protected by OAuth 2.0

###Index
* [Configuration Settings]
* [Installation]
 * [Scheduler]
 * [Spreadsheet]
 * [plotly]
* [Example]

##Configuration Settings
start_condition | Type | Meaning
--- | --- | ---
post2google | True/False | Determines whether or not the validated OD readings are posted to the google spreadsheet at the end of the Python script. If not needed or the readings have already been posted, set condition to False for significantly shorter run time.
input_filename | Text String | Program will look for a file of this name. Make sure the CSV filename matches this otherwise the program will exit prematurely.
run | True/False | Program will exit immediately unless True. After the main script has been executed completely without errors this will be changed to False to prevent the task/process scheduler from executing this script repeatedly. *Make sure this is set to True before leaving the Lab.

tolerance | Type | Meaning
--- | --- | ---
maxreq | Float | The maximum value for the well must exceed this number to pass validation
rangereq | Float | The range for the well must exceed this number to pass validation

####Default Tolerance settings are meant to exclude empty wells. Wells will pass the validation check if they meet either of these requirements. Make use of the Well Grouping feature to subset the data more narrowly.  

spread_sheet | Type | Meaning
---- | ---- | ----
sheet_name | Text String | gspread will accesses your google spreadsheet using this name. Make sure this matches the Spreadsheet you want to use, not the Worksheet title.

r_options | Type | Meaning
---- | ---- | ----
execute_r | True/False | Determines whether the program will execute the plot_data.R sub process.
gen_grping_file | True/False | Determines whether an Rscript will be generated based on the Well Groupings set in the Google Spreadsheet. If execute_r = Flase and gen_grping_file = True, the grouping.R script for creation of ggplots will be created but the ggplot images themselves will not be automatically created or posted to plotly.
post2plotly | True/False | If set to False the script for looping through the Data Groups and posting to your plotly account will still be generated but they will be commented out. To execute the loop at a later time remove the '#' and execute in R. To post results to plotly automatically post2ploty = True, the correct api key and username must be set and execute_r = True.
plotly_api_key | Text String | Replace with your plotly api key. Available with every plotly account. Not needed if post2plotly = false.
plotly_username | Text String | Replace with your plotly username. Not needed if post2plotly = false.

##Installation
* [Obtain OAuth2 credentials from Google Developers Console](http://gspread.readthedocs.io/en/latest/oauth2.html) (Steps 1-4)
* Setup Google Spreadsheet
* Download Zipfile
  * Place JSON authorization file in the same directory as main.py
  * Check config.ini preferences
    * Set google spreadsheet name
    * Set [plotly credentials (username and api key)](https://plot.ly/)
    * Set desired preferences, tolerances
* [Install & Add to PATH R](https://cran.r-project.org/mirrors.html)
* [Install & Add to PATH Python35](https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe)
  * Install python modules gspread & oauth2client

####To Install python modules on Windows:
1. Run commandprompt
2. python -m pip install gspread
3. python -m pip install oauth2client

####Setup Task Scheduler/Cron job (optional)

####Spreadsheet Setup
* [Copy Template](https://docs.google.com/spreadsheets/d/1iwIqJFmqjBiF7x14Bd4VQg8CFB-6jfWLCbYkezdn5Pw/edit?usp=sharing)
* Set config settings to match spreadsheet name
* Relabel Wells, Group Names and add items to Groups as needed
* Share the spreadsheet with the email from JSON authorization (pending fix to gspread to resolve issue)  
* REARRANGING WORKSHEET ORDER MAY RESULT IN ERROR

####Plotly Setup

##Example
An example CSV file has been provided in the 'examples' folder within 'auto_plotter'. To peform a test run; follow these steps after the initial setup.
* Move the 'raw_plate_reader.csv' to the same folder as the main script.
* Check the config settings and modify them where appropriate. Reccomending setting post2google = False for the first few runs.
* Run the main script from the command line or built in Python IDLE (recommended)
* Depending on your config settings and well label names and groups you should notice new ggplot.png files and a grouping.R file being created within the main 'auto_plotter' folder.

####Input data:
* BioscreenC derived .CSV file
* Well names
* Well groupings

![CSVexample](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/csv.png)

![labelEx](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/labelEx1.PNG?raw=true)

![groupingEx](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/groupingEx1_sm.png?raw=true)

####Output:
 * Updated Google Spreadsheet
 * [Plotly ggplots](https://dashboards.ly/ua-3iqBAQDFa93xVVHraRB3Tm "Plotly Dashboard")
 * updated CSV file
 * dynamically generated R script
 * ggplot png files

![Updated Google Spreadsheet](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/well_dataEx1.PNG?raw=true)

![PlotlyEx](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/plotlyEx1.PNG?raw=true)

![RscriptEx](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/groupingRex1.PNG?raw=true)

![local_fileEx](https://github.com/kilo59/data-alpha-Guilf/blob/alpha_2/readme_images/local_filesEx1.PNG?raw=true)
