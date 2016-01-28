# OpManager Decrypter Tools
These two python scripts allow for the decryption of credentials stored within Manage Engine OpManager databases. These include WMI, SSH and VMWare credentials, among others. The purpose of this code is to aid further network compromise in the event that one has compromised an OpManager installation. This code has been tested on credentials extracted from OpManager 11.6.

Two encryption schemes are used by OpManager, DES ECB and a custom encryption scheme. In OpManager these are defined in the com.adventnet.me.opmanager.server.util.OpManagerPasswordDecoder and com.adventnet.security.authorization.Coding Java classes, respectively.

 The following table details the credentials, their encryption mechanism and where they are stored:

| Credential | Encryption Scheme | Storage |
|------------|-------------------|---------|
| OpManager Accounts | OpManager | configuration file |
| SSH/Telnet | OpManager | commoncredential DB table |
| WMI | OpManager | commoncredential DB table |
| Citrix | DES | vicredential DB table |
| VMWare | DES | vicredential DB table |
| UCS | DES | ucscredential DB table |
      
## Retrieving Encrypted Passwords
Encrypted passwords can be retrieved from the OpManager instance by either dumping the PostgreSQL database on the host or using the /api/json/admin/SubmitQuery endpoint after logging into the web interface. The PostgreSQL database can be dumped by executing 'pg\_dump.exe -h 127.0.0.1 -p 13306 -U postgres OpManagerDB' on the OpManager host, assuming standard configuration. To use the JSON interface, log in an obtain a valid API key, then execute something like:

```
POST /api/json/admin/SubmitQuery?apiKey=<apikey>HTTP/1.1
Host: <whatever>
Content-Type: application/x-www-form-urlencoded
Content-Length: 56

query=select username, password from commoncredential;
```

Encrypted passwords for OpManager users themselves can be retrieved from the [OpManagerHome]/conf/securityDbData.xml file. These can be decrypted using opmanager-decrypt.py. 


## opmanager-decrypt.py
This script decrypts passwords stored using the customer OpManager Coding encryption scheme. Execute by passing the cipher text as argv[1]

```
$ ./opmanager-decrypt.py d7962C6y778XdgyO6ibs
trialuserlogin
```

## opmanager-des-decrypt.py
Simple DES decrypted loaded with the key hard coded in the OpManagerPasswordDecoder class. Execution is the same as above.

```
$ ./opmanager-des-decrypt.py gjxrer9jXqs2sa1i0lfyzQ==
asdfqwer
```

Note that both scripts require python2.
