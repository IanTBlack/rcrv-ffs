# RCRV Flowthrough Filtration System

This repository contains Python 3 modules and scripts for driving a three-way valve using a Raspberry Pi Waveshare Relay Hat.

## Operating System
Raspberry Pi OS (Debian Bullseye)

## Installation
First you will need to clone this repo to your user folder on your Raspberry Pi. In the past, the default user for the Raspberry Pi Operating system has been "pi",
but the release of Raspberry Pi OS Bullseye allows for custom users from the start. The setup and operation of the FFS takes this into account and is user agnostic.

To clone the repo...
```
cd ~
git clone https://github.com/R-DESC/rcrv-ffs.git
``` 

To add the Python modules to Path...

1. Open your user .bashrc with `sudo nano ~/.bashrc`.
2. At the end of the file, add `export PYTHONPATH=/home/$USER/rcrv-ffs`.
3. Write out the file with `Ctrl + O`
4. Exit the file with `Ctrl + X`
5. Reset with `source ~/.bashrc`.


## Usage

### Running the Filtered Seawater
The run_fsw.py script accepts three parameters. 
1. The number of minutes to run filtered seawater through the system.
2. The IP address you want UDP messages sent to.
3. The port you want UDP messages sent to.

This script simply turns the valve to the filtered position and waits for X number minutes before turning it off again.

At the command line you can enter

### Checking Valve Status
A separate script must be run in order to check the status of the valve. The state of the pins on the Raspberry Pi are 
check once per second to estimate the state of the valve. If not that confirmation that the valve has switch will need to be observed manually or within optical data.


## Running with Cron
The valve must be run with a cron job. To edit cron, enter `crontab -e` in your terminal.
To run hourly, on the hour, you would need to add this line to the bottom of your crontab. Where $USER is your active user.

```0 */1 * * * PYTHONPATH=/home/$USER/rcrv-ffs python3 /home/$USER/rcrv-ffs/operation/run_fsw.py 10 ip-address-here ip-port-here```

To set up the Pi to check the valve all of the time, the easiest method is to deploy the check_valve_state script to run
at reboot.

```@reboot PYTHONPATH=/home/$USER/rcrv-ffs python3 /home/$USER/rcrv-ffs/operation/check_valve_state.py```

Write out the changes with `Ctrl+O` and exit with `Ctrl+X`.

## Visual Cues
All relays off.
![Off](https://github.com/R-DESC/rcrv-ffs/blob/main/docs/relays_disabled.jpg)

Relay one on.
![On](https://github.com/R-DESC/rcrv-ffs/blob/main/docs/relay_one_enabled.jpg)

## Testing
`pytest` is used to run tests on the relay/valve.

To run tests...
1. Open a terminal window.
2. `cd /home/$USER/rcrv-ffs/ffs/tests`
3. `pytest`

## Caveats
Both Python logging and cron run on system time. It is recommended that you switch system time to UTC, otherwise your log output will
rotate to a new log at whatever time midnight is for the assigned timezone.

Note that there are no protections built in against the amount of time that you use as a command line argument interfering with crontab.
For example, if you set the valve to run filtered for 90 minutes every hour on the hour, your valve
would first run for 90 minutes, and then from then on every 30 minutes would turn off the filtered water.

