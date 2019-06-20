# subnet_check
Takes a csv file of static IP leases from Infoblox, scans to find which are used/unused, installs cronjob to rescan each week

## dependencies
This requires an internet connection and fping, please install fping using your favorite package manager

## setup
Before you run the setup.sh script, please specify the name of your csv file and the absolute path to the directory containing this file.