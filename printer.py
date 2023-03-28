from PIL import ImageGrab

# Define as dimensões da imagem que você deseja capturar
width = 1024
height = 500

# Obtém as dimensões da tela
screen_width, screen_height = ImageGrab.grab().size

# Calcula as coordenadas de início e fim para capturar a área desejada
start_x = (screen_width - width) // 2
start_y = (screen_height - height) // 2
end_x = start_x + width
end_y = start_y + height

# Captura a imagem da tela na área especificada
img = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

# Salva a imagem capturada em um arquivo
img.save("centro_da_tela.png")
