import os
from AddTags import AddTags

class TagGenerator(object):
    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))

        if not os.path.exists("tag_list.txt"):
            with open("tag_list.txt", "w+") as tags:
                pass
        self.tag_list = "tag_list.txt"

    def add_tags(self, tags):
        new_tags = AddTags(tags).tag_checker()
        print(new_tags)

if __name__ == "__main__":
    TagGenerator().add_tags("tags.txt")
    
