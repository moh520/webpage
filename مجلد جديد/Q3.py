import json
person = {}
person = {"name":"mouhammed",
          "address":"tartous",
          "age":"40",
          "jop":"doctor",
          "marrid":"yes",
          "email_id":"None",
          "phone":"25487",
          "hoppy":"drawing",
          "children":"2",
          "workplace":"in hospital"
}
person2 = json.dumps (person)
print (person2)

