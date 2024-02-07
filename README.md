# AstarothConfigExtractor

Python script to extract the configuration from **Astaroth/Guildma** samples.

When the malware is deployed with AutoIT, the configuration is stored in the file **dump.log**, located in the same directory of the AutoIT interpreter and script.

This file encapsulates a base64-encoded string, which, upon decoding, reveals a string encoded with a custom algorithm.

The algorithm employs the first character of the decoded string as a key, subtracting the value 0x41. Subsequently, each two subsequent characters in the string undergo a series of arithmetic operations involving the key to obtain the original string.

The obtained string contains four elements, named **dt**, **out**, **tp** and **ips**, associated with base64-encoded strings.

The **out** element can be decoded to retrieve a list of URLs that can be used to obtain an updated malware configuration. The **ips** section, instead, contains a list of domain names and TCP ports employed by the malware for communication with the Command-and-Control (C2) server.

![image](https://github.com/Microv/AstarothConfigExtractor/assets/9150645/c7f5d24c-a20f-4356-9244-63d8d7843830)



## Usage
```
python.exe .\astaroth_config_extractor.py .\dump.log 
```

