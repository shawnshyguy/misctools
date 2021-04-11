# Convenient File Relocator Tool Software Program Application
(CFRTSPA for short)

CFRTSPA (/kəˈfərtspə/) is a tool I wrote for putting many files from folder A into subfolders in folder B. For instance, imagine having a bunch of photos in your downloads folder, that you want to sort into "memes", "screenshots", etc in your photos library. You would just set the download and photo directories in the script, and choose where to move each image.


## Limitations
Currently, the way you choose the subfolder to move to is by typing it's index number. this number can be found by typing "help" when prompted for an index number, but is also just the position of the folder alphabetically, starting from 0.<br>
Additionally, the script was designed around, and currently only works on Windows. I'm sure its a quick fix (just some forwardslash-backslash conflict), and I'll get around to it eventually, but if you're using this now and it's not fixed yet, it shouldn't be a big deal to fix.

## To-do
- [x] ask user if they want to overwrite file, if file with existing filename already exists in destination
- [ ] add non-Windows support properly
- [ ] always/never overwrite, opposed to prompting every time
- [ ] option to (perhaps auto-) rename existing file when existing filename already exists
- [ ] perhaps a GUI, or at least some basic file previewing
