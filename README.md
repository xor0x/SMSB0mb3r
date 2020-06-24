## Requirements
- Run on Windows, macOS or Linux.
- Python 3 and Pip installed on it.

## Installation and Setup
It's as easy as typing the below commands into your terminal.
```bash
# Clone my repo
git clone https://github.com/xor0x/SMSB0mb3r.git

# Move into the work directory.
cd SMSB0mb3r

# Install the requirements via Pip.
pip3 install -r requirements.txt
```

## Options
You can also read this via `python3 bomber.py -h` or `python3 bomber.py --help`

```
usage: bomber.py [-h] [--repetitions Repetitions] TARGET

positional arguments:
  TARGET                    Target mobile number without country code

optional arguments:
  -h, --help                show this help message and exit
  --repetitions Repetitions, -r Repetitions         Number of sms to target (default: 5000)
  --country COUNTRY, -c COUNTRY
                        Country code without (+) sign
  --proxy, -p           Use proxy for bombing (It is advisable to use this
                          option if you are bombing more than 5000 sms)
```


## Credits and Thanks
- Thanks [iMro0t](https://github.com/iMro0t) for the original source code. Find it [here](https://github.com/iMro0t/bomb3r/).

