import pip
pip.main(["install", "requests"])
import requests
from random import randint
import traceback
import os
pip.main(["install", "zipfile"])
import zipfile
import time
pip.main(["install", "re"])
import re
pip.main(["install", "selenium"])

from selenium import webdriver
pip.main(["install", "numpy"])

import numpy as np
import multiprocessing
pip.main(["install", "webdriver_manager"])

from webdriver_manager.chrome import ChromeDriverManager

def create_chromedriver(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, USER_AGENT, chunk):
    manifest_json = """
    {
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
            username: "%s",
            password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


    def get_chromedriver(use_proxy=True, user_agent=USER_AGENT):
        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()
        if use_proxy:
            pluginfile = 'proxy_auth_plugin.zip'
            with zipfile.ZipFile(pluginfile, 'w') as zp:
                zp.writestr("manifest.json", manifest_json)
                zp.writestr("background.js", background_js)
            chrome_options.add_extension(pluginfile)
        if user_agent:
            chrome_options.add_argument('--user-agent=%s' % USER_AGENT)
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        return driver

    driver = get_chromedriver(use_proxy=True)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    globalranks = []
    print(chunk)
    for i in chunk:#len(sites)
      driver.close()
      driver = get_chromedriver(use_proxy=True)
      driver.get(f"view-source:https://www.similarweb.com/top-websites/{i}")
      #time.sleep(randint(3, 5))
      baddata = driver.find_element_by_tag_name('body').text
      #print(baddata)
      baddata = baddata[139749:]
      data = []
      for line in baddata.splitlines():
          if "/website/" in line:
              data.append(line.replace(" ", "").replace("<ahref=\"/website/", "").replace("\"", ""))
      #print(data)
      f = open("out.txt", "a", encoding="utf-8")
      f.write(f"{i} - {data}\n")
      f.close()
    print(globalranks)

    # driver.get('https://www.google.com/search?q=my+ip+address')

def launch(*args):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    create_chromedriver('gate.smartproxy.com', 7000, 'user-onetest', 's8rp83tmdlpjJUqv1Zgy', user_agent, args)
if __name__ == '__main__':
    threads = 12
    sites = []
    with open('storage.txt') as my_file:
        sites = my_file.read().splitlines()
    chunks = np.array_split(sites, threads)
    procs = []
    for i in range(threads):
        print(chunks[i])
        proc = multiprocessing.Process(target=launch, args=(chunks[i]),)
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
