import unittest
from app import app,all_mahasiswa

class UnitTestMahasiswa(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        all_mahasiswa.clear()
    
    def test_get_all_mahasiswa(self):
        response = self.app.get('/mahasiswa')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'all_mahasiswa':[]})
    
    def test_add_mahasiswa_success(self):
        mahasiswa_data = {'nama': 'Fauzan', 'nim': '123456', 'umur': 21}
        response = self.app.post('/mahasiswa', json=mahasiswa_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'],'berhasil menambahkan')

        self.assertEqual(len(all_mahasiswa), 1)
        self.assertEqual(all_mahasiswa[0], mahasiswa_data)
    
    def test_add_mahasiwa_failed(self):
        mahasiswa_data = {}
        response = self.app.post('/mahasiswa',json=mahasiswa_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'bad request')
        self.assertEqual(response.json['message'],'nama, nim, umur harus ada')
        self.assertEqual(len(all_mahasiswa), 0)



if __name__ == '__main__':
    unittest.main()