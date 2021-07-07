class AddTags(object):
    def __init__(self, tags):
        self.tags = tags
        self.new_tags = []

    def clean_tags(self):
        new_tags = ""
        with open(self.tags, "r") as file:
            tag_file = file.read().split(" ")
            for word in tag_file:
                for remove in [" ", "\n", "#"]:
                    word = word.replace(remove, "")
                new_tags += word
        return new_tags.split(",")

    def tag_checker(self):
        valids = []
        new_tags = self.clean_tags()
        with open("tag_list.txt", "r") as origional_tags:
            for new_tag in new_tags:
                if new_tag not in origional_tags.read().split(","):
                    valids.append(new_tag)
        return valids
