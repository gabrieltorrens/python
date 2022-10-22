import xml.dom.minidom

doc = xml.dom.minidom.parse("samplexml.xml")

print(doc.nodeName)
print(doc.firstChild.tagName)

skills = doc.getElementsByTagName("skill")
print(skills.length)
for i in skills:
    print(i.getAttribute("name"))

newSkill = doc.createElement("skill")
newSkill.setAttribute("name", "jQ")
doc.firstChild.appendChild(newSkill)
skills = doc.getElementsByTagName("skill")
print(skills.length)

for i in skills:
    print (i.getAttribute("name"))
skills = doc.getElementsByTagName("skill")
