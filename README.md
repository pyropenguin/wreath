# Wreath Project

This repo contains the code used to make an LED wreath for Christmas 2022.

## Installation

1. Git clone this repo
2. Put the following in the crontab:

    ```bash
    30 17 * * * python3 /home/jkunze/wreath/main.py
    # 30 19 * * * pkill -f "/home/jkunze/wreath/main.py"
    # @reboot python3 /home/jkunze/wreath/main.py
    ```

## To run

```bash
sudo python3 main.py # sudo required for LED access
```
