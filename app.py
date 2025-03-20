from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Define the buttons with their values and labels
    buttons = [
        {"text": "ruger LCP 2 mags(500usd)", "value": 500},
        {"text": "bersa 223da(350usd)", "value": 350},
        {"text": "bersa 383da(380usd)", "value": 380},
        {"text": "bersa bp9cc 2 mags(450usd)", "value": 450},
        {"text": "ballester 22 2 mags(700usd)", "value": 700},
        {"text": "colt government(1300usd)", "value": 1300},
        {"text": "taurus g3(500usd)", "value": 500},
        {"text": "taurus g3c(500usd)", "value": 500},
        {"text": "weinrauch cowboy(1600usd)", "value": 1600},
        {"text": "taurus 65(650usd)", "value": 650},
        {"text": "smith wesson 469(600usd)", "value": 600},
        {"text": "glock 17 fiber 3 mags(1000usd) ", "value": 1000},
        {"text": "glock 19 tritium 2 mags(1000usd) ", "value": 1000},
        {"text": "smith victory 4 mags(1300usd) ", "value": 1300},
        {"text": "sig p320 x-vtac(1500usd) ", "value": 1500},
        {"text": "tanfoglio force 45(600usd) ", "value": 600},
        {"text": "erma kgp69(450usd)", "value": 450}, 
        {"text": "high standard pump (550usd)", "value": 550},
        {"text": "smith fpc9(1350usd) ", "value": 1350},
        {"text": "smith 15-22 3 mags(1400usd) ", "value": 1400},
        {"text": "ruger 10-22 double mag(650usd)", "value": 650},
        {"text": "ruger custom shop triple mag(1500usd)", "value": 1500},
        {"text": "rossi 775(650usd)", "value": 650},
        {"text": "ruger american rimfire double mag(1650usd)", "value": 1650},
        {"text": "kusa kp9 1 mag(3500usd)", "value": 3500},
        {"text": "hunt group mh-ts12(850usd)", "value": 850},  
        {"text": "remington 870(1300usd)", "value": 1300},
       
    ]
    return render_template('index.html', buttons=buttons)

if __name__ == '__main__':
    app.run(debug=True)
