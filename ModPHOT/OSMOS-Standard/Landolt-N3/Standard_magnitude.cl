
del science*
del *.coord
del *.lis
del totalcoord
del tmp*

!./sky2xy.sh

!ls *.fits > fits.lis

!ls *coord > fits-coord.lis

!cat *coord > totalcoord

del *mag.1

# Calculamos las magnitudes instrumentales
phot @fits.lis coords=@fits-coord.lis  sigma=3.0 readnoi=5.0 epadu=2.3  fwhmpsf=4 itime=1 xairmas=1  annulus=10 dannulu=5 apertur=12 interac=no


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

pdump > magnitude_aper12.data
