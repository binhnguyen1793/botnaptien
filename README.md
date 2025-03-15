1.1. Update the System:
sudo apt update && sudo apt upgrade -y

1.2. Install Python and pip:
sudo apt install python3 python3-pip -y

1.3. Install Google Chrome & ChromeDriver:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y

Retrieve the installed Chrome version and download the matching ChromeDriver:
CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+')
wget https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/
sudo chmod +x /usr/bin/chromedriver

1.4. Install Selenium: 
pip3 install selenium

2.1. Create a Directory for the Script: 
mkdir selenium_script && cd selenium_script

2.2. Create the a.py File
Use nano to create the file and paste the script inside:
nano a.py

2.3. Run the Script with Parameters:
python3 a.py 100000  # Replace 100000 with the desired amount
