class Auto():
    def __init__(self, idTipoAuto, marca, modelo, descripcion, precioUnitario, cantidad, imagen):
        self.idTipoAuto = idTipoAuto
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precioUnitario = precioUnitario
        self.cantidad = cantidad
        self.imagen = imagen

    def __str__(self):
        return f'ID: {self.idTipoAuto} - Marca: {self.marca} - Modelo: {self.modelo} - Descripción: {self.descripcion} - Precio Unitario: {self.precioUnitario} - Cantidad: {self.cantidad} - Imagen: {self.imagen}'