import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import FixedTarget
from astroplan import Observer
from astroplan import EclipsingSystem
from pytz import timezone

# Our target is an explante in HAT-P-32, a G or F-type dwarf star
# 860 light years away with an apparent magnitude of 11.197
HATP32 = FixedTarget.from_name('HAT-P-32')

# I used the data from the desert museum, which is close
# close to our observation site. I average temp and humidity
# measures for observation months.
latitude = '+32d14m38.45s'
longitude = '-111d10m5.43s'
elevation = 867.2962 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name='BB/RH Tucson',
                location=location,
                pressure=0.91 * u.bar,
                relative_humidity=0.25,
                temperature=20.0 * u.deg_C,
                timezone=timezone('US/Mountain'),
                description="Betsy Burr and Robert Henderson observation station in Tucson, AZ."
                )

print(HATP32)
print(observer)
