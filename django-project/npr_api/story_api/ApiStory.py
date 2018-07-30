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
    def story(self):
        """
        Convenience method to get straight to the good part of the API.
        :return:
        """
        return self.story_dict["list"]["story"][0]

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
    def title(self):
        story = self.story_dict["list"]["story"][0]
        return story["title"]["$text"]

    @property
    def headline(self):
        return self.title

    @property
    def author(self):
        """
        Author from the Story API story.
        :return: Dict of author information.
        """
        return {
            "name": self.story["byline"][0]["name"]["$text"],
            "id": self.story["byline"][0]["name"]["personId"],
            "link": (self.story["byline"][0]["link"][1]["$text"] if self.story["byline"][0]["link"] else None)
        }

    @property
    def byline(self):
        return self.author

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
                    "author": (image["producer"]["$text"] if "$text" in image["producer"] else ""),
                    "source": (image["provider"]["$text"] if "$text" in image["provider"] else ""),
                    "caption": (image["caption"]["$text"] if "$text" in image["caption"] else ""),
                    # Currently alt must pull from caption
                    # change this as soon as API is fixed.
                    "alt": (image["caption"]["$text"] if "$text" in image["caption"] else "")
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
                    "description": (audio["description"]["$text"] if audio["description"] else None)
                }
        return None
