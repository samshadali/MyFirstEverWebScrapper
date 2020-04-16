import requests 
import bs4
url = input("Enter Url :")
response = requests.get(url)
# print(type(response))
# print(response.text)
filename = "lol.html"
bs = bs4.BeautifulSoup(response.text ,"html.parser" )

formatted_text = bs.prettify()
#print(formatted_text)

with open(filename ,"w+") as f :
    f.write(formatted_text)
    
list_img = bs.find_all('img')
# print(list_img)
no_of_imgs = len(list_img)
list_as = bs.find_all('a')
no_of_as = len(list_as)
print("NO of img :" ,  no_of_imgs)
print("no of a tag :" ,  no_of_as)

