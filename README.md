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



aperture study
--
guion1.cl (author : G. pinzon).\
This script will be used to obtain the magnitude of the stars in the standard system of the OSMOS field of LDN1588.
before executing the script it is necessary to change the parameters in IRAF. these changes are specified as follows.
we are going to do an aperture study so, we are going to change the aperture parameter (in line 97) from 8 to 15. In the last line we have to change the name of the output file for each aperture   

# configure IRAF

Configurar la tarea phot de APPHOT
noao.digi.APPHOT
Configurar la tarea phot de APPHOT
noao.digi.APPHOT

configurar tareas datapars, photpars, fitskypars, centerpars previamente:
consultar manual camara
 http://www.astronomy.ohio-state.edu/~martini/osmos/

**epar datapars

fwhmpsf 4
sigma 3
readnoi 3.8
epadu 1
exposur EXPTIME
airmass AIRMASS
filter FILTID2
obstime TIME-OBS

**epar centerpars
calgori centroid
cbox 8
cthresh 0
minsnra 1
cmaxite 10

**epar fitskypars

**epar phot

image @n3fits.lis
coords @n3coord.lis
datapar datapars
centerp centerpars
fitskyp fitskypars
photpar photpars

pdump  lo configuramos con salida XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR:

**apphot> lpar pdump
        infiles = "*.mag.1"       Input apphot/daophot databases(s)
       fields = "XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR" Fields to be extracted
         expr = "yes"           Boolean expression
     (headers = no)             Print field headers?
  (parameters = yes)            Print parameters?
      (inlist = "")             
        (mode = "ql")    


Mayor información help phot

**calculo de la magnigud instrumental :

 flux = sum - area * msky
         mag = zmag - 2.5 * log10 (flux) + 2.5 * log10 (itime)
        merr = 1.0857 * err / flux
         err = sqrt (flux / epadu + area * stdev**2 + area**2 * stdev**2 / nsky)
 flags de los errores
           No error
101       The centering box is off image
102       The centering box is partially off the image
103       The S/N ratio is low in the centering box
104       There are two few points for a good fit
105       The x or y center fit is singular
106       The x or y center fit did not converge
107       The x or y center shift is greater than maxshift
108       There is bad data in the centering box



