---
description: 'Default arguments, Recursion, PIP, Terminal'
---

# Extensions

## Default Arguments

If we want a function to use a default value for a parameter, we can use = when defining the functions parameters list:

```python
def greet_user(greeting="Hi", name):
    print(greeting +" " name + ", nice to meet you!")
```

## Recursion

Recursion is a fun and occasionally useful concept. It refers to the ability to have functions **call themselves**

```python
# A recursive function calls itself

# This function will count down to zero
def count_down(number):
    print(number)
    if (number > 0): # Recurse until we reach zero
        count_down(number - 1) # "Recursive" call!
    
count_down(3) # Will print 3 2 1 0
```

## PIP

You'll often find that the package you want to use is not installed alongside python by default. But if it's popular, then chances are you'll be able to add it using python's package manager, **pip** \(pip = "pip installs packages"\).

pip can be used via the command line / terminal

Installing the numpy package on Windows:![pip](http://localhost:8888/notebooks/week7/pip_windows.png)

and on Linux/Mac:![pip](http://localhost:8888/notebooks/week7/pip_install.png)

## Using the terminal  

Much professional programming is done on Linux or mac, both of which are based on UNIX. Windows users can install the UNIX subsystem with fairly little effort \(I recommend looking at [https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10\)](https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10%29).

"pip install" is an example of a terminal command, but there are many more. Amongst these, the most commonly used are those which allow you to move around inside your PCs directories:

* **ls** lists the files and folders in your current directory, and **ls -a** includes additional information
  * Here -a is an example of an additional parameter. Many commands have these, and you can typically find out about the possible parameters/usage of a command by using the --help tag. For example, "ls --help"
* **cd** short for change directory allows you to move between folders
  * e.g. "cd my\_folder\* moves you into the folder my\_folder, if it exists in the current directory
* **pwd** prints the working directory, so you know where you are in the filesystem
* **mkdir** creates a directory. E.g. "mkdir fish" creates a folder named "fish" in your current directory
* **less** allows you to view the contents of a file without opening it. You can exit this using the "q" key.
  * e.g. if there's a "test.txt" file, you can use "less.txt" to directly view its contents in the terminal window
* **rm** removes stuff - **be careful with this**. The **-r** parameter removes recursively, allowing you to delete folders and their contents
  * e.g. "rm -r my\_folder" deletes the folder "my\_folder"
  * "sudo rm -rf /\*" deletes everything on your pc! :D \(the -f parameter forces deletion of protected files\)

