import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'learning_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all() #equivalent of Select * from in SQL

for topic in topics:
    print(topic.id)
    print(topic.text) #can also do just (Topic) because of the str code we have in models.
    print(topic.date_added)  #all from models


t = Topic.objects.get(id=1)
print(t) #prints Chess

entries = t.entry_set.all()


for e in entries:
    print(e)