# Python Tools
## Random tools building using python
### Device specififcation:
- Windows
    - `python3 specs_device.py`
    - Output
        ```
        {
            "Manufacture Date": "19 Nov, 2020",
            "Device Age": "1 year 2 month 21 day",
            "OS Install Date": "16th Aug, 2021",
            "OS Age": "5 month 23 day",
            "Brand Name": "Acer",
            "Model Name": "Nitro AN515-55"
        }
        ```
- Linux
    - `sudo python3 specs_device.py`
    - Output
        ```
        {
            "Manufacture Date": "19 Nov, 2020",
            "Device Age": "1 year 2 month 21 day",
            "Brand Name": "Acer",
            "Model Number": "Nitro AN515-55",
            "Model Family": "Nitro 5",
            "RAM Size": "16 GB"
        }
        ```
### Device Junk Clean
- Windows
    - `python3 pc_clean.py`
    - It will execute following command & clean
        - `temp`
        - `%temp%`
        - `recent`
        - `prefetch`
        - `tree`
- Linux
    - `sudo python3 pc_clean.py`
    - It will execute following command & clean
        - `cache/apt`
        - `cache/thumbnails`
        - `autoremove`
        - `clean`