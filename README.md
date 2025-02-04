# QR API

Made with **Flask and Python**. A simple API that makes QRs easily. To install the requirements and stuff needed just run

```
sh install.sh
```

# How to use?

The API will be ran following the settings declared on *global.conf*.
1. To run the API type:

```
sh run.sh
```


2. Once the app is running, the structure to make a request to the API is on the JSON body, like the next one:

```
{
	"content": "the content of your QR code"
}
```

NOTE: the generated QRs will be saved on the folder declared on *global.conf*

3. And finally the answer will be in JSON format and follows the next structure:

```
{
	"path": "where the generated QR is located"
}
```

