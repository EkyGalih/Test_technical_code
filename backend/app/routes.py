from app import app
from app.controllers import GenerateController

@app.route('/')
def index():
    return "tes page"


@app.route('/segitiga', methods=['POST'])
def segitiga():
    return GenerateController.GenSegitiga()

@app.route('/prima', methods=['POST'])
def Prima():
    return GenerateController.GenPrima()

@app.route('/ganjil', methods=['POST'])
def Ganjil():
    return GenerateController.GenGanjil()