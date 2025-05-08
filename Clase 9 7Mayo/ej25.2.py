def construir_perfil(nombre,apellido,**info_usuario):
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario

perfil_usuario = construir_perfil('Julieta', 'Rossney', edad=16, ciudad='CABA')
print(perfil_usuario)
