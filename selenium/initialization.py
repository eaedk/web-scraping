#!/usr/bin/env python
# coding: utf-8

# [Official Doc](https://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-seleniumhttps://selenium-python.readthedocs.io/installation.html#installing-python-bindings-for-selenium)

# In[5]:


# install the package locally
get_ipython().system('pip install -q selenium webdriver-manager')
#Then test if everything works perfectly


# In[3]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.close()
#it works let get started

