import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import FixedTarget
from astroplan import Observer
from astroplan import EclipsingSystem
from pytz import timezone

# Our target is an explanet in HAT-P-32, a G or F-type dwarf star
# 860 light years away with an apparent magnitude of 11.197
# at 02h04m10.28s +46d41m16.2s
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
                description='Betsy Burr and Robert Henderson observation
                station in Tucson, AZ.'
                )

# Orbital data from explanetarchive.ipac.caltec.edu
primary_eclipse_time = Time(2454942.898400, format='jd') 
orbital_period = 2.150009 * u.day
eclipse_duration = 3.1102 * u.day

HATP32b = EclipsingSystem(primary_eclipse_time=primary_eclipse_time,
                orbital_period=orbital_period,
                duration=eclipse_duration,
                name='HAT-P-32b'
                )

n.transits = 169 # The number of transits per year
obs_time = Time('2017-08-01 12:00')

print(HATP32)
print(observer)
