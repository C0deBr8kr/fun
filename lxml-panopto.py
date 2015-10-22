from lxml.html import parse
doc = parse('http://scs.hosted.panopto.com/Panopto/Podcast/Podcast.ashx?courseid=4b73b1cc-afb6-4f6b-96c0-476a24527e3e&type=mp4').getroot()
for link in doc.cssselect('enclosure'):
    if 'mp4' in link.get('url'):
        print link.get('url')
