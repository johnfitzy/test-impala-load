import sys
from pyopensky import OpenskyImpalaWrapper
from datetime import datetime


def main():

    format="%Y-%m-%d %H:%M:%S"

    start = datetime.utcfromtimestamp(int(sys.argv[1])).strftime(format)
    end = datetime.utcfromtimestamp(int(sys.argv[1]) + 1800).strftime(format)

    opensky = OpenskyImpalaWrapper()

    res = opensky.query(
        type="adsb",
        start=start,
        end=end,
        bound=[40.626, -74.0807, 40.806, -73.9007] # lat/lon, lat/lon
    )

    print(f'\n {start} df size: {len(res)}')

if __name__ == "__main__":
    main()