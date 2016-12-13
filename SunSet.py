try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import time
#from twilio.rest import TwilioRestClient

request = ('http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=9b56b06ab4c7f06821ccf55e3e10fce5')

response = urllib2.urlopen(request)
#data = response.read()

str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
sunset = obj['sys']['sunset']
sunset_time = time.strftime('%H:%M:%SPM', time.localtime(sunset))

cur_time = time.strftime('%H:%M:%SPM', time.localtime())
#cur_time1 = time.strftime('%H:%M:%SPM', time.localtime())

if cur_time == sunset_time:
    from twilio.rest import TwilioRestClient

    account = "ACe1b4216246d4bfa4e46b97fcf1b747f4"
    token = "445ec508c12eac63a09818fcd1034d7c"
    client = TwilioRestClient(account, token)

    message = client.messages.create(from_="+1(847) 380 - 8591", to="+18474712449",
                                     body="The Sun is Setting!")



