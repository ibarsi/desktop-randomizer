## README ##

Wrote some quick logic to scrape a web page (currently Unsplash) using xPath format to find all useful (ie. high quality) images,
pick a random one, save/update locally and set as my current desktop background.

### GETTING STARTED ###
1. Ensure you have a Python environment setup on your machine.
2. Run `pip install virtualenv`.
3. Create your virtualenv by running `virtualenv desktop-randomizer` (this path has been added to `.gitignore`).
4. Activate virtualenv by running `source desktop-randomizer/bin/activate`.
5. Install frozen dependencies by running `pip install -r requirements.txt`.
6. Create an image file in your "Desktop Images" folder called `RandomizedImage.jpg` (this name can be changed in `settings.py`).
7. Run `./main.py` to update Desktop image.

#### OPTIONAL ####
This script could be configured to run automatically to keep your desktop _extra_ fresh.

OS X (Launchd):

1. Remove the ".ex" at the end of `com.user-name.desktop-randomizer.plist.ex` and replace all instances of {{user-name}} with whatever you'd like (including in the file name).
2. Move file to `/Library/LaunchAgents`.
3. Ensure `<key>EnvironmentVariables</key>` and `<key>ProgramArguments</key>` paths are pointing to the correct folders on your machine.
4. Update the `<key>StartCalendarInterval</key>` node to set when you'd like to have the script run (currently its set to daily at
midnight).

### NOTES ###
Currently, Unsplash's "new" page is used to scrape random images. This can be changed to point to another site, but then all image
config props (ie. `IMAGE_*`) in `settings.py` must be updated for the script to scrape appropriately. Also, if Unsplash ever decides
to modify their markup then the `IMAGE_XPATH_LOGIC` config prop will need to be updated, too.

This repo was built with OS X only support in mind. It wouldn't take much to support Windows (ie. change "Desktop Images" folder path),
but it wasn't necessary for me at the time of implementation.
