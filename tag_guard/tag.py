import string

class Tag:
  def __init__(self, tag):
    # tag = tag.translate(string.maketrans('', '', string.punctuation)) # Strips punctuation
    tag = tag.lower() # Makes lowercase
    self.tag = tag
       
  def __str__(self):
    return self.tag
  
  def __eq__(self, other):
    return str(self) == str(other)

  