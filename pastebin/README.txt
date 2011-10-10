This is the example code from 
"Practical web development with django" "Chapter 10: Pastebin"


I learn the following things. ( I  dont like the fact they use exclusivly generic views, 
they explain it... but I dont have to like it.)


  - Note this is doing some fairly advanced generic views things with 
    from django.views.generic.list_detail import object_list, object_detail
    from django.views.generic.create_update import create_object
  
  - How to do a nested settings.py file, so our App, in this case "pastebin" can have its own settings defines
    fro the media. I have not even read about this yet... I just copied the code from Brain R. I need to find 
    where this technique is documented.
    
  - How to plug in the "syntaxhighlighter" code.