from .. import TagSet
class Group:
  def __init__(self, name, tags):
    self.name = name 
    self.tags = TagSet(tags)