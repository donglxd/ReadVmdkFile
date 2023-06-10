# ReadVmdkFile
Obtain the relationship between vmdk volumes through Python and draw a relationship diagram through Python

Installation and usage tutorial

0. Copy all vmdk volumes that need to be read separately to a new folder, copy the directory, and place them freely.

1. Extract Graphviz 0.7.2 (which can be downloaded from the Graphviz official website and is available on all three platforms, with the latest version being 0.8.2) from the Graphviz folder to your preferred directory, preferably without Chinese characters.

2. Right click on the desktop computer - Properties - Advanced System Settings - Environment Variables - Create a new variable in path and copy the bin directory of Graphviz into it (E: My Documents Desktop Python Development Graphviz bin)

3. Unzip ReadVMDKFile.rar (password 1234), run ReadVMDKFile.py (please install Python 3, the latest version is fine), and then paste the previous vmdk volume directory with the command line that pops up. Press Enter and wait for it to read. After a while, you will see an image showing the relationship between VMDKs.



 
