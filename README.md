# Control-System

This is a fully customisable control-system for managing door access.

## Authors

- [@louboi](https://github.com/louboi)

## Demo

Insert gif or link to demo

## Prerequisites:

### Control Node:
- Any system able to run linux
    - I Used a Raspberry Pi 4B
- Debian
    - I use raspberry pi OS lite 64 bit- Based on Debian 12
- Sudo Privilages
- Python
    - I used 3.13
- Bash
- An internet connection (or way of transfering files to the system) for installation
- A connection to the Remote nodes via a network switch or router (For the deployment)

### Remote Node:
- Any system able to run linux
    - I Used a Raspberry Pi 2B
- Debian
    - I use raspberry pi OS lite 32 bit- Based on Debian 12
- Sudo Privilages
- Python
    - I used 3.13
- Bash
- An internet connection (or way of transfering files to the system) for installation
- A connection to the Remote nodes via a network switch or router (For the deployment)

## Installation
### Part 1 - Pre-Event set up
Download the project files
```bash
  git clone https://github.com/louboi/Control-System.git
```
### Part 2 - Set up the remote Pi
#### Part 2.1
Copy the remote scripts to your remote Pi using whatever method you want.
```bash
  Control-System/Setup Scripts/Remote
```
#### Part 2.2
Run the script by navigating to the folder the scripts sit in and typing:
```bash
  sudo chmod +x Initial_Setup.sh
  sudo ./Initial_Setup.sh
```
### Part 3 - Set up the controling Pi
#### Part 3.1
Copy the Controller scripts to your controling Pi using whatever method you want.
```bash
  Control-System/Setup Scripts/Controller
```
#### Part 3.2
Run the script by navigating to the folder the scripts sit in and typing:
```bash
  sudo chmod +x Initial_Setup.sh
  sudo ./Initial_Setup.sh
```
### Part 4 - Running the Main Program
```bash
  git clone https://github.com/louboi/Control-System.git
```
### Part 5
```bash
  git clone https://github.com/louboi/Control-System.git
```
  
## Roadmap

- Additional browser support

- Add more integrations
