# Python Tools
### Device Specififcation
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
        - `autoremove`
        - `clean`
        - `cache/apt`
        - `cache/thumbnails`
### English Dictionary [ Link ](English%20Dictionary)
```python
from dictionary import Dictionary
dictionary_data = Dictionary()
dictionary_data.suggest_status = True
print(dictionary_data['cosmos'])
>>> Everything that exists anywhere.

print(dictionary_data['helo'])
>>> We didn not find helo.
>>> Please have a look similar word matching with your input key
['Help', 'Hel', 'Helot', 'Hero', 'He lo', 'He-lo', 'Hel o', 'Hole', 'Hello', 'Halo', 'Hell', 'Held']
```