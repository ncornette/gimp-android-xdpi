gimp-android-xdpi
=================

Gimp plugin to write images for all android densities. 
A basic use of this plugin is to write icon files for your app directly from your full size picture, 
you just have to run the plugin with this parameters :
 1. select your app res folder
 2. type `icon` as the image base name
 3. select a image width of `48`
 4. select a density of `mdpi`

Icon resources for all densities will be scaled and written accordingly.
You will be warned if an image has been upscaled

### Installation: 
* Put this file into your gimp plugin directory, ie: ~/.gimp-2.6/plug-ins/gimpfu_android_xdpi.py
* Restart Gimp
* Run script via Filters/Android/Write Android XDPIs...
