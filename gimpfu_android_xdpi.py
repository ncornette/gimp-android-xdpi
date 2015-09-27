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
DEFAULT_FOLDER_PREFIX = 'drawable'

UPSCALE_WARN_MESSAGE = '\nQuality of your application could be seriously affected when using upscaled bitmaps !'

def write_xdpi(img, layer, res_folder, folder_prefix, image_basename, target_width, x_ldpi, x_mdpi, x_hdpi, x_xhdpi, x_xxhdpi, x_xxxhdpi, allow_upscale, image_extension):
    '''
    Resize and write images for all android density folders 
    
    @param img: gimp image
    @param layer: gimp layer (or drawable)
    @param res_folder: output directory : basically res folder of your android project 
    @param folder_prefix: android mipmap or drawable folder
    @param image_basename: basename of your image, ex: icon
    @param target_width: new width for your image
    @param target_dpi: reference density for your target width
    @param allow_upscale: whether to create upscaled images
    @param image_extension: output format
    '''
    
    warnings = list()
    
    gimpfu.pdb.gimp_edit_copy_visible(img); #@UndefinedVariable
    
    dpi_ratios = (('ldpi',    0.75 ,x_ldpi),
                  ('mdpi',    1    ,x_mdpi),
                  ('tvdpi',   1.33 ,False),
                  ('hdpi',    1.5  ,x_hdpi),
                  ('xhdpi',   2    ,x_xhdpi),
                  ('xxhdpi',  3    ,x_xxhdpi),
                  ('xxxhdpi', 4    ,x_xxxhdpi))

    for folder, ratio, export in dpi_ratios:
        if not export: 
            continue

        new_img = gimpfu.pdb.gimp_edit_paste_as_new(); #@UndefinedVariable
        
        resize_ratio = float(target_width) / new_img.width
        target_dp_width = target_width
        target_dp_height = round(new_img.height * resize_ratio)
        
        # Compute new dimensions for the image
        new_width = target_dp_width * ratio
        new_height = target_dp_height * ratio
        
        print('%s : %dx%d' % (folder, new_width, new_height))
        
        if (new_width>new_img.width):
            if not allow_upscale:
                warnings.append('Not creating resource for %s upscaled by %0.2f' %
                            (folder, new_width/new_img.width))
                continue
            else:
                warnings.append('Resource for %s has been upscaled by %0.2f' %
                            (folder, new_width/new_img.width))

        target_res_folder = os.path.join(res_folder, folder_prefix + '-' + folder)
        if (os.path.exists(res_folder) and not os.path.exists(target_res_folder)):
            os.makedirs(target_res_folder)

        target_res_filename = os.path.join(target_res_folder, image_basename + '.' + image_extension)
        
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
                    (gimpfu.PF_RADIO, "folder-prefix", "Android Folder Prefix", DEFAULT_FOLDER_PREFIX, (("drawable", "drawable"), ("mipmap", "mipmap"))),
                    (gimpfu.PF_STRING, "image-basename", "Image Base Name", 'icon'),
                    (gimpfu.PF_SPINNER, "target-width", "Target DP Width", 48, (1, 8000, 2)),
                    (gimpfu.PF_BOOL, "x_ldpi",    "  Export ldpi",   False),
                    (gimpfu.PF_BOOL, "x_mdpi",    "  Export mdpi",   True),
                    (gimpfu.PF_BOOL, "x_hdpi",    "  Export hdpi",   True),
                    (gimpfu.PF_BOOL, "x_xhdpi",   "  Export xhdpi",  True),
                    (gimpfu.PF_BOOL, "x_xxhdpi",  "  Export xxhdpi", True),
                    (gimpfu.PF_BOOL, "x_xxxhdpi", "  Export xxxhdpi",False),
                    #(gimpfu.PF_BOOL, "x_tvdpi",   "  Export tvdpi",  False),
                    (gimpfu.PF_BOOL, "allow_upscale", "  Create upscaled images", False),
                    (gimpfu.PF_RADIO, "image-extension", "Image Format", DEFAULT_OUTPUT_EXT, (("gif", "gif"), ("png", "png"), ("jpg", "jpg"))),
                      ], 
                [], 
                write_xdpi) #, menu, domain, on_query, on_run)

gimpfu.main()
