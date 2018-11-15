import os
import platform


if __name__ == "__main__":

    path = os.path.dirname(os.path.realpath(__file__))

    if 'Windoes' not in platform.platform():
        import pandas as pd
        import readline
        from StationsCompleter import *

        stations = pd.read_csv(path + '/stations.csv').values
        completer = StationsCompleter(stations.T[0])
        readline.set_completer(completer.complete)
        readline.set_completer_delims('')
        readline.parse_and_bind('tab: complete')

    departure = input("\nStart Station:\t")
    arrival = input("\nEnd Station:\t")

    if 'Windoes' not in platform.platform():
        readline.parse_and_bind('set disable-completion on')

    print("specify date range: Format (yyyy-mm-dd)")
    from_date = input("Begin Date:\t")
    to_date = input("End Date:\t")

    #run command "python db_info.py -f "Oldenburg (Oldb) Hbf" -t München Hbf -fd 2018-11-11 -td 2018-11-20"
    
    command = "python "+ path +"/db_info.py -f \""+ departure + "\" -t \"" + arrival + "\" -fd " + from_date + " -td " + to_date

    os.system(command)
    print(command)
