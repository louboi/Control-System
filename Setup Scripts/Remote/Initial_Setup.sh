#-----------------------------------------------------PRE-EVENT SET-UP-----------------------------------------------------
# Update and upgrade everything before moving on
sudo apt update && sudo apt upgrade -y

#-----------------------------------------------------GPIO-----------------------------------------------------
# Get the user to input the IP address of the controlling system
echo "Please input the IP address of the controlling computer:"
read IP
echo "If you need to correct the IP address then just run the Reset_IP.sh script"

# Get the user to change the config
echo "Please enable remote GPIO either through the setting panel or by running sudo raspi-config"

# Install the pigpio library for use in python
sudo apt install pigpio

# enable and start the pigpoio service on system start-up
sudo systemctl enable pigpio -n $IP

# Reboot to finish
echo "rebooting in 5 seconds"
sudo reboot