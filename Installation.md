


### Option 1: Install using Package Control within Sublime Text

First, if you have not already done so, install Package Control for Sublime Text.

Then bring up the command pallette and press `Ctrl+Shift+P` (or `Cmd+Shift+P`) to bring up the command pallet.
Start typing "package control: install package", and select the option from the list.
Start typing "TextToSpeech" when the next window pops up, and select the entry from the list.
Close and restart Sublime Text.

Test that TextToSpeech works:
Select some text.
Press `Ctrl+Shift+P` to bring up the command pallet.
Type **`TTS: Speak`** and select the entry from the list.
You should now hear the selected text being spoken.




### Option 2: Download and place in Sublime Text packages folder

**OBS: The methods described here requires you to manually install the required dependencies for Sublime Text.
This is neither easy nor straight-forward.
If you are using Package Control, the required packages will be automatically installed.
Using Package Control is therefore recommended.

The required dependencies are:

* **pyttsx3**
* **pywin32**

To install these dependencies, go to your "Packages" directory, and type:

```
git clone https://github.com/packagecontrol/sublime-pywin32.git python-pywin32
git clone https://github.com/scholer/pyttsx3-st-dependency.git pyttsx3
```

Then you need to manually create a `dependency-metadata.json` file for both of the dependency packages above,
so that Package Control will recognize them and load them during startup.

Finally, we need to tell Package Control to load the above dependency packages
by editing the file `0_package_control_loader.sublime-package`.

> Once the package is extracted, a custom-generated python file is added to a special package named
> 0_package_control_loader. For Sublime Text 3, this is a .sublime-package file, whereas for Sublime Text 2
> it is just a folder. The reason for the name (and creating it as a .sublime-package file in ST3) is to
> ensure it is the very first non-default package that Sublime Text loads.

Alternatively, to make a dependency package available, open the console in Sublime Text and type:

```
import package_control
package_control.sys_path.add_dependency('pyttsx3')
```

However, note that Package Control may delete any dependency packages if they are not listed
as required by other packages.


Edit: We can also allegedly place a `.sublime-dependency` file in the root of the dependency package,
c.f. https://forum.sublimetext.com/t/general-method-to-add-a-pypi-package-as-st-dependency/34081


Edit: Just download required dependencies to another folder, not the Packages/ folder,
and then inside Sublime Text console, type:
```
import sys; sys.path.insert(0, r"C:\Users\au206270\Dev\sublime-text-dev\temp\pyttsx3\all")
```
Notice the `/all` at the end. (Or use `st3`, `st3_windows`, etc.)




Refs, dependencies:

* https://github.com/SublimeText/Pywin32
* https://github.com/packagecontrol/sublime-pywin32
* https://forum.sublimetext.com/t/general-method-to-add-a-pypi-package-as-st-dependency/34081



#### Option 2a: Just download zipped code

1. Go to https://github.com/scholer/TextToSpeech.
2. Press the "Clone or Download" button, then click "Download ZIP".
	Your browser should download a zip file for you.
3. Unzip the zip file.
4. Open Sublime Text, and select "Preferences → Browse Packages…".
	This will bring up Windows File Explorer (or Finder, or Dolphin).
5. Move the contents of the zip file to the folder containing your Sublime Text packages.
	OBS: The files should be placed together, and be located inside their own
	folder named "TextToSpeech".
6. Close and restart Sublime Text.




#### Option 2b: Download using Git

1. Open Sublime Text, and select "Preferences → Browse Packages…".
	This will bring up Windows File Explorer (or Finder, or Dolphin).
	* On Windows: In the address bar, type `cmd` and wait for a command prompt to pop up.
		(doing it this way just guarantees that you are in the correct directory).
2. In the terminal, type:
	**`git clone git@github.com:scholer/TextToSpeech.git`**.
3. Close and restart Sublime Text.


#### Option 2c: Download and symlink

1. Download package source code:
	a. Option A: Use git. Open a terminal, `cd` to the directory where you would like to clone the
		`TextToSpeech` git repository to (e.g. `cd C:\Users\username\Dev\sublime-text-dev`),
		then type **`git clone git@github.com:scholer/TextToSpeech.git`**.
2. Open Sublime Text, and select "Preferences → Browse Packages…".
	This will bring up Windows File Explorer (or Finder, or Dolphin).
	* On Windows: In the address bar, type `cmd` and wait for a command prompt to pop up.
		(doing it this way just guarantees that you are in the correct directory).
3. Create symbolic link:
	* On Windows, in the new command prompt, type:
		`mklink /D TextToSpeech "C:\Users\username\Dev\sublime-text-dev\TextToSpeech"`
		`mklink /D TextToSpeech "C:\Users\au206270\Dev\sublime-text-dev\TextToSpeech"`

