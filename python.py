
def  download_image(image_url,i,albumi,titl,thumb):
    url = str(image_url)
    r = requests.get(url, allow_redirects=True)
    filename = url.split('/')[-1]
    path = 'images/{}.png'.format(id)
    open(path, 'wb').write(r.content)
    img = Image.open(path)
    resized_img = img.resize((500, 500), Image.ANTIALIAS)
    resized_img.save(path)
    img.show()


def add_photo(request):
       url = 'http://jsonplaceholder.typicode.com/photos' 
       response = requests.get(url)
       data = jsonRes = response.json() 
       i = 0
       with ThreadPoolExecutor(max_workers=3) as executor:
              for x in data :
                     i = i+1
                     executor.submit(download_image,x['url'],x['id'],x['albumId'],x['title'],x['thumbnailUrl'])
                     print(i)

