# kahootSmash
A Kahoot flooder tool made with Python and Selenium. This tool generates random bots to join a Kahoot game.  
Download this tool in the [__releases__](https://github.com/switchmeep/kahootSmash/releases) page of this repository.  

## How to use:
Run client.py, enter your game pin, and adjust the thread count. Thread count is the amount of threads to create, not the amount of bots. A higher thread count will result in faster botting, but use more of your cpu.

![](https://s10.gifyu.com/images/9EmsqL6kYt.gif)

Bots will begin to join the kahoot session.

![](https://s10.gifyu.com/images/chrome_X3uHCi5DWw.gif)

Key Features:
 - Extremely lightweight.
 - Incognito mode.
 - Username randomization.

## Setup Guide
1. Install Python 3.8 (or higher) at [**python.org**](python.org).
2. Open your terminal and run the command `pip install selenium`.
3. Download [**chromedriver**](https://chromedriver.chromium.org/downloads).
 - Be sure to download the version that matches your chrome version. You can find your chrome version in Chrome Settings > About.  
 - Place chromedriver.exe inside the same directory as the kahootSmash client.

## Requirements
- Selenium
- Tkinter

## Warnings
- I do not condone the act of Kahoot flooding. This tool was made for educational purposes.
- The amount of threads that the client can run is limited by your cpu. Large thread counts may crash your computer.
