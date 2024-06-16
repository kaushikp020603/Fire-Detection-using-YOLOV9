from roboflow import Roboflow
rf = Roboflow(api_key="pushUxcO4QD23l8yStGo")
project = rf.workspace().project("fire-ql2gq")
model=project.version(1).model



model.predict("a.jpg", confidence=20).save("b.jpg")






