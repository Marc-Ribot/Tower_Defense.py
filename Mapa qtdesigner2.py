from PIL import Image

# Carga la imagen del mapa
image_path = r"C:\Users\mribo\OneDrive\Documents\6è quadri\Tower_Defense.py\1.jpg"

image = Image.open(image_path)

# Convierte la imagen a escala de grises
image_gray = image.convert("L")

# Obtén las dimensiones de la imagen
width, height = image_gray.size

# Define el tamaño deseado de la matriz
desired_width = 37
desired_height = 24

# Calcula los factores de escala para redimensionar la imagen
scale_x = width // desired_width
scale_y = height // desired_height

# Redimensiona la imagen para que se ajuste al tamaño deseado
resized_image = image_gray.resize((desired_width * scale_x, desired_height * scale_y))

# Obtiene los píxeles de la imagen redimensionada en forma de matriz
pixel_matrix = list(resized_image.getdata())

# Crea una matriz vacía para almacenar los valores del mapa
map_matrix = []

# Itera sobre los píxeles y asigna valores numéricos o símbolos según el umbral
for i in range(desired_height):
    row = []
    for j in range(desired_width):
        pixel_value = pixel_matrix[i * desired_width * scale_y + j * scale_x]
        # Define un umbral para separar el camino del resto del mapa
        threshold = 128
        if pixel_value < threshold:
            # Asigna un valor representativo del camino
            row.append(1)  # Puedes utilizar cualquier número o símbolo que desees para representar el camino
        else:
            # Asigna un valor representativo del resto del mapa
            row.append(0)  # Puedes utilizar otro número o símbolo para representar otras áreas del mapa
    map_matrix.append(row)

# Ahora tienes la matriz 'map_matrix' que representa el mapa con el camino marcado

# Puedes imprimir la matriz para verificar los valores asignados
for row in map_matrix:
    print(row)
