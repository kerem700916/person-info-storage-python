import pandas, json

class person():
    def __init__(self, name, age, sex, country, dad_name, mom_name, job, email):
        global data_frame
        self.name = name
        self.age = age
        self.sex = sex
        self.country = country
        self.dad_name = dad_name
        self.mom_name = mom_name
        self.job = job
        self.email = email
        data_frame = pandas.DataFrame(
            ['name', 'age','sex', 'country', 'dad_name', 'mom_name', 'job', 'email'],
            [name, age, sex, country, dad_name, mom_name, job, email]
        )
        file_name = self.name + '.json'
        file = open(file_name, 'a')
        file_read = open(file_name, 'r')
        content = file_read.read()
        file.truncate(0)
        string = '''{
    "'''+self.name+'''": [
        {
            "name":"'''+self.name+'''",
            "age":"'''+self.age+'''",
            "sex":"'''+self.sex+'''",
            "country":"'''+self.country+'''",
            "dad_name":"'''+self.dad_name+'''",
            "mom_name":"'''+self.mom_name+'''",
            "job":"'''+self.job+'''",
            "email":"'''+self.email+'''"
        }
    ]
}\n'''
        file.write(string)
        file.close()

def get_info(name):
    info = []
    with open(name+'.json') as json_file:
        data = json.load(json_file)
    for d in data[name]:
        info.append(d)
    return info
