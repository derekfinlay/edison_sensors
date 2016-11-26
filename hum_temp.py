import mraa
import pyupm_th02
import thread, time
th02 = pyupm_th02.TH02(6,0x40)
print th02.name()
print th02
# <pyupm_th02.TH02; proxy of <Swig Object of type 'upm::TH02 *' at 0xb76a74a0> >
temp = th02.getTemperature()
print temp
th02.getStatus()
hygro = th02.getHumidity ()
print hygro
