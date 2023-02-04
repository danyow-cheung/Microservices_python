import c3_tests
import unittest
from unittest import mock 
import requests_mock

class TestHeroCode(unittest.TestCase):
    def setUp(self):
        self.fake_heros = {
            'members':[
                {"name":"Age 20 Hero","age":20},
                {"name":"Age 30 Hero","age":30},
                {"name":"Age 40 Hero","age":40},
                
            ]
        }
    
    def test_get_hero_names_age_filter(self):
        result = list(c3_tests.get_hero_namesz_v2(
            self.fake_heros,filter= lambda x:x.get('age',0)>30
        ))
        self.assertEqual(result,[{'name':'Age 40 Hero','age':40}])

    @requests_mock.mock()
    def test_display_heroes_over(self,mocker):
        mocker.get(requests_mock.ANY,json=self.fake_heros)
        rendered_text = c3_tests.render_hero_message(age=30)
        self.assertEqual(rendered_text,'Age 40 Hero is over 30\n')
if __name__=='__main__':
    unittest.main()
