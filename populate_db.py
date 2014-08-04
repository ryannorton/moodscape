import os
from datetime import datetime
from random import randint

def populate():

    add_tweet(text="This is my first tweet!",
        location="El Paso, TX",
        user="ryannorton",
        date=datetime(2014,1,1,12,32,5),)

    add_tweet(text="Moodscape is going to be awesome!",
        location="Austin, TX",
        user="ryannorton",
        date=datetime(2014,1,2,13,14,52),)

    add_tweet(text="Can't wait til I'm done!",
        location="Portland, OR",
        user="tabchas",
        date=datetime(2014,1,2,4,12,24),)

    add_tweet(text="Here is another test tweet!",
        location="El Paso, TX",
        user="ryannorton",
        date=datetime(2014,1,2,7,30,9),)

    add_tweet(text="Going to play my guitar!",
        location="Philadelphia, PA",
        user="johnmayer",
        date=datetime(2014,1,3,11,31,8),)

    add_tweet(text="Let's start another company!",
        location="Mountain View, CA",
        user="elonmusk",
        date=datetime(2014,1,4,17,44,12),)

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    for state in states:
        add_state(name=states[state], abbrev=state)

    # Print out what we have added to the user.
    for t in Tweet.objects.all():
        print "- {0} - {1}".format(str(t.user), str(t))

    for s in State.objects.all():
        print "- {0} - {1}".format(str(s.abbrev), str(s.sentiment))

def add_tweet(text, location, user, date):
    t = Tweet.objects.get_or_create(text=text, location=location, user=user, date=date)[0]
    return t

def add_state(name, abbrev):
    s = State.objects.get_or_create(name=name, abbrev=abbrev, sentiment=randint(0,100))[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print "Starting database population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MoodScape.settings')
    from app.models import Tweet, State
    populate()