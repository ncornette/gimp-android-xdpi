#! /usr/bin/env python
'''
Created on 2012/04/20

@author: nic

This is a Gimp plugin

Actions: 
    - Save Visible Selection to android drawables into 
        - res/drawable-ldpi 
        - res/drawable-mdpi 
        - res/drawable-hdpi 
        - res/drawable-xhdpi 
    - You can select a new width for the drawable and select the target density.
    - Drawables for other densities will be scaled accordingly

Installation: 
    - Put this file into your gimp plugin directory, ie: ~/.gimp-2.6/plug-ins/gimpfu_android_xdpi.py
    - Restart Gimp
    - Run script via Filters/Android/Write Android XDPIs...
'''

import gimpfu
import gimp
import os

DEFAULT_OUTPUT_DIR = os.getcwd()
DEFAULT_OUTPUT_EXT = 'png'

UPSCALE_WARN_MESSAGE = '\nQuality of your application could be seriously affected when using upscaled bitmaps !'

def write_xdpi(img, layer, res_folder, image_basename, target_width, x_ldpi, x_mdpi, x_hdpi, x_xhdpi, x_xxhdpi, x_xxxhdpi, image_extension):
    '''
    Resize and write images for all android density folders 
    
    @param img: gimp image
    @param layer: gimp layer (or drawable)
    @param res_folder: output directory : basically res folder of your android project 
    @param image_basename: basename of your image, ex: icon
    @param target_width: new width for your image
    @param target_dpi: reference density for your target width
    @param image_extension: output format
    '''
    
    warnings = list()
    
    gimpfu.pdb.gimp_edit_copy_visible(img); #@UndefinedVariable
    
    dpi_ratios = (('drawable-ldpi',    0.75 ,x_ldpi),
                  ('drawable-mdpi',    1    ,x_mdpi),
                  ('drawable-tvdpi',   1.33 ,False),
                  ('drawable-hdpi',    1.5  ,x_hdpi),
                  ('drawable-xhdpi',   2    ,x_xhdpi),
                  ('drawable-xxhdpi',  3    ,x_xxhdpi),
                  ('drawable-xxxhdpi', 4    ,x_xxxhdpi))

    for folder, ratio, export in dpi_ratios:
        if not export: 
            continue

        new_img = gimpfu.pdb.gimp_edit_paste_as_new(); #@UndefinedVariable
        
        resize_ratio = float(target_width) / new_img.width
        target_dp_width = target_width
        target_dp_height = round(new_img.height * resize_ratio)

        target_res_folder = os.path.join(res_folder, folder)
        if (os.path.exists(res_folder) and not os.path.exists(target_res_folder)):
            os.makedirs(target_res_folder)
            
        target_res_filename = os.path.join(target_res_folder, image_basename+'.'+image_extension)
        
        # Compute new dimensions for the image
        new_width = target_dp_width * ratio
        new_height = target_dp_height * ratio
        
        print('%s : %f' % (folder, ratio))
        
        if (new_width>new_img.width):
            warnings.append('Resource for %s has been upscaled by %0.2f' % 
                            (folder, new_width/new_img.width))
        
        # Save the new Image
        gimpfu.pdb.gimp_image_scale_full( #@UndefinedVariable
            new_img, new_width, new_height, gimpfu.INTERPOLATION_CUBIC)
        
        gimpfu.pdb.gimp_file_save( #@UndefinedVariable
            new_img, new_img.layers[0], target_res_filename, target_res_filename)
        
        gimpfu.pdb.gimp_image_delete(new_img) #@UndefinedVariable
        
    # Show warning message
    if warnings: 
        warnings.append(UPSCALE_WARN_MESSAGE)
        gimp.message('\n'.join(warnings))

gimpfu.register("python_fu_android_xdpi", 
                "Write Android drawables for all DPI folders", 
                "Write images for all android densities", 
                "Nic", "Nicolas CORNETTE", "2012", 
                "<Image>/Filters/Android/Write Android XDPIs...", 
                "*", [
                    (gimpfu.PF_DIRNAME, "res-folder",     "Project res Folder", DEFAULT_OUTPUT_DIR), #os.getcwd()),
                    (gimpfu.PF_STRING, "image-basename", "Image Base Name", 'icon'),
                    (gimpfu.PF_SPINNER, "target-width", "Target DP Width", 48, (1, 8000, 2)),
                    (gimpfu.PF_BOOL, "x_ldpi",    "  Export ldpi",   False),
                    (gimpfu.PF_BOOL, "x_mdpi",    "  Export mdpi",   True),
                    (gimpfu.PF_BOOL, "x_hdpi",    "  Export hdpi",   True),
                    (gimpfu.PF_BOOL, "x_xhdpi",   "  Export xhdpi",  True),
                    (gimpfu.PF_BOOL, "x_xxhdpi",  "  Export xxhdpi", False),
                    (gimpfu.PF_BOOL, "x_xxxhdpi", "  Export xxxhdpi",False),
                    #(gimpfu.PF_BOOL, "x_tvdpi",   "  Export tvdpi",  False),
                    (gimpfu.PF_RADIO, "image-extension", "Image Format", DEFAULT_OUTPUT_EXT, (("gif", "gif"), ("png", "png"), ("jpg", "jpg"))),
                      ], 
                [], 
                write_xdpi) #, menu, domain, on_query, on_run)

gimpfu.main()
