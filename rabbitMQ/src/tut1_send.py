#!/usr/bin/env python 

'''
Created on Oct 26, 2011

@author: jds
'''
import pika

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body="Hello World!")
    print " [x] Sent 'Hello world!'"
    connection.close()
    