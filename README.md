## README ##

Wrote some quick logic to scrape a web page (currently Unsplash) using xPath format to find all useful (ie. high quality) images,
pick a random one, save/update locally and set as my current desktop background.

### GETTING STARTED ###
1. Ensure you have a Python environment setup on your machine.
2. Create an image file in your "Desktop Images" folder called `RandomizedImage.jpg` (this name can be changed in `config.json`).
3. Install `virtualenv` and activate it in this project's root by running `virtualenv desktop-randomize/bin/activate`.
4. Run `./main.py` to update Desktop image.

### NOTES ###
Currently, Unsplash's "new" page is used to scrape random images. This can be changed to point to another site, but then all image
config props (ie. `image_*`) in `config.json` must be updated for the script to scrape appropriately. Also, if Unsplash ever decides
to modify their markup then the `image_xpath_logic` config prop will need to be updated, too.

This repo was built with OS X only support in mind. It wouldn't take much to support Windows (ie. change "Desktop Images" folder path),
but it wasn't necessary for me at the time of implementation.
