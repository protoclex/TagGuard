class TagSet(set):
  def intersection(self, other):
    return super().intersection(other)

  def add_tag(self, tag):
    super().add(tag)

  def remove_tag(self, tag):
    super().discard(tag)

  def has_group(self, engine, group):
    pass
  
