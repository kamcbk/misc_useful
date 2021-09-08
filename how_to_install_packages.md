# How to install packages

#### Author: Kevin Marroquin

## Preface:

This is an overview on how to install packages within a system (primarily a linux system). I often times struggled early on with dealing with packages unaware of where to store them and how to set them onto a path on command line. Here is a brief tutorial on how to write packages into your system and onto your path.

## Installing Files:

Packages in Linux will often contain packages in the form of gz, zip, etc. Whenever you decompress it, you should get a folder with subfolders named *bin*, *lib*, and other materials (occasionally a *src* or *conf* folder). *bin/[program]* will launch the program, the usual desired result.

In terms of where to store it all these packages, I recommend this entire folder should be placed in */usr/local/*. For example;

`
cd /usr/local
sudo tar xzf <the file you just downloaded>
`

With the second line opening the file and installing it in said directory. One may choose to move the folder itself if desired.

## Assigning Path

In order for your system to understand and communicate with your program, one neeeds to open their *.bashrc* script (or alternative start up script) and add the following lines, with Java being an example:

`
export JAVA_HOME=/usr/local/jdk-17
export PATH=$PATH:$JAVA_HOME/bin
`

Assuming you have a standard path set up, this will tell your system to look into the JAVA home, which we've designated as /usr/local/jdk-17. The PATH is set to look into this bin. *bin* is usually set to where programs are stored and run, and java is no exception. Hence, when typing 'java' on your terminal, your computer will run java from this *bin* folder.

Another example to illustrate this working:

`
export PYTHONPATH=/usr/local/anaconda3/
export PATH=$PATH:$PYTHONPATH/bin
`

Of course, there is nothing wrong with adding the strict path.

`
export PATH="/usr/local/anaconda3/bin:$PATH"
`

The `$PATH:` or `:$PATH` is needed to reassign PATH to itself plus the addition to whatever you included, with the above example being python.

## Conclusion:

Hopefully this helps guide one through this often unguided process, primarily my future self. Any misspellings, please contact to correct.
