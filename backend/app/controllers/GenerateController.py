from flask import jsonify, request

def GenSegitiga():
    try:
        angka = int(request.json.get('angka'))
        angka_str = str(angka)
        jumlah_digit = len(angka_str)
        segitiga = []
        for i in range(jumlah_digit, 0, -1):
            data = angka_str[-i]
            segitiga.append(data)
        
        segitiga = [f'{i}0' if i.isdigit() and int(i) < 10 else i for i in segitiga]
       
        return jsonify({'segitiga': segitiga})
    except Exception as e:
        print(e)
        
def GenPrima():
    try:
        angka = request.json.get('angka')
        if angka >= 2:
            primes = []
            for num in range(2, angka + 1):
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)

            return jsonify({'angka': primes})
    except Exception as e:
        print(e)
        
def GenGanjil():
    try:
        angka = request.json.get('angka')
        if angka >= 1:
            ganjil = []
            for num in range(1, angka + 1):
                if num % 2 != 0:
                    ganjil.append(num)
                    
            return jsonify({'angka': ganjil})
    except Exception as e:
        print(e)