class TagRule:
  def __init__(self, tag, requires, conflicts):
    self.tag = tag
    self.requires = set(requires)
    self.conflicts = set(conflicts)
  
  def meets_requirements(self, tagset):
    if self.tag in tagset:
      if not tagset.issuperset(self.requires):
        return False
    return True

  def no_conflicts(self, tagset):
    if self.tag in tagset:
      for tag in tagset:
        if tag in self.conflicts:
          return False
    return True

  def check(self, tagset):
    return (
      self.meets_requirements(tagset) and 
      self.no_conflicts(tagset)
    )