from PIL import Image

# Abrir imagen original
img = Image.open('perfil.jpeg').convert('RGBA')

# Umbral para considerar como blanco (0-255)
threshold = 245

# Procesar píxeles
datas = img.getdata()
newData = []
for item in datas:
    r, g, b, a = item
    if r >= threshold and g >= threshold and b >= threshold:
        # Hacer transparente
        newData.append((255, 255, 255, 0))
    else:
        newData.append((r, g, b, a))

img.putdata(newData)
img.save('perfil.png')
print('Saved perfil.png')
