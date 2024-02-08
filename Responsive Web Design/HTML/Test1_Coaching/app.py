from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    nombre = ''
    email = ''
    numero = ''
    liga = ''
    linea = ''
    condicion_1 = ''
    condicion_2 = ''
    bio = ''
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        email = request.form.get('email', '')
        numero = request.form.get('numero', '')
        liga = request.form.get('liga', '')
        linea = request.form.get('lane', '')
        condicion_1 = 'Checkbox1' if 'condicion_1' in request.form else ''
        condicion_2 = 'Checkbox2' if 'condicion_2' in request.form else ''
        bio = request.form.get('bio', '')
        print(nombre)
        
        # Puedes hacer lo que quieras con los datos aquí
        # Por ahora, simplemente los pasaré a la plantilla
        return render_template('formulario.html', nombre=nombre, email=email, numero=numero,
                               liga=liga, linea=linea, condicion_1=condicion_1,
                               condicion_2=condicion_2, bio=bio)

    # Si la solicitud es GET, simplemente renderiza la plantilla
    
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)

