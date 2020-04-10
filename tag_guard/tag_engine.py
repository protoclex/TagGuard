import TagFailure, GroupFailure

class TagEngine:
  def __init__(self, tag_rules, group_rules, group_list):
    self.tag_rules = tag_rules
    self.group_rules = group_rules
    self.group_list = group_list

  def validate_all(self, tagset):
    reasons = []
    for tagrule in self.tag_rules:
      if not tagrule.meets_requirements(tagset):
        reasons.append(TagFailure("requires", tagrule.tag, tagrule.requires))
      if not tagrule.no_conflicts(tagset):
        reasons.append(TagFailure("conflicts", tagrule.tag, tagrule.conflicts))
    for grouprule in self.group_rules:
      if not grouprule.meets_requirements(tagset):
        reasons.append(GroupFailure("requires", grouprule.group, grouprule.tag_requires, grouprule.group_requires))
      if not grouprule.no_conflicts(tagset):
        reasons.append(GroupFailure("conflicts", grouprule.group, grouprule.tag_conflicts, grouprule.group_conflicts))
    return not reasons, reasons
