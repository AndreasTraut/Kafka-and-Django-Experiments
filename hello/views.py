import re
from django.shortcuts import render
from django.utils.timezone import datetime
from kafka import KafkaConsumer, TopicPartition
import pickle # pickle converts data into byte array

# Create your views here.
# See https://docs.microsoft.com/en-us/windows/python/web-frameworks#hello-world-tutorial-for-django
from django.http import HttpResponse

def home(request):
    your_url = 'hello'  # Define your URL here
    print("<a href={}>link</a>".format(your_url))
    return HttpResponse("Hello, Django! I am in a Ubuntu Container in Visual Studio! Please click <a href={}>here</a>!".format(your_url))

def hello(request):
    return HttpResponse("Hello! Please enter a name behind the / in the url-adress!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def mykafkaview(request): 
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest', enable_auto_commit=False, consumer_timeout_ms=1000)    
    consumer.subscribe(['UbuntuTopic'])
    
    #deserialized_data = []
    for message in consumer: 
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))                             
        #deserialized_data.append(pickle.loads(message.value))
        deserialized_data = message.value # pickle.loads(message.value)
        return HttpResponse("I received: " + deserialized_data)

"""     for p in consumer.partitions_for_topic('UbuntuTopic'):
        tp = TopicPartition('UbuntuTopic', p)
        consumer.assign([tp])
        committed = consumer.committed(tp)
        consumer.seek_to_end(tp)
        last_offset = consumer.position(tp)
        print("topic: %s partition: %s committed: %s last: %s lag: %s" % ('UbuntuTopic', p, committed, last_offset, (last_offset - committed)))
 """