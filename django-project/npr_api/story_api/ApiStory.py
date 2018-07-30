"""
Story API Story Class
"""

from get_story import get_story_dict
from datetime import datetime


class ApiStory:

    def __init__(self, story_id):
        self.story_id = story_id
        self.story_dict = get_story_dict(story_id)

    @property
    def canonical_link(self):
        links = self.story_dict["list"]["link"]
        for link in links:
            if link["type"] == "html":
                return link["$text"]
        return None

    @property
    def date_time(self):
        # Format from json: Thu, 19 Jul 2018 09:48:06 -0400
        return datetime.strptime(
            self.story_dict["list"]["story"][0]["storyDate"]["$text"][:-6],
            "%a, %d %b %Y %H:%M:%S")

    @property
    def html_text(self):
        text_with_html_arr = self.story_dict["list"]["story"][0]["textWithHtml"]["paragraph"]
        # This elaborate list comprehension was a better idea at the time.
        # Here's what it does:
        #    1. Go through the array of paragraphs.
        #    2. Extract the text.
        #    3. Add paragraph tags.
        #    4. Merge the list into one string.
        return u"".join([u"<p>{}</p>".format(p["$text"]) for p in text_with_html_arr])

    @property
    def image(self):
        """
        Primary image from the Story API story, if there is one. None if not.
        :return: Dict of image information. None if none.
        """
        story = self.story_dict["list"]["story"][0]
        if story["image"]:
            if len(story["image"]) > 0:
                image = story["image"][0]
                return {
                    "url": image["src"],
                    "id": image["id"],
                    "author": image["producer"]["$text"],
                    "source": image["provider"]["#text"],
                    "caption": image["caption"]["$text"],
                    # Currently alt must pull from caption
                    # change this as soon as API is fixed.
                    "alt": image["caption"]["$text"]
                }
        return None

    @property
    def audio(self):
        """
        Primary audio from the Story API story, if there is one.
        :return: Dict of audio information. None if none.
        """
        story = self.story_dict["list"]["story"][0]
        if story["audio"]:
            if len(story["audio"]) > 0:
                audio = story["audio"][0]
                return {
                    "url": audio["format"]["mediastream"]["$text"],
                    "duration": audio["duration"]["$text"],
                    "description": audio["description"]["$text"]
                }
        return None