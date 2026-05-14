# Actividad 3: Gestión de Lista de Reproducción Musical

# 1) Crea una lista con 5 canciones (nombres)
playlist = ["Canción 1","Canción 2","Canción 3","Canción 4","Canción 5"]

# Mostrar estado inicial
print("Lista inicial:", playlist)

# 2) Aplica los métodos en orden y muestra el estado después de cada uno
playlist.append("Bonus Track 1")
print("\nDespués de append('Bonus Track 1'):", playlist)

playlist.insert(2, "Bonus Track 2")
print("\nDespués de insert(2, 'Bonus Track 2'):", playlist)

# c) extend con otra canción en la siguiente posición
playlist.extend(["Bonus Track 3"])
print("\nDespués de extend(['Bonus Track 3']):", playlist)

# d) remove('Bonus Track 2') para eliminar una canción por su nombre
playlist.remove("Bonus Track 2")
print("\nDespués de remove('Bonus Track 2'):", playlist)

# e) pop() para eliminar la última canción
eliminada = playlist.pop()
print("\nEliminada con pop() (última):", eliminada)
print("Después de pop():", playlist)

# f) reverse() para invertir la lista
playlist.reverse()
print("\nDespués de reverse():", playlist)

# 5) Responder preguntas usando métodos de lista
print("\n--- Respuestas ---")

# ¿Cuántas canciones tiene la playlist?
print("¿Cuántas canciones tiene la playlist?", len(playlist))

# ¿En qué posición está la primera canción que agregaste?
# La primera que agregaste fue "Bonus Track 1"
pos_primera = playlist.index("Bonus Track 1")
print("¿En qué posición está 'Bonus Track 1'?", pos_primera)

# ¿Cuántas veces aparece el string 'Bonus Track 1'?
# r// aparece una vez solamente porque se agrego una sola vez, y no se ha eliminado
veces = playlist.count("Bonus Track 1")
print("¿Cuántas veces aparece 'Bonus Track 1'?", veces)
