# coding=gbk

def city_country(city,country):
    message = '"' + city + "," + country + '"'
    return message
    
message1 = city_country('beijing','china')
print(message1) 
    
def make_album(singer,album,number=''):
    information = {'musician':singer,'music':album}
    if number:
        information['number'] = number
    return information
    
one = make_album("jay zhou","qi li xiang")
print(one)
two = make_album("vae","su ge la mei you di",12)
print(two)

def make_album(singer,album,number=''):
    information = {'musician':singer,'music':album}
    if number:
        information['number'] = number
    return information
    
while True:
    print("enter 'q' at any time to quit")
    singer = input("���ֵ�����")
    if singer == 'q':
        break
    album = input("ר��������")
    if album == 'q':
        break
    number = input("������")
    if number == 'q':
        break
    song = make_album(singer,album,number)
    print(song)
