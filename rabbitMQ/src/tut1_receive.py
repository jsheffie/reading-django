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

    print ' [*] Waiting for messages. To exit press CTRL+C'
    
    def callback(ch, method, properties, body):
        print " [x] Received %s" % ( body,)
    
    channel.basic_consume(callback, 
                          queue='hello',
                          no_ack=True)
    
    channel.start_consuming()