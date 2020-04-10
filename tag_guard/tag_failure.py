class TagFailure:
  def __init__(self, result, checked, other_tags):
    self.result = result
    self.checked = checked
    self.other_tags = other_tags
  def __str__(self): 
    return (
      f"Tag set invalid because the tag {self.checked} "
      f"{self.result} the tags "
      f"{self.other_tags}"
    )