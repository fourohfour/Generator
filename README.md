# Generator
Takes a csv file and turns it into a list matching the template you give it.

The first row of the CSV file contains your field headers.

Every row below that is your data - each line is a record and a new item.

In template.txt is the template that you want your result to match. The START value is inserted at the start of the output, a MODULE is added for each record in your CSV and the END value is added, unsurprisingly, at the end of the file.

The MODULE can contain placeholders in the form of {FIELDNAME} which will be replaced by the corresponding value for each record.

You should put your data.csv and template.csv in a subfolder of the script directory. Then, you can replace the datalocation variable in your python file with the path to this folder. This means that you will not be prompted for the path each time you run the program.

The result will be put in output.txt, in the same folder as data.csv and template.csv.
