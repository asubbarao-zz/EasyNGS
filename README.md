README

Please view as "raw" in github or save as .txt for proper formatting

This is the README of the EasyNGS Project. This project provides a GUI and scripts which analyze NGS data files. The
program requires a design file, MPileup file, and SAM file.
Modules in this program include:
  -EasyNGS_with_UI.py
  -EasyNGS_input_module.py
  -EasyNGS_output_module.py
  -EasyNGS_results.py
  
Required files to run this program include:
  -design_file.csv
  -EasyNGS_Mpileup.csv
  -EasyNGS_Sam.csv
  
Libraries imported by this program include: 
  -re (regex)
  -doctest
  -Pandas
  -Numpy
  -wx
  -sys
  -collections
  -matplotlib.pyplot and matplotlib.patches
  
INSTRUCTIONS
In order to run this program, place all files into the current Python working directory, unzipped. 
You may open all files, but open and run EasyNGS_output_module.py. A GUI will appear with three buttons:
"Design File", "Mpileup", and "SAM". 

Click on the Design File button and a dialog box will appear. Type 'design_file.csv'  (or the name of your design file with .csv extension) 
without quotes and press OK. A dialog box will pop up stating "OK!"  when the file is successfully read. 
Do the same for both the Mpileup and SAM buttons, entering filename without quotes.
Once all three files have successfully loaded, click the "Close" or "X" button in the top right of the dialog box.

At this point, a graph of the depth should appear and all information has been loaded into the console. 
A file in your working directory title 'output.csv'



AUTHORS AND LICENSE
Copyright and licensing information: this project is open-source and has been created to help the world of NGS
analysis. Please feel free to use this code for scientific, academic, or any other non-commercial purposes. 

The authors of this project are:
  -Kiranmayee Dhavala (kiranmayee.dhavala@gmail.com)
  -Renu Jayakrishnan (renukrishna21@gmail.com)
  -Alok Subbarao (aloksubbarao@gmail.com
  -Harjot Hans (harjokong@gmail.com)
  -Jeffrey Byrnes (jrbyrnes1989@gmail.com)
  
Any bugs, glitches, feature requests, etc should be sent to the authors listed above re: EasyNGS
The GitHub respository for this project can be found at: https://github.com/sjsumbt/Python_Project/
