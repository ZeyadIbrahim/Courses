"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        print "$$$$$$$$$"
        courses = self.models['Course'].get_courses()
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        print "in add course function"
        course_id= self.models['Course'].add_course(request.form)
        return redirect ('/')

    def confirm_delete(self, id):
        print id
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('remove.html', course=course[0])

    def destroy(self, id):
        print "Destroying"
        print id
        self.models['Course'].destroy(id)
        return redirect ('/')

    def update(self, id):
        print id
        self.models['Course'].update_course(id)
        return self.load_view
