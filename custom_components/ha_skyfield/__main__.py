import datetime

from ha_skyfield.bodies import Sky

seattle = (47.608, -122.335)
pacific = "America/Los_Angeles"
sky = Sky(seattle, pacific)
sky.load()
when = datetime.datetime.now()
sky.plot_sky(when=when)

# timelapse

# when =datetime.datetime.now()
# interval = datetime.timedelta(minutes=30)
#
# for frame in range(72*2):
#    print(f"plotting frame {frame}")
#    sky.plot_sky(f'sun_{frame:03d}.png', when=when+interval*frame)
