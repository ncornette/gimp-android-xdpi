gimp-android-xdpi
=================

Gimp plugin to write images for all android densities

### Actions: 
1. You can select the target width and the target density.
2. Visible Selection is exported into these res folders : 
	* res/drawable-ldpi 
	* res/drawable-mdpi 
	* res/drawable-hdpi 
	* res/drawable-xhdpi 
3. Drawables for all densities are scaled accordingly

### Installation: 
* Put this file into your gimp plugin directory, ie: ~/.gimp-2.6/plug-ins/gimpfu_android_xdpi.py
* Restart Gimp
* Run script via Filters/Android/Write Android XDPIs...
