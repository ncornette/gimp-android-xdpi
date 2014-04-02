gimp-android-xdpi
=================

Gimp plugin to export images or icons for all android densities.

### Usage

 - Select the area to export, 
 - Run the plugin from Filters -> Android -> Write Android XDPIs...  
 - Images will be written to your drawable-ldpi / mdpi / hdpi / xhdpi folders with appropriate size.
 - You can select the target width for the corresponding density so you don't have to resize your picture.


### Installation

 - Download the script [gimpfu_android_xdpi.py](https://github.com/ncornette/gimp-android-xdpi/raw/master/gimpfu_android_xdpi.py), save into your gimp plugin directory, ie: `~/.gimp-2.6/plug-ins/gimpfu_android_xdpi.py`
 - Restart Gimp
 - Run script via Filters/Android/Write Android XDPIs...

### Example

To write you app icon directly from you full size picture, select area for your icon : 


[![icon selection](https://lh5.googleusercontent.com/9ovI_ry3awmPs0tWjt2b08c5ykQxwFz7GQgltRxs3BOV5LREYr4pWPrMNunrZDeP5zCqig1kjiUmnd5-CmXzCNk_oKPTRC5i_qpbZBI_cazA29VC4dw)](https://lh5.googleusercontent.com/9ovI_ry3awmPs0tWjt2b08c5ykQxwFz7GQgltRxs3BOV5LREYr4pWPrMNunrZDeP5zCqig1kjiUmnd5-CmXzCNk_oKPTRC5i_qpbZBI_cazA29VC4dw)  

Use the reference values for an app icon, 48px on mdpi : 

![icon parameters](https://github.com/ncornette/gimp-android-xdpi/raw/master/screenshot.png)


 1. select your app res folder
 2. type `icon` as the image base name
 3. select a image width of `48`
 4. select a densities to export
 5. select image format `png`

Icon or Image resources for all densities will be scaled and written accordingly.
You will be warned if an image has been upscaled

[![export result](https://lh6.googleusercontent.com/LT7vn7uo2jmjul4ejuu59iM4elDto1TsjagX1Zp5wdgzPghQ_TBsUKGOF65y7m6XwW2DaTpJlxS2GxU9Xi3jklrxj2bR8c6d8blc6dgi8Iwnri56SlM)](https://lh6.googleusercontent.com/LT7vn7uo2jmjul4ejuu59iM4elDto1TsjagX1Zp5wdgzPghQ_TBsUKGOF65y7m6XwW2DaTpJlxS2GxU9Xi3jklrxj2bR8c6d8blc6dgi8Iwnri56SlM)

