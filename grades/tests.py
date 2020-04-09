from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import course
from django.contrib.auth.models import User
from .views import IndexView
# Create your tests here.

def create_course(course_text):
    return course.objects.create(course_name = course_text)

def create_course_with_user(course_text,user):
    return course.objects.create(course_name = course_text, owner = user)


class CourseTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username = 'test')
        self.user2 = User.objects.create_user(username = 'loser')

    def test_no_course(self):
        request = self.factory.get('/grades')
        request.user = self.user2
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            []
        )

    def test_add_grade(self):
        create_course_with_user('course', self.user)
        request = self.factory.get('/grades')
        request.user = self.user
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            ['<course: course>']
        )

    def test_add_course_null(self):
        create_course_with_user('', self.user)
        request = self.factory.get('/grades')
        request.user = self.user
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            ['<course: >']
        )
    def test_add_course_2(self):
        create_course_with_user('course1', self.user2)
        request = self.factory.get('/grades')
        request.user = self.user2
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            ['<course: course1>']
        )
    def test_authentication(self):
        request = self.factory.get('/grades')
        request.user = self.user2
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            []
        )

class usertests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username = 'test')
        self.user2 = User.objects.create_user(username = 'loser')

    def test_user_grade(self):
        create_course_with_user('user_owned', self.user)
        request = self.factory.get('/grades')
        request.user = self.user
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            ['<course: user_owned>']
        )

    def test_dont_see_other_grades(self):
        create_course_with_user('user_owned', self.user)
        request = self.factory.get('/grades')
        request.user = self.user2
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertQuerysetEqual(
            context,
            []
        )

def create_ass_type(cours, ass_typ, grade_percentag):
    return ass_type.objects.create(course = cours, ass_type = ass_typ, grade_percentage = grade_percentag)
def create_ass(ass_typ, ass_nam, cours, grad):
    return assignment.objects.create(course = cours, ass_type = ass_typ, ass_name=ass_nam, grade = grad)

class gradeCalculationTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username = 'test')
    def test_percentbased(self):
        create_course_with_user('course1', self.user)
        create_ass_type('<course: course1>', 'hw', 60)
        create_ass_type('<course: course1>', 'midterm', 20)
        create_ass_type('<course: course1>', 'final', 20)
        create_ass('hw', 'hw0', '<course: course1>', 100)
        create_ass('hw', 'hw1', '<course: course1>', 85)
        create_ass('hw', 'hw2', '<course: course1>', 90)
        create_ass('midterm', 'midterm', '<course: course1>', 88)
        create_ass('final', 'final', '<course: course1>', 90)

        request = self.factory.get('/grades/course/1/')
        request.user = self.user
        
        view = IndexView()
        view.setup(request=request)
        context = view.get_queryset()
        self.assertEquals(indCourse.course_grade, 90.6)
      