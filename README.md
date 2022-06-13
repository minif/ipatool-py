# Scraping ready version
This is a WIP version of ipatool-py that should allow for mass downloading for scraping purposes.

### Usage:
```
main.py single [-h] [--appleid APPLEID]
                      (--password PASSWORD | --itunes-server ITUNES_SERVER)
                      [--purchase] [--latest] [--all] [--country COUNTRY]
                      [--appId APPID] [--bundleId BUNDLE_ID]
                      [--output-dir OUTPUT_DIR]
```

- Currently tested with `--itunes-server | -s`, but Apple ID should work (Not with 2FA)
	- Follow Manually way below to set up iTunes Server
	- You may use a VM, but be sure you can communicate it via HTTP on port 9000
- Use `--purchase` to only purchase an app, `--latest | -l` to download the latest, or `--all | -a` to get all versions
- Use `--country` to select a country that is not USA
- Use `--appId | -i` to input an app ID or `--bundleId | -b` to look up a bundle ID
- Use `--output-dir | -o` to select location for IPA files

### Example:
This should download all versions of "ABC Animals Coloring Book" using the iTunes Server on 192.168.0.102
```
python3 main.py single -s http://192.168.0.102:9000 -b com.kanapot.ABCColoring --all
```

### Multi-app scraping
```
main.py file [-h] [--appleid APPLEID]
                    (--password PASSWORD | --itunes-server ITUNES_SERVER)
                    [--purchase] [--country COUNTRY] [--latest] [--all] --path
                    FILE_PATH [--output-dir OUTPUT_DIR]

```
- Use `--path` to select a file containing app IDs to download
	- File must be .txt and IDs must be line-seperated.
- Use `--purchase` to only purchase an app, `--latest | -l` to download the latest, or `--all | -a` to get all versions
- Use `--country` to select a country that is not USA
- Use `--output-dir | -o` to select location for IPA files

Help is appreciated! Needs major refactoring and testing.
Needs iTunesServer (Read "Manually way" below) 

# IPATool-py

Python version of IPATool! 

**Now Supports**:
  - **Purchasing App via `--purchase`**
  - **Downloading Old IPA via iTunes Server**

## Installation

```
pip3 install -r requirements.txt
```

## Usage

There're three commands: lookup, historyver, download. Each command's usage can be found by `-h` option.

You can also chain multiple command, last command's output will be passed to next command (so you don't need to supply some arguments like appVerId)

### Download Newest Version

Download an app using bundleID (-o can be omited)
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download -e APPLE_EMAIL -p APPLE_PWD -o DIR
```

Or appID (`XXXXX` in the `apps.apple.com/app/xxxx/idXXXXXX`)
```
python3 main.py download -i XXXXX
```

You can also purchase apps when downloading using `--purchase`:
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download --purchase -e APPLE_EMAIL -p APPLE_PWD -o DIR
```

### Download OLD Version

Old versions must be downloaded together with `iTunes Server`. You can get `iTunes Server` in several ways:
- Using [action-ipadown](https://github.com/NyaMisty/action-ipadown) directly, which integrated this tool
    - NOTE: this method does not support 2FA
- Manually way: (supports 2FA)
    - download this repo: https://github.com/NyaMisty/actions-iTunes-header
    - install iTunes 12.6.5.3, from https://secure-appldnld.apple.com/itunes12/091-87819-20180912-69177170-B085-11E8-B6AB-C1D03409AD2A6/iTunes64Setup.exe
    - patch the iTunes using `actions-iTunes-header/workflow_helper/iTunesInstall/patch_itunes.py`
    - install frida: `pip3 install frida`
    - open iTunes, sign out & re-login your account
    - run: `actions-iTunes-header/workflow_helper/iTunesDownload/get_header.py`

After setting up the server, you can run this tool to download a specific version
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP download -s http://127.0.0.1:9000 --appVerId 833889087
```

### Get History Ver (usually used together with JSON)

Get all appVerId of app from Apple
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
```

### Lookup (usually used together with JSON)

Query app basic information:
- By bundleID: `python3 main.py lookup -b com.touchingapp.potatsolite -c JP`
- By appID: `python3 main.py lookup -i 1239860606 -c JP`

Query appVerId:
```
python3 main.py lookup -b com.touchingapp.potatsolite -c JP --get-verid
```

### Headless Usage

For each command you can use `--json` switch to get result of command in JSON

```
python3 main.py --json lookup -b com.touchingapp.potatsolite -c JP --get-verid
python3 main.py --json lookup -b com.touchingapp.potatsolite -c JP historyver -e APPLE_EMAIL -p APPLE_PWD
```

## Development

- All requests' reqBody and respBody are modeled using modified JSONSchema2PoPo2 (see my NyaMisty/JSONSchema2PoPo2), you can regenerate the binding by cd into `reqs/schemas` and execute `python3 -m schema_defs`
- See more information on how to generate schema in reqs/schemas directory

## Credit

- Thanks @majd's ipatool, which is written in swift
