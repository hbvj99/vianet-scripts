# vianet-scripts
A collection of automation python scripts for Vianet Communication. You can automatize speed test and issue tickets, change IP, reboot router or view user's bandwidth details in terminal.

Here's the sample service ticket automatically created for high latency;
![Untitled](https://user-images.githubusercontent.com/43197293/79756223-085ee500-833a-11ea-946c-3c73abcfd266.png)


## How it works?
- Automates browser to collect required info
- Fetch raw data and display in CLI

## Requirements
- Python 3.x
- Selenium 3.x
- [Speedtest-cli](https://github.com/sivel/speedtest-cli)
- Google Chrome/Chromium

It requires Vianet (PPPoE credentials) and Raisecom ISCOM HT803-1GE EPON Home Terminal username/ password to get authorization. 

## How to run?
- Add login credentials ```credentials.py```
- Execute ```internet_details.py``` to get ```user ID```, ```Bandwidth usages```, ```Next billing```, ```FUP staus```
- Get new public IP ```router_change_ip.py```
- Test Internet and issue ticket using speedtest-cli ```test_speed_create_ticket_speedtest-cli.py``
- Test Internet and issue ticket using selenium ```test_speed_create_ticket_selenium.py``` (doesn't require [Speedtest-cli](https://github.com/sivel/speedtest-cli))
- Reboot router ```router_reboot.py```

> Change IP, reboot router only works with Raisecom ISCOM HT803-1GE EPON Home Terminal

## Contributions and about project
You can modify the content, optimize the code as you may like. You can credit me by mentioning this repository if you wish. Pull requests are welcomed.

**Disclaimer:** I will not be repsonsible if you issue huge amount of service tickets or sending large amount of traffic to the server. These are some of the simple scripts I wrote for learning and quick information access. 
