# Birthday notifier

- This is a birthday notifier tool, it fetches data from excel sheet and sends notification if their is a birthday or in 1 or 2 days on whatsapp to a specified phone number.

## Steps to use

- Make a `log.txt`, `check.txt`, `values.txt`
- Put yesterday's date in `check.txt` in following way. ex- `30:1:True`
```
date:month:True
```
- Put following data in following order in `values.txt` file.

```
excel-sheet-path
green-id:green-token
mobile-number
```
- mobile-number - is that number to which you'll send upcoming birthday's to.
- This tool uses [`green-api`](https://console.green-api.com) so kindly make your account their and connect you whatsapp account and put green-id and green-token or say key in `values.txt` file.
- and for running it daily, put a shortcut of [script.py](./script.py) python file into your windows startup folder so it runs daily. 
- Then run [`script.py`](./script.py) file and message will be sent to you..