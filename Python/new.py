import pyshorteners

print("Welcome to the url shortener")

long_url = input("Enter the long url: ")



def url_shortener(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    print(f"{short_url}")

url_shortener(long_url)