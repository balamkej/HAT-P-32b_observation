import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import FixedTarget
from astroplan import Observer
from pytz import timezone


HATP32 = FixedTarget.from_name('HAT-P-32')

latitude = '+32d14m38.45s'
longitude = '-111d10m5.43s'
elevation = 867.2962 * u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

# I used the data from the desert museum.
observer = Observer(name='BB/RH Tucson',
                location=location,
                pressure=0.91 * u.bar,
                relative_humidity=0.25,
                temperature=80.0 * u.deg_C,
                timezone=timezone('US/Mountain'),
                description="Betsy Burr and Robert Henderson observation station in Tucson, AZ."
                )

#print(location)
#print(observer)
