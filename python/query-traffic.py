import sys
from datetime import datetime
from traffic.data import opensky

def main():

    format="%Y-%m-%d %H:%M"

    start = datetime.utcfromtimestamp(int(sys.argv[1])).strftime(format)
    end = datetime.utcfromtimestamp(int(sys.argv[1]) + 1800).strftime(format)

    res = opensky.history(
        start=start,
        stop=end,
        bounds=[-74.0807, 40.626, -73.9007, 40.806] # lon/lat, lon/lat
    )

    print(f'\n {start} df size: {len(res.data)}')

if __name__ == "__main__":
    main()
