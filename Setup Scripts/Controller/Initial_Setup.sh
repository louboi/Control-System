#-----------------------------------------------------PRE-EVENT SET-UP-----------------------------------------------------
# Update and upgrade everything before moving on
sudo apt update && sudo apt upgrade -y

#-----------------------------------------------------GPIO-----------------------------------------------------
# Install GPIO Zero and the pgpio library
sudo apt install python3-gpiozero python3-pigpio

# Reboot to finish
echo "rebooting in 5 seconds"
sudo reboot