
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



# Borramos los siguientes archivo que contienen resultados previos, si el guion se ha ejecutado antes:
del science*
del *.coord
del *.lis
del totalcoord
del tmp*
del PdumpOuT

# Ejecutamos el guion que usa sky2xy de wcstools y el catálogo 2mass (2m) para encontrar cuales de este catálogo aparecen en la imágen.
!./sky2xy.sh

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
phot @fits.lis coords=@fits-coord.lis  sigma=3.0 readnoi=5.0 epadu=2.3  fwhmpsf=4 itime=1 xairmas=1  annulus=10 dannulu=5 apertur=12 interac=no

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

pdump > PdumpOuT

#juntamos la salida de pdump con el archivo de coordenadas de todas las estrellas del catálogo del 2MASS.
# Esta salida es el archivo file3

!awk '{f1 = $0; getline < "PdumpOuT"; print f1, $0}' < totalcoord  > file3


#Ahora vamos a pasar de magnitudes instrumentales a absolutas:
noao

photcal


# Hacemos una lista de los archivos mag.1 (magnitudes instrumentales)
!ls *.mag.1 > mag.lis

#Construimos el archivo de las observaciones. (imset de LAndoltN3 debe estar en el directorio fits )
# Generamos un archivo tmp que carece de los nombres de catalogo.

mknobsfile @mag.lis idfilter="V, R, I" imsets=imset observat=tmp

#Con el fin de incluir correctamente los nombres de las estrellas de catálogo :

!cat file3 | awk '{print $11,$12,$8,$5,$13, $14,$3, $4}' > file4
!cat tmp | awk '{print $5,$0}' > scienceobs1
!awk 'NR==FNR { n[$1]=$0;next } ($1 in n) { print n[$1],$5,$6,$1,$2 }' file4 scienceobs1 > final
!cat final | awk '{print $4, $3, 2011.,$9,$1,$2, $5, $6}' > scienceobsFINAL

!cp scienceobsFINAL tmp
!sed -i '/INDEF/s/INDEF/99999/' tmp
!sed -i '/INDEF/s/INDEF/99999/' tmp

!sed '/R/s/[0-9.]*/*/'  tmp > tmp1

!sed -i '/R/s/*/*       /' tmp1

!sed '/I/s/[0-9.]*/*/'  tmp1 > tmp2

!sed -i '/I/s/*/*       /' tmp2


!sed -i '/R/s/*/*       /' tmp2
!sed -i '/I/s/*/*       /' tmp2
!sed -i '/V/s/V/       V/' tmp2

!sed -i -e '1i# FIELD         FILTER           OTIME AIRMASS  XCENTER   YCENTER     MAG   MERR  \'  tmp2


!sed -i '/99999/s/99999/INDEF/' tmp2

!sed -i '/99999/s/99999/INDEF/' tmp2


!mv tmp2 scienceobsN3L

#El archivo scienceobsN3 tiene esta estructura :

# FIELD         FILTER           OTIME AIRMASS  XCENTER   YCENTER     MAG   MERR  
#05212345        V 2011 1.108 1814.402 88.629 INDEF INDEF
#*               R 2011 1.101 1815.185 85.845 23.922 1.309
#*               I 2011 1.096 1812.932 82.387 23.166 0.770
#05212440        V 2011 1.108 1784.526 40.658 18.436 0.007
#*               R 2011 1.101 1785.374 39.554 17.684 0.006
#*               I 2011 1.096 1785.844 39.088 18.010 0.008
#05212068        V 2011 1.108 1893.738 115.253 22.775 0.525
#*               R 2011 1.101 1893.537 121.776 22.511 0.495
#*               I 2011 1.096 1887.516 118.383 24.809 4.529
#05212528        V 2011 1.108 1760.579 20.912 16.616 0.002
#*               R 2011 1.101 1761.456 19.819 15.777 0.002
#*               I 2011 1.096 1761.915 19.321 16.040 0.002
#05212169        V 2011 1.108 1857.928 108.631 20.104 0.029
#*               R 2011 1.101 1858.801 107.520 19.313 0.023
#*               I 2011 1.096 1859.150 107.112 19.523 0.029
#05211558        V 2011 1.108 2024.036 58.902 INDEF INDEF
#*               R 2011 1.101 2019.913 57.463 INDEF INDEF
#*               I 2011 1.096 2026.380 62.111 INDEF INDEF
#05212009        V 2011 1.108 1897.758 51.598 25.179 26.750
#*               R 2011 1.101 1902.637 47.579 INDEF INDEF
#*               I 2011 1.096 1901.408 46.625 21.012 0.579



#Ahora invertimos las ecuaciones usando photcal.inverfit


#photcal> lpar invertfit
# observations = "scienceobsN3"    List of observations files
#       config = "config"        Configuration file
#   parameters = "params"        Fitted parameters file
#        calib = "sciencecalibN3"  Output calibrated standard indices file
#    (catalogs = "")             List of standard catalog files
#      (errors = "obserrors")    Error computation type (undefined,obserrors,equations)
#     (objects = "all")          Objects to be fit (all,program,standards)
#       (print = "")             Optional list of variables to print
#      (format = "")             Optional output format string
#      (append = no)             Append output to an existing file ?
#      (catdir = )_.catdir)      The standard star catalog directory
#        (mode = "ql")           


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# FIN DEL GUION :




#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%






# G. Pinzon - Tecnicas Observacionales - 2021


