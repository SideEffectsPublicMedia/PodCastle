"""
Story API Story Class
"""

from get_tag import get_tag_dict
from datetime import datetime
from django.conf import settings


class ApiTag:


    def __init__(self, tag_id, org_id=None, restrict=None):
        self.tag_id = tag_id

        # Initialize some cached things.
        self.stories = []

        # Set orgId needed to complete query
        if org_id:
            self.org_id = org_id
        else:
            self.org_id = settings.STATION_ID

        # Set restrictions for what content types
        # a story must have to list, then make the request.
        if restrict:
            self.tag_dict = get_tag_dict(tag_id=tag_id, org_id=self.org_id, restrict=restrict)
        else:
            self.tag_dict = get_tag_dict(tag_id, org_id=self.org_id)


    @property
    def num_stories(self):
        """
        Count how many stories are in the API entry.
        :return: Integer number of stories. Zero if none.
        """
        if self.tag_dict["list"]["story"]:
            return len(self.tag_dict["list"]["story"])
        return 0

    @property
    def story_ids(self):
        """
        Return an array of story IDs.
        :return: Array of story IDs. Empty if no stories.
        """
        if self.num_stories <= 0:
            return []
        else:
            stories = self.tag_dict["list"]["story"]
            return [d["id"] for d in stories]

    @property
    def title(self):
        """
        The title of the story API tag group.
        :return:
        """
        return self.tag_dict["title"]["$text"]
