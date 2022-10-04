########################
#   AUTHOR: Tr4shL0rd  #
# CREATION: 10/4/2022  #
########################
"""module for getting data from a speedtest.net CSV file"""
import os.path 
from dataclasses import dataclass
from sys import argv
import csv
from rich.table import Table
from rich.console import Console
console = Console()

@dataclass
class Desktop:
    """
        represents the data gotten from the web speedtest csv file
    """
    platform:str
    file:str
    ping = []
    down = []
    up   = []
@dataclass
class Web:
    """
        represents the data gotten from the desktop speedtest csv file
    """
    platform:str
    file:str
    ping = []
    down = []
    up   = []

def data_reader(plat:object) -> tuple[float,float,float]: 
    """
        reads the data from csv file gotten from speedtest
    """
    with open(plat.file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        if plat.platform == "Desktop":
            for row in reader:
                plat.ping.append(round(float(row[2]),2))
                plat.down.append(round(float(row[3]),2))
                plat.up.append(round(float(row[4]),2))
        elif plat.platform == "Web":
            for row in reader:
                plat.ping.append(round(float(row[5]),2) )
                plat.down.append(round(float(row[3]),2) )
                plat.up.append(round(float(row[4]),2) )
    return (plat.ping,plat.down, plat.up)
def get_dates(plat:object) -> list:
    """
        parses the dates from the files
    """
    with open(plat.file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        monthNumbers = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        dates = []
        for row in reader:
            if row[1].split("/")[0].isalpha():
                    dates.append(f"{monthNumbers[row[1].split('/')[0]]}/{row[1].split('/')[1]}/{row[1].split('/')[2].split(' ')[0]}")
            else:
                dates.append(row[1].split(" ")[0])
    return dates
def main(verbose:bool=False):
    desk = Desktop(file=os.path.join("csv_files", "speedtest_Desktop.csv"), platform="Desktop")
    web = Web(file=os.path.join("csv_files", "speedtest_Web.csv"), platform="Web")
    web_ping,  web_down,  web_up = data_reader(web)
    desk_ping, desk_down, desk_up = data_reader(desk)

    web_max_ping,web_min_ping = max(web_ping),min(web_ping)
    web_max_down,web_min_down = max(web_down),min(web_down)
    web_max_up,web_min_up     = max(web_up),  min(web_up)

    desk_max_ping,desk_min_ping = max(desk_ping),min(desk_ping)
    desk_max_down,desk_min_down = max(desk_down),min(desk_down)
    desk_max_up,desk_min_up     = max(desk_up),  min(desk_up)

    web_avg_down = round(sum(web_down)/len(web_down),2)
    web_avg_up   = round(sum(web_up)/len(web_up),2)
    web_avg_ping = round(sum(web_ping)/len(web_ping),2)

    desk_avg_down = round(sum(desk_down)/len(desk_down),2)
    desk_avg_up   = round(sum(desk_up)/len(desk_up),2)
    desk_avg_ping = round(sum(desk_ping)/len(desk_ping),2)

    table_title = "AVERAGE INTERNET SPEEDS"
    table = Table(title=table_title if not verbose else table_title + "(verbose)", show_lines=True)
    table.add_column("PLATFORM")
    if verbose: table.add_column("DATE RANGE")
    table.add_column("AVG DOWN(Mbps)")
    table.add_column("AVG UP(Mbps)")
    table.add_column("AVG PING(ms)")
    if verbose:
        table.add_column("MIN DOWN(Mbps)")
        table.add_column("MAX DOWN(Mbps)")

        table.add_column("MIN UP(Mbps)")
        table.add_column("MAX UP(Mbps)")

        table.add_column("MIN PING(ms)")
        table.add_column("MAX PING(ms)")

    if verbose:
        table.add_row(
                        "DESKTOP",
                        f"{get_dates(desk)[-1]} - {get_dates(desk)[0]}",
                        f"{str(desk_avg_down)}",
                        f"{str(desk_avg_up)}",
                        f"{str(desk_avg_ping)}",
                        str(desk_min_down),
                        str(desk_max_down),
                        str(desk_min_up),
                        str(desk_max_up),
                        str(desk_min_ping),
                        str(desk_max_ping),
                    )
    else:
        table.add_row(
                        "DESKTOP",
                        f"{str(desk_avg_down)}",
                        f"{str(desk_avg_up)}",
                        f"{str(desk_avg_ping)}"
                    )
    if verbose:            
        table.add_row(
                        "WEB",
                        f"{get_dates(web)[-1]} - {get_dates(web)[0]}",
                        f"{str(web_avg_down)}",
                        f"{str(web_avg_up)}",
                        f"{str(web_avg_ping)}",
                        str(web_min_down),
                        str(web_max_down),
                        str(web_min_up),
                        str(web_max_up),
                        str(web_min_ping),
                        str(web_max_ping),
                    )
    else:
        table.add_row(
                        "WEB",
                        f"{str(web_avg_down)}",
                        f"{str(web_avg_up)}",
                        f"{str(web_avg_ping)}",
                    )
            
    console.print(table)
if __name__ == "__main__":
    try:
        if argv[1].lower() == "-v":
            verbose = True
        elif argv[1].lower() == "-h":
            print("""python speedtest_results.py [FLAGS]
                        \r\t-v: returns verbose data
                        \r\t-h: displays this help message

                        \rCreated By @Tr4shL0rd""")
            exit()
    except IndexError:
        verbose = False
    main(verbose)