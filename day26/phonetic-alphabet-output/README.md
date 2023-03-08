## List comprehension

Creating a list from a list

This was previously done with a for loop like

```python
numbers = [1, 2, 3]
new_list = []
for n in numbers:
	add_1 = n + 1
	new_list.append(add_1)
```

List comprehension example that does the same thing

```python
new_list = [n + 1 for n in numbers]

keyword method
new_list = [new_item for item in list]

>>> numbers = [1,2,3]
>>> new_numbers = [num + 1 for num in numbers]
>>> new_numbers
[2, 3, 4]
```

You can also work with strings

```python
name = "Andrew"
new_list = [letter for letter in name]
>>> new_list
['A', 'n', 'd', 'r', 'e', 'w']


>>> new_range = [num * 2 for num in range(1, 5)]
>>> new_range
[2, 4, 6, 8]
```

## Conditional List Comprehension
```python
new_list = [new_item for item in list if test]          # "if test" is the only added syntax

>>> names
['Alex', 'Drew', 'Beth', 'Dave', 'Elaenor', 'Caroline']
>>> short_names = [name for name in names if len(name) < 5 ]
>>> short_names
['Alex', 'Drew', 'Beth', 'Dave']

>>> upper_names = [name.upper() for name in names if len(name) > 4 ]
>>> upper_names
['ELAENOR', 'CAROLINE']
```

## Dictionary Comprehension
Create a new dictionary from values in a list or previous dictionary 
```python
new_dict = {new_key:new_value for item in list}

>>> names = ['Alex', 'Drew', 'Beth', 'Dave', 'Elaenor', 'Caroline']
students_scores = {Student:random.randint(1, 100) for student in names}
>>> students_scores
{'Alex': 47, 'Drew': 3, 'Beth': 28, 'Dave': 73, 'Elaenor': 82, 'Caroline': 81}

# Creates new dictionary based on values in previous dictionary 
new_dict = {new_key:new_value for (key, value) in dict.items()}
```

## Conditional Dictionary Comprehension 
```python
new_dict = {new_key:new_value for (key, value) in dict.items() if test}

>>> students_scores
{'Alex': 47, 'Drew': 3, 'Beth': 28, 'Dave': 73, 'Elaenor': 82, 'Caroline': 81}

>>> passed_student = {student:score for (student, score) in students_scores.items() if score >= 60}
>>> passed_student
{'Dave': 73, 'Elaenor': 82, 'Caroline': 81}
```

## How to Iterate over a Pandas DataFrame
```python

import pandas

student_data_frame =  pandas.DataFrame(student_dict)
print(student_data_frame)
    
# Loop Through a data Frame
for (key, value) in student_data_frame.items():
    print(value)
    
# Loop Through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
```