```py
>>> from selenium import webdriver
>>> from selenium.webdriver.chrome.options import Options
>>> options = Options()
>>> options.add_argument("--disable-web-security")
>>> options.add_argument("--disable-features=IsolateOrigins,site-per-process")
>>> driver = webdriver.Chrome(options=options)
```
