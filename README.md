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

Standard_magnitude (author : G. pinzon).\
This script will be used to obtain the magnitude of the stars in the standard system of the OSMOS field of LDN1588.

guion2.cl\
this script calculates the magnitudes in the science stars. run it in IRAF as: \
> cl < guion2.cl 


config_file
--
in this directory there is configuration file, catalog, theoretical file

standobs: is the standard star observation file, characterization of night 3  

aperture study
--
guion1.cl (author : G. pinzon).\
This script will be used to obtain the magnitude of the stars in the standard system of the OSMOS field of LDN1588.
before executing the script it is necessary to change the parameters in IRAF. these changes are specified as follows.
we are going to do an aperture study so, we are going to change the aperture parameter (in line 97) from 8 to 15. In the last line we have to change the name of the output file for each aperture   
Executing this file in IRAF whit >: cl < guion1.cl

configure IRAF
--

Configurar la tarea phot de APPHOT\
noao.digi.APPHOT\
Configurar la tarea phot de APPHOT\
noao.digi.APPHOT\

configurar tareas datapars, photpars, fitskypars, centerpars previamente:\
consultar manual camara\
 http://www.astronomy.ohio-state.edu/~martini/osmos/ \

**epar datapars**\

fwhmpsf 4\
sigma 3\
readnoi 3.8\
epadu 1 \
exposur EXPTIME\
airmass AIRMASS\
filter FILTID2\
obstime TIME-OBS\

**epar centerpars**

calgori centroid\
cbox 8\
cthresh 0\
minsnra 1\
cmaxite 10\

**epar fitskypars**\

**epar phot**\

image @n3fits.lis\
coords @n3coord.lis\
datapar datapars\
centerp centerpars\
fitskyp fitskypars\
photpar photpars\

pdump  lo configuramos con salida XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR:

**apphot> lpar pdump**\
        infiles = "*.mag.1"       Input apphot/daophot databases(s)\
       fields = "XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR" Fields to be extracted\
         expr = "yes"           Boolean expression\
     (headers = no)             Print field headers?\
  (parameters = yes)            Print parameters?\
      (inlist = "")             \
        (mode = "ql")    \


Mayor información help phot\

**calculo de la magnigud instrumental :**\

 flux = sum - area * msky\
         mag = zmag - 2.5 * log10 (flux) + 2.5 * log10 (itime)\
        merr = 1.0857 * err / flux\
         err = sqrt (flux / epadu + area * stdev**2 + area**2 * stdev**2 /\ nsky)\
 flags de los errores\
           No error\
101       The centering box is off image\
102       The centering box is partially off the image\
103       The S/N ratio is low in the centering box\
104       There are two few points for a good fit\
105       The x or y center fit is singular\
106       The x or y center fit did not converge\
107       The x or y center shift is greater than maxshift\
108       There is bad data in the centering box\


characterize night 3
--
PACKAGE = photcal\
   TASK = fitparams\
    
observat=             standobs  List of observations files\
catalogs=         nlandolt.dat  List of standard catalog files\
config  =               config  Configuration file\
paramete=               params  Output parameters file\
(weighti=              uniform) Weighting type (uniform,photometric,equations)\
(addscat=                  yes) Add a scatter term to the weights ?\
(toleran=   3.0000000000000E-5) Fit convergence tolerance\
(maxiter=                   15) Maximum number of fit iterations\
(nreject=                    2) Number of rejection iterations\
(low_rej=                   3.) Low sigma rejection factor\
(high_re=                   3.) High sigma rejection factor\
(grow   =                   0.) Rejection growing radius\
(interac=                  yes) Solve fit interactively ?\
(logfile=               STDOUT) Output log file\
(log_unm=                  yes) Log any unmatched stars ?\
(log_fit=                   no) Log the fit parameters and statistics ?\

after digit :go

magnitude of the scientific stars
--

Once we have the characterization of night 3 with the optimal aperture of the data, we are going to obtain the magnitudes of the scientific stars, for this we are going to execute in IRAF: > cl < script2.cl, we must modify this file with the optimal aperture for these stars. but before, we must make the imset file with IRAF, as follows: 

> epar mkimset

PACKAGE = photcal\
   TASK = mkimsets\

imlist  =              *.mag.1  The input image list\
idfilter=                V,R,I  The list of filter ids\
imsets  =                imset  The output image set file\
(imobspa=                  obs) The output image observing parameters file\
(input  =            photfiles) The source of the input image list\
(filter =              filtid2) The filter keyword\
(fields =                     ) Additional image list fields\
(sort   =                     ) The image list field to be sorted on\
(edit   =                  yes) Edit the input image list before grouping\
(rename =                  yes) Prompt the user for image set names\
(review =                  yes) Review the image set file with the editor\
(list   =                     )\
(mode   =                   ql)\

:go

NOTE: when doing epar mkimset on science stars L, you have a problem, you must remove tow medias for each filter.

and you have to save the files with :wq. and then you have an imset file and obs

now, we execute in IRAF:
> cl < guion2.cl

we have the scienceobsN3S file, this file has the magnitude of the stars.
we must run the imvertfit task to invert the magnitudes, this uses the params file we did before.

> epar invertfit

PACKAGE = photcal\
   TASK = invertfit\

observat=        scienceobsN3S  List of observations files\
config  =               config  Configuration file\
paramete=               params  Fitted parameters file\
calib   =      sciencecalibN3S  Output calibrated standard indices file\
(catalog=                     ) List of standard catalog files\
(errors =            obserrors) Error computation type (undefined,obserrors,equa\
(objects=                  all) Objects to be fit (all,program,standards)\
(print  =                     ) Optional list of variables to print\
(format =                     ) Optional output format string\
(append =                   no) Append output to an existing file ?\
(catdir =            )_.catdir) The standard star catalog directory\
(mode   =                   ql)\

:go

and then, in the terminal, execute:

> sed -i "1,19d" sciencecalibN3S \
> sed -i '/INDEF/d' sciencecalibN3S\
> sed -i '1i #ID V err_V V-R err_V-R V-I err_V-I' sciencecalibN3S\ 

Finally, we have the file sciencecalibN3S, this file contains the magnitudes of the science stars on night 3 short.
we must do the same for the science stars of night 3 large.
we will move these files to a new directory for the analysis

Analysis
--
in the Analysis directory should be the files sciencecalibN3, and the theoretical files zamsvr. let's analyze this with.
> analysis.py
1. first let's read the files
 2. define the constants:
- extinction coefficient
- distance
3. calculate the absolute magnitudes 
4. We make the figures 
5. eliminate the measurements whose error is greater than 0.5
6. using the error diagram we define which magnitude we are going to use for the short and large exposure 
7.Finally, we join the two catalogs and export them in a .csv file. 



> young_stars.py\


1.we first construct the third-degree polynomial approximations for the theoretical curve\
2.we calculate the differences on the y-axis between the points and the polynomial\
3.tomamos solo los puntos en que las diferencias sean mayores a 0\
4.export the catalog to a .csv file\




