pavel = {
"name" : "pavel" ,
"age" : 22 ,
"children" : [{
"name" : "masha" ,
"age" : 21 ,
}, {
"name" : "victoria" ,
"age" : 10 ,
}],
}
darja = {
"name" : "natalia" ,
"age" : 41 ,
"children" : [{
"name" : "kirill" ,
"age" : 11 ,
}, {
"name" : "pavel" ,
"age" : 15 ,
}],
}
emps = [pavel , darja]

def check(data):
  flag = False
  for i in data:
    if i['age'] > 18:
      flag = True
  return flag

def test(emps):
  for i in emps:
    if check(i['children']):
      print(i['name'])

test(emps)