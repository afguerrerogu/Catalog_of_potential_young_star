#!/bin/bash
# -*- ENCODING: UTF-8 -*-
# autor: Andres Guerrero

#this script rewrites the first two lines of the .coord file to the new .coo file
#this is needed to do the photometry in IRAF
#-------------------------------------------------------------------------
# this script must be located in the directory where the photometric images
# to be compared with the 2mass catalog are located. 
#-------------------------------------------------------------------------
#parameters
#path: path of the photometric images 
#res: characters to cut for the path. not always necessary.


path=`pwd`
num=${#path}
res=0
let caracter=$num-$res

for fits in "$path"/*.fits.coord
    do
        cat "$fits" | awk '{print $1, $2}' > "$fits".coo
    done

