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

    message=' '.join(sys.argv[1:]) or "Hello World!"

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print " [x] Sent %r" % ( message )
    connection.close()
    