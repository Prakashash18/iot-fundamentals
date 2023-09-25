# iot-fundamentals

# Two ways to install required dependencies on Rpi 4 Bullseye OS

## First Way
1. Download shell file

`wget https://raw.githubusercontent.com/Prakashash18/iot-fundamentals/main/install.sh`

2. Install required
   
`sh install.sh`

## Second Way

1. Clone the repo to your local directory

`git clone https://github.com/Prakashash18/iot-fundamentals.git`

2. Install required dependencies 

`cd iot-fundamentals && pip install -r requirements.txt`

3. Remove repo

`cd .. && sudo rm -r iot-fundamentals`
