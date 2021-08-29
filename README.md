# Script description :

Browse all the category pages from http://books.toscrape.com/index.html to extract the following :  
-Product page url  
-Universal product code (upc)  
-Title  
-Price including tax  
-Price excluding tax  
-Number available  
-Product description  
-Category  
-Review rating  
-Image url  
and download the associated cover image.



# Script Installation (Example of Python 3) :


Extract the repository's files in a folder of your choosing

### Setup the virtual environment :


In your command bash/shell go in the folder containing the files

Type :  
Windows :
```
py -m venv venv
```
Unix/mac :
```
python3 -m venv venv
```


You then need to activate the virtual environment :  
Windows :
```
.\venv\Scripts\activate
```
Unix/mac :  
```
source venv/bin/activate
```
(venv) should now be displayed to the left of your command line :
```
(venv) C:\>
```

### Install the libraries required to run the script :

In the virtual environment (command bash/shell) type : 
```
pip(3) install -r requirements.txt
```



You can now run the script :  
Windows
```
C:\Folder\containing\py\files\projet-2.py

```
Unix/mac
```
python3 projet-2.py
```