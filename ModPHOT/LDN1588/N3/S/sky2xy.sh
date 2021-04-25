#!/bin/bash
# -*- ENCODING: UTF-8 -*-
# autor: Andres Guerrero

#this script is for making a mach between the stars in the images with the 2mass catalog, it uses the sky2xy library of wcstools 
#-------------------------------------------------------------------------
#this script is for making a mach between the stars in the images with the
# 2mass and landold catalog, it uses the sky2xy library of wcstools 
#-------------------------------------------------------------------------
# this script must be located in the directory where the photometric images
# to be compared with the 2mass catalog are located. 
#-------------------------------------------------------------------------
#parameters
#path: path of the photometric images 
#path_sk2xy: path of wsctools 
#path_catg : path of catalog for match
#res: characters to cut for the path. not always necessary.

path=`pwd`
path_sk2xy="/home/andres/Documentos/Documents/tecnicasobservacionales/wcstools-3.9.6/bin/"
path_catg="/home/andres/Documentos/Documents/tecnicasobservacionales/Catalog_of_potential_young_star/Catalog_match/2m"

num=${#path}
res=0
let caracter=$num-$res

for fits in "$path"/*.fits
    do

    "$path_sk2xy"./sky2xy -z "$fits" @"$path_catg" >> "$path"/"${fits:$caracter}".txt

    sed -i '/(off image)/d' "$path"/"${fits:$caracter}".txt
    sed -i '/(offscale)/d' "$path"/"${fits:$caracter}".txt


    cat "$path"/"${fits:$caracter}".txt | awk '{print $5, $6, $1,$2, $3}' > "$path"/"${fits:$caracter}".coord

    rm "$path"/"${fits:$caracter}".txt

    done
