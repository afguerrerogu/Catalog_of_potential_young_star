# Calatog of potential young star
Construction of a catalog of potential young star in the lamda orionis region
--

in the 'catalog_match' directory there are two catalogs that we will use to find the stars that are in the images .FIT


code
--
sky2xy.sh\\
this script is for making a mach between the stars in the images with the 2mass and landold catalog, it uses the sky2xy library of wcstools 

tophot.sh\\
this script rewrites the first two lines of the .coord file to the new .coo file. this is needed to do the photometry in IRAF
