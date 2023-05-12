# Python Projectopdracht Trojan 22-23

## Documentation

This Python script makes use of a GitHub repository that you will need to create yourself. This repository has to contain a JSON file. This JSON file will be used to configure which modules you want the script to execute. When changing to different modules the script will remotly change it functionality.

To make use of this script you will need to pull this repository and add a .env file.  
This .env file has to contain these variables:
```
    ftp-host=<ftp-server-ip>
    ftp-port=<ftp-server-port>
    ftp-user=<ftp-server-user>
    ftp-password=<ftp-server-user-password>
    repo=<remote-github-repository>
    config-file=<config-file-inside-repo>
```

## Modules