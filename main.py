from flask import Flask, render_template, request, redirect, url_for, flash
from Autos import Auto

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar flash messages

autos = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def loginDatos():
    usuario = request.form['user']
    contrasena = request.form['password']

    if usuario == 'empleado' and contrasena == '$uper4utos#':
        return redirect(url_for('inicio'))
    else:
        flash('El usuario o contraseña son incorrectas', 'error')
        return redirect(url_for('login'))

@app.route('/inicio')
def inicio():
    return render_template('inicio.html', listado = autos)

@app.route('/registro')
def registro():
    return render_template('registro.html')

# Ruta para manejar la eliminación de un auto
@app.route('/eliminar', methods=['POST'])
def eliminar_auto():
    idEliminar = request.form['idEliminar']
    global autos
    # Filtramos la lista para eliminar el auto con el ID correspondiente
    for auto in autos:
        if auto.idTipoAuto == idEliminar:
            autos.remove(auto)
            flash('Auto eliminado con éxito.', 'success')
            break
    return redirect(url_for('inicio'))

@app.route('/submit', methods=['POST'])
def submit():
    idTipoAuto = request.form['idTipoAuto']
    marca = request.form['marca']
    modelo = request.form['modelo']
    descripcion = request.form['descripcion']
    precioUnitario = request.form['precioUnitario']
    cantidad = request.form['cantidad']
    imagen = request.form['imagen']

    for auto in autos:
        if auto.idTipoAuto == idTipoAuto:
            flash('El auto con el ID ya existe. Intenta con otro ID.', 'error')
            return redirect(url_for('registro'))
    
    auto = Auto(idTipoAuto, marca, modelo, descripcion, precioUnitario, cantidad, imagen)
    autos.append(auto)
    
    flash('Auto registrado con éxito.', 'success')
    return redirect(url_for('registro'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
