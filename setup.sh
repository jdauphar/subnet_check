# install fping to ping the whole range
# sudo apt install fping

# initial run
sudo python3 check.py

#write out current crontab
sudo crontab -l > crons
#echo new cron into cron file
sudo echo "0 0 * * 6 python3 $PWD/handle_log.py" >> crons
#install new cron file
sudo crontab crons
sudo rm crons
