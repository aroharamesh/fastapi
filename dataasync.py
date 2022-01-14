# Databases and Asynchronous ORMs


# An overview of relational and NoSQL databases
# Communicating with a SQL database with SQLAlchemy
# Communicating with a SQL database with Tortoise ORM
# Communicating with a MongoDB database using Motor


# relational 


# tables, rows, columns 

# student
# id  name    city
# 1   ramesh  bangalore
# 2   jeffrey bangalore
# 3   rajeshwari  bangalore
# 4   lakshay bangalore

# courses
# id  name        description
# 1   fastapi     dfskas
# 2   python      sdlkjf
# 3   react       lhjkdsf

# M : M

# 1 student: M courses
# 1 course: M students

# student_courses
# stud_id course_id
# 1   2
# 2   3
# 1   2

# select b.name, c.description from student_courses a, student b, courses c 
# where a.stud_id = b.id and a.course_id = c.id and b.name like 'ramesh'


# # NoSQL

# # JSON Object 

# # collections, documents, attributes/fields
# # Document -->
# student = {
#     "_id": 1,
#     "name": "Ramesh",
#     "city": "Bangalore"
# }

# # collection ->
# student = [{
#     "_id": 1,
#     "name": "Ramesh",
#     "city": "Bangalore",
#     "course": {
#         "id": "1",
#         "name": "fastapi"
#     }
# },
# {
#     "_id": 2,
#     "name": "jeffrey",
#     "city": "Bangalore"
# }
# ]


#-----------------------------------------------------
# Communicating with a SQL database with SQLAlchemy

# https://www.encode.io/databases/


# pip install databases
# pip install databases[sqlite]



