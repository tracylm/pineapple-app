from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders



class GeneralTests(TestCase):
    def test_serving_static_files(self):
        result = finders.find('images/pineapple.jpg')
        self.assertIsNotNone(result)


'''
class IndexPageTests(TestCase):

    def test_index_contains_hello_message(self):
        # Check if there's a message 'Pineapple Says'

        response = self.client.get(reverse('index'))
        self.assertIn(b'Pineapple says', response.content)

    def test_index_using_template(self):
        # Check template used to render index page

        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'pineapple/index.html')

    def test_pineapple_picture_displayed(self):
        # Check if there is an image 'pineapple.jpg' on the index page

        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/pineapple.jpg"', response.content)

    def test_index_has_title(self):
        # Check to make sure title tag has been used
        # And that template contains HTML from Chapter 4
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'<title>', response.content)


class AboutPageTests(TestCase):

    def test_about_contains_create_message(self):
        # Check if the about page is there and contains the specified message

        response = self.client.get(reverse('about'))
        # self.assertIn(b'This tutorial has been put together by' in str(response.content))
        self.assertIn('This tutorial has been put together by', (response.content))


    def test_about_contain_image(self):
        # Check if there is an image on the about page

        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media"', response.content)

    def test_about_using_templates(self):
        # Check the template used to render index page

        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'pineapple/about.html')



class ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_pineapple import populate
            populate()
        except ImportError:
            print('The module populate_pineapple does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate function :(')


    def get_category(self, name):

        from pineapple.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)


class Chapter4ViewTest(TestCase):
    def test_index_contains_hello_message(self):
        # Check if there is the message 'hello world'
        response = self.client.get(reverse('index'))
        self.assertIn('Pineapple says', response.content)

    def test_does_index_contain_img(self):
        # Check if the index page contains an img
        response = self.client.get(reverse('index'))
        self.assertIn('img', response.content)

    def test_about_using_template(self):
        # Check the template used to render index page

        response = self.client.get(reverse('about'))

        self.assertTemplateUsed(response, 'pineapple/about.html')

    def test_does_about_contain_img(self):
        # Check if the about page contains an image
        response = self.client.get(reverse('about'))
        self.assertIn('img', response.content)

    def test_about_contains_create_message(self):
        # Check if the about page contains the message from the exercise
        response = self.client.get(reverse('about'))
        self.assertIn('This tutorial has been put together by', response.content)


class Chapter5ViewTests(TestCase):

    def setUp(self):
        try:
            from populate_pineapple import populate
            populate()
        except ImportError:
            print('The module populate_pineapple does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :(')


    def get_category(self, name):

        from pineapple.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')

        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)

    def test_view_has_title(self):
        response = self.client.get(reverse('index'))

        # Check title used correctly
        self.assertIn('<title>', response.content)
        self.assertIn('<title>', response.content)

    # Need to add tests to:
    # check admin interface - is it configured and set up?

    def test_admin_interface_page_view(self):
        from admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)


class Chapter6ViewTests(TestCase):

    def setUp(self):
        try:
            from populate_pineapple import populate
            populate()
        except ImportError:
            print('The module populate_pineapple does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :)')


    # are categories displayed on index page?

    # does the category modle have a slug field?


    # test the slug field work ...
    def test_does_slug_field_work(self):
        from pineapple.models import Category
        cat = Category(name='How do I create a slug in Django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')

    # test category view - does the page exist?


    # test whether you can navigate from index to a category page


    # test whether the index page contains top five pages

    # test whether index page contains "most liked" and "most viewed"

    # test whether category page contains a link back to index page


class Chapter7ViewTests(TestCase):

    def setUp(self):
        try:
            from forms import PageForm
            from forms import CategoryForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something went wrong with the Chapter 7 View Tests')

    pass
    # test whether there is a PageForm in pineapple.forms

    # test whether there is a CategoryForm in  pineapple.form

    # test whether there is an add page view

    # test whether there is a category page


    # test if index contains a link to add category page
    #<a href="/pineapple/add_category/">Add a New Category</a><br />


    # test if the add_page.html template exists
    '''
