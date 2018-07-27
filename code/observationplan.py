import astropy.units as u
import datetime as dt
from astropy.time import Time
from astropy.time import TimezoneInfo
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astroplan import FixedTarget
from astroplan import Observer
from astroplan import EclipsingSystem
from astroplan import is_event_observable
from astroplan import PrimaryEclipseConstraint
from astroplan import AtNightConstraint
from astroplan import AltitudeConstraint
from astroplan import TimeConstraint
from pytz import timezone

# Download updated bulletin table
from astroplan import download_IERS_A
# download_IERS_A()

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
                description='Betsy Burr and Robert Henderson observation station in Tucson, AZ.'
                )

# Orbital data from explanetarchive.ipac.caltec.edu
primary_eclipse_time = Time(2454942.898400, format='jd') 
orbital_period = 2.150009 * u.day
eclipse_duration = 3.1102 * u.hour

HATP32b = EclipsingSystem(primary_eclipse_time=primary_eclipse_time,
                orbital_period=orbital_period,
                duration=eclipse_duration,
                name='HAT-P-32b'
                )

n_transits = 169 # The number of transits per year
observing_time = Time('2018-08-01 12:00')


utc_minus_six_hour = TimezoneInfo(utc_offset=-6*u.hour)

constraints = [AtNightConstraint.twilight_astronomical(),
                AltitudeConstraint(min=30*u.deg),
                ]

ing_egr = HATP32b.next_primary_ingress_egress_time(observing_time, n_eclipses=n_transits)

hits = is_event_observable(constraints, observer, HATP32, times_ingress_egress=ing_egr)

# Create a list of ingress-egress time objects matching constraints.
candidates = []
for i in range(len(hits[0])):
    if hits[0][i] == True:
        candidates.append(ing_egr[i])

# Convert from Julian to ISO
for i in candidates:
    i.format = 'iso'

f = open('observation_times.txt', 'w')
f.write("Obervation times [Ingress Egress] --- UTC (MST is UTC - 6)\n")
for i in candidates:
    f.write("%s\n" % i.value)
f.close()
