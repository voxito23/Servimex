import urllib.request
import re
import os

urls = [
    'https://worldvectorlogo.com/logo/kenworth-1',
    'https://www.crunchbase.com/organization/kwang-sung-electronics',
    'https://worldvectorlogo.com/logo/kellogg-s-red',
    'https://logowik.com/rheem-logo-vector-svg-pdf-ai-eps-cdr-free-download-17196.html',
    'https://empleonuevo.sfo2.cdn.digitaloceanspaces.com/public/companies/logos/jLIl98wCNBZ6zrteFFBZKfX1c3NGVAFvR6IvZTcs.jpeg',
    'https://www.skywin.be/sites/default/files/logo-membres/Sonaca_Logotype_RGB_%28%2B%29.png',
    'https://logowik.com/deacero-logo-vector-44937.html',
    'https://worldvectorlogo.com/logo/mohawk-industries-logo'
]

names = [
    'kenworth',
    'kwang-sung',
    'kelloggs',
    'rheem',
    'poly',
    'sonaca',
    'deacero',
    'mohawk'
]

os.makedirs('static/img/logos', exist_ok=True)

for i, url in enumerate(urls):
    name = names[i]
    if url.endswith('.png') or url.endswith('.jpeg'):
        ext = url.split('.')[-1]
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req).read()
            with open(f'static/img/logos/{name}.{ext}', 'wb') as f:
                f.write(data)
            print(f'Downloaded {name}.{ext}')
        except Exception as e:
            print(f'Failed to download {name}: {e}')
        continue
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        target_url = None
        if 'worldvectorlogo' in url:
            match = re.search(r'<img[^>]+src="([^"]+\.svg)"', html)
            if match:
                target_url = match.group(1)
        elif 'logowik' in url:
            match = re.search(r'<img[^>]+src="(https://logowik\.com/content/uploads/images/[^"]+)"', html)
            if match:
                target_url = match.group(1)
        elif 'crunchbase' in url:
            print(f'Crunchbase needs manual extraction for {name}')
            continue
            
        if target_url:
            print(f'Downloading {target_url} for {name}')
            ext = target_url.split('.')[-1]
            if not target_url.startswith('http'):
                target_url = 'https://worldvectorlogo.com' + target_url if target_url.startswith('/') else target_url
            
            img_req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(img_req).read()
            with open(f'static/img/logos/{name}.{ext}', 'wb') as f:
                f.write(img_data)
        else:
            print(f'No image URL found for {name}')
    except Exception as e:
        print(f'Error processing {name}: {e}')

