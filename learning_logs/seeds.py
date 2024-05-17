from learning_logs.models import Topic

def run():
    Topic.objects.create(text='Django Basics')
    Topic.objects.create(text='Advanced Django')
    Topic.objects.create(text='Python Basics')
    Topic.objects.create(text='Machine Learning')

def print_all():
    topics = Topic.objects.all()
    for topic in topics:
        print(topic.id, topic.text)
