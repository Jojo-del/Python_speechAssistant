import webbrowser
import bitcoinAPI, email_assistant
import subprocess

bitcoin= bitcoinAPI.Bitcoin()
mail= email_assistant.email_assistantClass()



def scanString(sourceString):
    if 'twitter' in sourceString:
        webbrowser.open('https://twitter.com')

    if 'trump' in sourceString and 'twitter' in sourceString:
        webbrowser.open('https://twitter.com/realdonaldtrump')

    elif 'tesla stock' in sourceString:
        webbrowser.open('https://de.tradingview.com/chart/0yUk04Bf/')

    elif 'tesla website' in sourceString:
        webbrowser.open('https://www.tesla.com/')

    elif 'instagram' in sourceString:
        webbrowser.open('https://www.instagram.com')

    elif 'bitcoin' in sourceString and 'euro' in sourceString:
        print(f'1 Euro <-> {bitcoin.getEURBitcoins()} Bitcoin  || {bitcoin.getTime()}')

    elif 'bitcoin' in sourceString and 'dollar' in sourceString:
        print(f'1 USD <-> {bitcoin.getUSDBitcoins()} Bitcoin  || {bitcoin.getTime()}')

    elif 'school' in sourceString and 'email' in sourceString:
        webbrowser.open('https://outlook.office365.com/mail/inbox/id/AAQkADhiZTUxZDY4LWJlNmYtNDk5OS04NzZkLWNhNmVlNGZmYTYyOQAQAM%2FJ%2FzQGNShDgl2HfKXLNpM%3D?state=0')

    elif 'mail' in sourceString and 'open' in sourceString:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

    elif 'latest' in sourceString and 'space' in sourceString and 'video':
        webbrowser.open('https://www.youtube.com/watch?v=W8K0HrAS3fU')

    elif 'united states of america' in sourceString:
        webbrowser.open('https://www.youtube.com/watch?v=ygHkNOQWOzY')

    elif 'darknet' in sourceString:
        subprocess.call([r'C:\Users\johan\Desktop\Tor Browser\Browser\firefox.exe'])

    elif 'opera' in sourceString:
        subprocess.call([r'C:\Users\johan\AppData\Local\Programs\Opera\launcher.exe'])

    elif 'flight' in sourceString or 'airplanes' in sourceString:
        if 'austria' in sourceString:
            webbrowser.open('https://www.flightradar24.com/47.99,12.34/7')

        elif 'us' in sourceString or 'north america' in sourceString:
            webbrowser.open('https://www.flightradar24.com/44.75,-88.11/4')

        elif 'europe' in sourceString:
            webbrowser.open('https://www.flightradar24.com/54.8,35.56/4')

        elif 'africa' in sourceString:
            webbrowser.open('https://www.flightradar24.com/4.7,33.01/4')

        elif 'south america' in sourceString:
            webbrowser.open('https://www.flightradar24.com/-16.17,-57.7/4')

        elif 'asia' in sourceString:
            webbrowser.open('https://www.flightradar24.com/41.99,98.51/4')

        elif 'australia' in sourceString:
            webbrowser.open('https://www.flightradar24.com/-24.74,136.25/5')

    elif 'chrome' in sourceString:
        subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    elif 'excel' in sourceString:
        subprocess.call(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

    elif 'eclipse' in sourceString:
        subprocess.call(r"C:\Program Files\eclipse\eclipse.exe")

    elif ('send' in sourceString or 'write' in sourceString) and 'email' in sourceString:
        mail.init_settings()
        mail.mailing()





