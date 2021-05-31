from .test_setup import Testsetup
import pdb
from rest_framework import status

class TestView(Testsetup):

    def test_movie_post(self):
        res = self.client.post(self.list_url, self.user_data, format="json")
        #pdb.set_trace()
        self.assertEqual(res.data['Name'] , self.user_data['Name'])
        self.assertEqual(res.data['Description'] , self.user_data['Description'])
        self.assertEqual(res.status_code,201)
    def test_movie_get(self):
        res = self.client.get(self.list_url, self.user_data, format="json")
        self.assertEqual(res.status_code,200)

    def test_get_by_id(self):
        response = self.client.get('/api/movie/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(json.loads(response.content), {'id': 1, 'Name': 'Baghban'})

    def test_delete_by_id(self):
        response = self.client.delete('/api/movie/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

