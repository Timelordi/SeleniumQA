import webbrowser

def validator(func):
    def wrapper(URL):
        if "." in URL:
            func(URL)
        else:
            print("Invalid URL")
    return wrapper

@validator
def openURL(URL):
    webbrowser.open(URL)

openURL("https://www.webometrics.info/")