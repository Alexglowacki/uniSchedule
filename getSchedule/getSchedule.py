import requests
import re


class getSchedule:
    def __init__(this):
        this.url = "https://it.pk.edu.pl/page/rz"
        this.file_url = "download/35c09905cc4086500ebada31a2213f1c/26012024_24_INFORMATYKA zima rozklad NIESTACJONARNE 2023_2024.xls"

    def getScheduleWebsite():
        print("DEBUG: Getting the schedule file")
        url = "https://it.pk.edu.pl"

        get_file = "https://it.pk.edu.pl/page/rz"
        r = requests.get(get_file, allow_redirects=True)
        open('Website.txt', "wb").write(r.content)
        
        line_list = []
        with open('Website.txt', "r") as file:
            for line in file:
                if ("Informatyka I stopie" and "NIESTACJONARNE") in line:
                    line_list.append(line)

            download_regex = r'\.\./.*?\.xls'
            match = re.findall(download_regex, line_list[1])
            match = match[0].replace("../", "")

        get_file = f"{url}/{match}"
        r = requests.get(get_file, allow_redirects=True)
        open('Schedule.xls', "wb").write(r.content)


if __name__ == "__main__":
    getSchedule.getScheduleWebsite()
