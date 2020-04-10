import tag_guard 

tag1 = tag_guard.Tag("ontokinetic")
tag2 = tag_guard.Tag("humanoid")
tag3 = tag_guard.Tag("goi-format")
tag4 = tag_guard.Tag("supplement")
tag5 = tag_guard.Tag("_cc")

test_set = tag_guard.TagSet(tag1, tag2, tag3, tag4, tag5)
print("Contents of test_set: " + test_set)

print("Check if tag in tagset: " + ("supplement" in test_set))