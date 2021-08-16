input
```python
from person import person
jack = person(name='jack', age='20', sex='male', country='en', dad_name='mike', mom_name='helen', job='student', email='jackmail@gmail.com')
```
the output file named jack.json
```json
{
    "jack": [
        {
            "name":"jack",
            "age":"20",
            "sex":"male",
            "country":"en",
            "dad_name":"mike",
            "mom_name":"helen",
            "job":"student",
            "email":"jackmail@gmail.com"
        }
    ]
}
```
input
```python
from person import get_info
info = get_info(jack)
print(info)
```
output
```python
[{'name': 'jack', 'age': '20', 'sex': 'male', 'country': 'en', 'dad_name': 'mike', 'mom_name': 'helen', 'job': 'student', 'email': 'jackmail@gmail.com'}]
```
