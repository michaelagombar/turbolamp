try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import time


request = ('http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=9b56b06ab4c7f06821ccf55e3e10fce5')

response = urllib2.urlopen(request)

str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
sunset = obj['sys']['sunset']
sunset_time = time.strftime('%H:%M', time.localtime(sunset))

cur_time = time.strftime('%H:%M', time.localtime())
cur_time2 = time.strftime('%H:%M', time.localtime())

#if cur_time == cur_time2:
if cur_time == sunset_time:
    from twilio.rest import TwilioRestClient #cool

    account = "ACe1b4216246d4bfa4e46b97fcf1b747f4"
    token = "445ec508c12eac63a09818fcd1034d7c"
    client = TwilioRestClient(account, token)

    message = client.messages.create(from_="+1(847) 380 - 8591", to="+xxxxxxxx",
                                     body="The Sun is Setting and the time is {}".format(sunset_time))



