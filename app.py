
from flask import Flask,render_template,request,url_for
import objects.matrices.matrix as mat
import objects.matrices.matrixElement as matEl
from shor import shors_algorithm
from grover_sparse import grovers_algorithm




    
    



app = Flask(__name__)
app.config['STATIC_URL_PATH'] = '/static'
app.config['STATIC_FOLDER'] = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0




@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        n = request.form.get('inputGroupSelect01')
        k = request.form.get('target')
        n = int(n)
        k = int(k)
        found = grovers_algorithm(n,k)
        

        return render_template('results.html', found = found)
    else:
        return render_template('home.html')
        
    


@app.route('/results')
def results():
    return render_template('results.html')
        
    
    
    
if __name__ == '__main__':
    app.run(debug =True)



