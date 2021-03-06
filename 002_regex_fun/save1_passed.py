import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
    """
    m = re.compile(r'\d+:\d+')
    return m.findall(course)


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function.
    """
    m = re.compile(r'http\S+|#\w+')
    return m.findall(tweet)


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in html."""
    m = re.compile(r'<p>(.+?)</p>')
    return m.findall(html)[0]