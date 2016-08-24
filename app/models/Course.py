"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()


    def get_courses(self):
        query = "SELECT * from courses"
        return self.db.query_db(query)

    def get_course_by_id(self, course_id):
        query = "SELECT * from courses where id = :course_id"
        data = {'course_id': course_id}
        return self.db.query_db(query, data)

    def add_course(self, course):
        query = "INSERT into courses (title, description, created_at) values(:title, :description, NOW())"
        data = { 'title': course['title'], 'description': course['description'] }
        return self.db.query_db(query, data)
        return True

    def update_course(self, course):
        query = "UPDATE courses SET title= :title, description= :description WHERE id= :course_id"
        data = {'title': course['title'], 'description': course['description'], 'course_id': course['id']}
        return self.db.query_db(query, data)

    def destroy(self, course_id):
        query = "DELETE FROM courses WHERE id =:course_id"
        data = {"course_id": course_id}
        return self.db.query_db(query, data)
