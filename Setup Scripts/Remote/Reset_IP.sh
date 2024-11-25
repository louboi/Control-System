#-----------------------------------------------------PRE-EVENT SET-UP-----------------------------------------------------
# Update and upgrade everything before moving on
sudo apt update && sudo apt upgrade -y

#-----------------------------------------------------GPIO-----------------------------------------------------
# Get the user to input the IP address of the controlling system
echo "Please input the IP address of the controlling computer:"
read IP
echo "If you need to correct the IP address then just re-run the Reset_IP.sh script"

# enable and start the pigpoio service on system start-up
sudo systemctl reload pigpio -n $IP
