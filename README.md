# ping
checks if certain pages are up  and diplays  status in  simple http interface


To run type

```
python ping.py
```
it will periodicly check if current pages are up

To set pages to check and period edit ``` config.py``` file.


To watch live statuses type
```
python -m SimpleHTTPServer 8000
```

and go to ``` http://localhost:8000/ ``` 

It will reload data every 10 seconds