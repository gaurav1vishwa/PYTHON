import math_module;  # user defined module;

# In-built module
import math;
import random; 
import json;

print(math_module.add(30,20));
print(math_module.sub(40,20));

print(math.pi);
print(math.sqrt(3));

print(random.randint(1,10));
print(random.random());
print(random.randint(1000,100000));

import json

student = {
    "name": "Gaurav",
    "age": 22,
    "marks": 85
}

json_data = json.dumps(student)

print(json_data)
print(type(json_data));

print(f"{math.pi:.2f}");
