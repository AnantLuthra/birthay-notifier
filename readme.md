# Birthday notifier

- This is a birthday notifier tool, it fetches data from excel sheet and sends notification if their is a birthday or in 1 or 2 days.

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

- Then run [`script.py`](./script.py) file and message will be sent to you..