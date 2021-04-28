#!/bin/bash
# -*- ENCODING: UTF-8 -*-
# autor: Andres Guerrero

#this scrip removes all lines whose magnitude result is 'INDEF'.
#-------------------------------------------------------------------------
# this script must be located in the directory where the magnitude results
 #are located
#-------------------------------------------------------------------------
#parameters
#path: path of the magnitude results

path=`pwd`

for data in "$path"/*.data
    do
    
    sed -i '/INDEF/d' "$data"
    
    done
