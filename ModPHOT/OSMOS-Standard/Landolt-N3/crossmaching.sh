#!/bin/bash
# -*- ENCODING: UTF-8 -*-

#this script is for making a mach between the stars in the images with the 2mass catalog, it uses the sky2xy library of wcstools 
#-------------------------------------------------------------------------
#

path=`pwd`
path_sk2xy="/home/andres/Documentos/Documents/tecnicasobservacionales/wcstools-3.9.6/bin/"
path_catg="/home/andres/Documentos/Documents/tecnicasobservacionales/ModPHOT/ejecutable/catalogonlandolt"

num=${#path}
res=0
let caracter=$num-$res
echo "$caracter"

#ls $path

#echo "$path"
#echo "$path_catg"
#echo "$path_sk2xy"

for fits in "$path"/*.fits
    do

    "$path_sk2xy"./sky2xy -z "$fits" @"$path_catg" >> "$path"/"${fits:$caracter}".txt

    sed -i '/(off image)/d' "$path"/"${fits:$caracter}".txt
    sed -i '/(offscale)/d' "$path"/"${fits:$caracter}".txt


    cat "$path"/"${fits:$caracter}".txt | awk '{print $5, $6, $1,$2, $3}' > "$path"/"${fits:$caracter}".coord

    rm "$path"/"${fits:$caracter}".txt

    done


#/home/andres/Documentos/Documents/tecnicasobservacionales/Calatog_of_potential_young_star/ModPHOT/OSMOS-Standard/Landolt-N3/olt-N3/Fosmosn3.0051.ow.fits.txt:
#/home/andres/Documentos/Documents/tecnicasobservacionales/Calatog_of_potential_young_star/ModPHOT/OSMOS-Standard/Landolt-N3/lt-N3/Fosmosn3.0051.ow.fits.txt