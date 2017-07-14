import sys
import os

if len(sys.argv) != 2:
    print "Usage: gen_podcast <directory>"
    exit()
    
DIR = sys.argv[1]

FEED_HEADER = '<?xml version="1.0" encoding="utf-8"?> \n \
<rss version="2.0" xmlns:itunes="http://www.itunes.com/DTDs/Podcast-1.0.dtd"
xmlns:media="http://search.yahoo.com/mrss/"> \n \
\n \
<channel> \n  \
<title> {} </title>\n  \
<description> My Audio Books </description>\n \
<itunes:author>Author</itunes:author>\n \
<link> nas </link>\n \
<itunes:image href="http://www.yourserver.com/YourPodcastPicture.jpg" />\n \
<pubDate> Fri, 13 Jan 2017 21:00:00 EST </pubDate>\n \
<language>en-us</language>\n \
<copyright> Not Copyright </copyright>\n \n'

FEED_FOOTER = '</channel> \n \
</rss> \n \
'

EPISODE_TEMPLATE = '<item> \n \
<title> {} </title> \n \
<description> desc </description> \n \
<itunes:author> Name </itunes:author> \n \
<pubDate> Fri, 13 Jan 2017 21:00:01 EST </pubDate> \n \
<enclosure url="http://192.168.1.145/{}" length="{}" type="audio/mpeg" /> \n \
</item>'

out = open('{}/{}.xml'.format(DIR, DIR), 'w')
out.write(FEED_HEADER.format(DIR))

for f in sorted(os.listdir(DIR)):
    if 'mp3' not in f:
        continue
    title = f.replace('.mp3', '')
    filename = DIR + '/' + f
    size = os.path.getsize("{}/{}".format(DIR, f))
    out.write(EPISODE_TEMPLATE.format(title, filename, size))
    
out.write(FEED_FOOTER)

idx = open('index.html', 'a')
idx.write('<a href="{}/{}.xml">{}</a><br>\n'.format(DIR, DIR, DIR))
idx.close() 
