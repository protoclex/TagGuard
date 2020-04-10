class GroupFailure:
  def __init__(self, result, checked, other_tags, other_groups):
    self.result = result
    self.checked = checked
    self.other_tags = other_tags
    self.other_groups = other_groups
  def __str__(self):
    return (
      f"Tag set invalid because the tag {self.checked} "
      f"{self.result} the tags "
      f"{self.other_tags} and the groups "
      f"{self.other_groups}"
    )