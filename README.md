# Calatog of potential young star
Construction of a catalog of potential young star in the lamda orionis region
--

in the 'catalog_match' directory there are two catalogs that we will use to find the stars that are in the images .FIT


code
--
sky2xy.sh\
this script is for making a mach between the stars in the images with the 2mass and landold catalog, it uses the sky2xy library of wcstools 

tophot.sh\
this script rewrites the first two lines of the .coord file to the new .coo file. this is needed to do the photometry in IRAF

guion1.cl (author : G. pinzon).\
This script will be used to obtain the magnitude of the stars in the standard system of the OSMOS field of LDN1588.



# aperture study
guion1.cl (author : G. pinzon).\
This script will be used to obtain the magnitude of the stars in the standard system of the OSMOS field of LDN1588.
before executing the script it is necessary to change the parameters in IRAF. these changes are specified in the guion1.cl
we are going to do an aperture study so, we are going to change the aperture parameter (in line 97) from 8 to 15  
