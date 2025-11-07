url = "https://www.kaggle.com/models/google/gemma"
protocol = url[ : url.find(':')]

dot_1 = url.find('.')
dot_2 = url.find('.',dot_1 + 1)
domain = url[dot_1 + 1 : dot_2]

page = url[url.find('/',dot_2):]

print("protocol:",protocol)

print("domain: ",domain)

print("page:   ",page)