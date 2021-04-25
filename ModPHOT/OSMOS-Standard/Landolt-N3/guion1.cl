#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# GUIÓN (SCRIPT) PARA OBTENER LAS MAGNITUDES EN EL SISTEMA ESTANDAR DE CAMPOS OSMOS DE LDN1588 PARA LA NOCHE N3.
# G. Pinzon, Técnicas Observacionales 2019-II. Módulo1. 05.10.19

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



# ejecutar digitando cl < guionN3.cl dentro del directorio fits que contiene las  imágenes a las cuales se les va a 
#extraer la fotometrñia:


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Archivos necesarios que deben estar en el directorio fits:
# Este archivo "guionN3.cl"
# imset
# config
# params

# Estos tres últimos fueron los que se obtuvieron durante la calibración de la noche 3 con los campos LANDOLT.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




# COMIENZO DEL GUION :
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




# Defino el directorio de trabajo en donde se encuentran las imágenes. (COLOQUE SU DIRECTORIO DE TRABAJO)

!cd /home/andres/Documentos/Documents/tecnicasobservacionales/ModPHOT/LDN1588/N3/S


# Borramos los siguientes archivo que contienen resultados previos, si el guion se ha ejecutado antes:
del science*
del *.coord
del *.lis
del totalcoord
del tmp*
#del PdumpOuT

# Ejecutamos el guion que usa sky2xy de wcstools y el catálogo 2mass (2m) para encontrar cuales de este catálogo aparecen en la imágen.
!./skyxy.sh

# Se generan archivos de coordenadas (extensión coord)

# Al final de este archivo se encuentra el programa sky2xy.sh




# Generamos las listas de archivos fits y  de coordenadas


!ls *.fits > fits.lis

!ls *coord > fits-coord.lis

# Y también genero un archivo con todas las coordenadas de todas las estrellas del catálogo 2MASS en la imágen. Esto
# es útil para obtener luego los nombres de las estrellas del catálogo ( photcal.mknobsfile )

!cat *coord > totalcoord


# Borramos cualquier resultado previo de magnitudes.
del *mag.1

#Configurar la tarea phot de APPHOT
#noao.digi.APPHOT

#configurar tareas datapars, photpars, fitskypars, centerpars previamente:
#consultar manual camara
# http://www.astronomy.ohio-state.edu/~martini/osmos/

#epar datapars

#fwhmpsf 4
#sigma 3
#readnoi 3.8
#epadu 1
#exposur EXPTIME
#airmass AIRMASS
#filter FILTID2
#obstime TIME-OBS

#epar centerpars
#calgori centroid
#cbox 8
#cthresh 0
#minsnra 1
#cmaxite 10


#epar fitskypars

#epar phot

#image @n3fits.lis
#coords @n3coord.lis
#datapar datapars
#centerp centerpars
#fitskyp fitskypars
#photpar photpars


# Calculamos las magnitudes instrumentales
phot @fits.lis coords=@fits-coord.lis  sigma=3.0 readnoi=5.0 epadu=2.3  fwhmpsf=4 itime=1 xairmas=1  annulus=10 dannulu=5 apertur=15 interac=no

#pdump  lo configuramos con salida XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR:

#apphot> lpar pdump
#      infiles = "*.mag.1"       Input apphot/daophot databases(s)
#       fields = "XINIT,YINIT,IFILTER,OTIME,XAIRMASS,XCENTER,YCENTER,MAG,MERR" Fields to be extracted
#         expr = "yes"           Boolean expression
#     (headers = no)             Print field headers?
#  (parameters = yes)            Print parameters?
#      (inlist = "")             
#        (mode = "ql")    


#Mayor información help phot

#calculo de la magnigud instrumental :

# flux = sum - area * msky
#         mag = zmag - 2.5 * log10 (flux) + 2.5 * log10 (itime)
#        merr = 1.0857 * err / flux
#         err = sqrt (flux / epadu + area * stdev**2 + area**2 * stdev**2 / nsky)
# flags de los errores
#           No error
#101       The centering box is off image
#102       The centering box is partially off the image
#103       The S/N ratio is low in the centering box
#104       There are two few points for a good fit
#105       The x or y center fit is singular
#106       The x or y center fit did not converge
#107       The x or y center shift is greater than maxshift
#108       There is bad data in the centering box



noao

apphot

pdump > aper15.data
