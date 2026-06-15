import urllib.request
import ssl
import sys
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

logos = {
    'kenworth': 'https://logo.clearbit.com/kenworth.com',
    'kwangsung': 'https://logo.clearbit.com/kwangsung.co.kr',
    'kelloggs': 'https://logo.clearbit.com/kelloggs.com',
    'mohawk': 'https://logo.clearbit.com/mohawkind.com'
}

base_dir = r"c:\Users\victo\OneDrive\Escritorio\Servimex\static\img\logos"
os.makedirs(base_dir, exist_ok=True)

for name, url in logos.items():
    req = urllib.request.Request(url, headers=headers)
    filepath = os.path.join(base_dir, f"{name}.png")
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"Success: {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")
        # fallback to wikimedia or other public URLs if clearbit fails
        if name == 'kelloggs':
            fallback_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Kellogg%27s_logo.svg/1024px-Kellogg%27s_logo.svg.png'
            req = urllib.request.Request(fallback_url, headers=headers)
            try:
                with urllib.request.urlopen(req, context=ctx) as response:
                    with open(filepath, 'wb') as f:
                        f.write(response.read())
                print(f"Success (fallback): {name}")
            except Exception as e2:
                print(f"Fallback failed {name}: {e2}")
        elif name == 'kwangsung':
            # Create a dummy image or find another source
            pass
