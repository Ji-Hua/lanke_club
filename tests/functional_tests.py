import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_visit_the_website_and_do_staff(self):
        # Lucy heard about a cool website that could host a werewolf game
        # She checked the website
        self.browser.get('http://localhost:8000')
        # She noticed that this website has been named `烂柯游艺社`
        # in both title and header
        self.assertIn('烂柯游艺社', self.browser.title)
        self.fail('Fail on purpose, should remove this when finished')

        # She want to login to the website but find she needs
        # to register first


        # She has logged in and is able to create a game


        # She also could join the game created by others by the id


        # Lucy forgets the password somehow
        # and she wants to reset the password by email


        # She received the email and then she use the link to reset her password

        # She is satisfied

if __name__ == '__main__':
    unittest.main(warnings='ignore')