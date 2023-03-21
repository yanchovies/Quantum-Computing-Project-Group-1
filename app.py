from flask import Flask,render_template,request,url_for
import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
from shor import shors_algorithm
from grover_sparse import grovers_algorithm




    
    



app = Flask(__name__)

#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0




@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        n = request.form.get('qubit')
        k = request.form.get('target')
        n = int(n)
        k = int(k)
        found, amplitude = grovers_algorithm(n,k)
        
        if amplitude == "none":
            send_found = "The target state was not found"
        else:
        
            send_found = "The probability of finding the taget state " + str(found) + " is " + str(amplitude)
        

        return render_template('results.html', send_found = send_found)
    else:
        return render_template('home.html')
        
    


@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/shors', methods=['POST','GET'])
def shors():
    if request.method == 'POST':
        
        k = request.form.get('target')
        k = int(k)
        factor1, factor2 = shors_algorithm(k)
        factor_msg = "The factors of " + str(k) + " are: " + str(factor1) + ", " + str(factor2)

        return render_template('shor_factor.html', factor_msg = factor_msg)
    
    else:
        return render_template('shors.html')


        
    
    
    
if __name__ == '__main__':
    app.run(debug =True)



