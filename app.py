from flask import Flask, request, jsonify

app = Flask(__name__)

#dummy database
all_mahasiswa = []

@app.route('/mahasiswa',methods=['GET'])
def get_all_mahasiswa():
    return jsonify({'all_mahasiswa':all_mahasiswa}),200

@app.route('/mahasiswa',methods=['POST'])
def add_mahasiswa():
    data = request.get_json()
    if not all(key in data for key in ['nama','nim','umur']):
        return jsonify({'error':'bad request','message':'nama, nim, umur harus ada'}),400
        
    mahasiswa = {
        'nama':data['nama'],
        'nim': data['nim'],
        'umur':data['umur']
    }

    all_mahasiswa.append(mahasiswa)
    return jsonify({'message':'berhasil menambahkan'}),201

if __name__ == '__main__':
    app.run(debug=True)
