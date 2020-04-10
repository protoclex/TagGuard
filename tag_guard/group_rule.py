class GroupRule:
  def __init__(self, group, tag_requires, tag_conflicts, group_requires, group_conflicts):
    self.group = group
    self.tag_requires = set(tag_requires)
    self.tag_conflicts = tag_conflicts
    self.group_requires = group_requires
    self.group_conflicts = group_conflicts
  
  def meets_requirements(self, tagset):
    if self.group.tags.intersection(tagset):
      if not tagset.issuperset(self.tag_requires):
        return False
      for group in self.group_requires:
        # tagset must share at least one tag that's a member of the current group
        if tagset.isdisjoint(group.tags):
          return False
    return True

  def no_conflicts(self, tagset):
    if self.group.tags.intersection(tagset):
      if tagset.intersection(self.tag_conflicts):
        return False
      for group in self.group_conflicts:
        # tagset must share no tag that is a member of the current group
        if tagset.intersection(group.tags):
          return False
    return True

  def check(self, tagset):
    return (
      self.meets_requirements(tagset) and 
      self.no_conflicts(tagset)
    )