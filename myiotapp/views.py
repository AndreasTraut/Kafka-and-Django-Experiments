import re
from django.shortcuts import render
from django.utils.timezone import datetime
from kafka import KafkaConsumer, TopicPartition
import pickle # pickle converts data into byte array

# Create your views here.
# See https://docs.microsoft.com/en-us/windows/python/web-frameworks#hello-world-tutorial-for-django
from django.http import HttpResponse

def home(request):
    mykafkaconsumer_url = 'mykafkaconsumer'  # Define your URL here
    print("<a href={}>link</a>".format(mykafkaconsumer_url))
    return HttpResponse("Hello, Django! I am in a Ubuntu Container in Visual Studio! Please click <a href={}>here</a> to start mykafkaconsumer!".format(mykafkaconsumer_url))

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

def mykafkaconsumer(request): 
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='latest', enable_auto_commit=False, consumer_timeout_ms=1000)    
    consumer.subscribe(['UbuntuTopic'])
    
    deserialized_data = ""
    for message in consumer: 
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))                             
        #deserialized_data.append(pickle.loads(message.value))
        deserialized_data = message.value #.decode('utf-8') # pickle.loads(message.value)
    
    return HttpResponse("I am a Kafka-Consumer and I received: " + deserialized_data)


def mykafkaproducer(request): 
    myevent = ""
    # not yet implemented ....
    return HttpResponse("I am a Kafka-Producer and I am not doing anything at the moment... waiting for being implemented later....  ")