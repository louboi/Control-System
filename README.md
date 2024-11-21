# Control-System

This is a fully customisable control-system for managing door access.

## Authors

- [@louboi](https://github.com/louboi)

## Demo

#### Example Database of users
![Database Example](https://github.com/user-attachments/assets/7c3aa356-296d-4569-a39f-295808284abe)


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
  
## Roadmap

- RFID Reader implementation
- Door lock release
- Led for feedback
- Numpad for back-up
- ~~Create UUID~~

## Appendix

- ASCII Table:
    - https://www.ascii-code.com/

## Error Code Reference

| Code  | Name     | Description                                         | Solution                                                  |
| :---- | :------- | :-------------------------------------------------- | :-------------------------------------------------------- |
| `001` | `Length` | `Username or Password is longer than 10 characters` | `Shorten the length of your Username or Password`         |
| `002` | `Entry`  | `Username or Password has not been entered`         | `Enter a Username and Password`                           |
| `003` | `Mod`    | `Modulo of UUID is not a number`                    | `Try clearing the database and restarting the program`    |
<!-- | `004` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `005` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `006` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `007` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `008` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `009` | `string` | `string`                                            | `string`                                                  | -->
<!-- | `010` | `string` | `string`                                            | `string`                                                  | -->
