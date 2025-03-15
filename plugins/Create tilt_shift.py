from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

PLUGIN_NOME = "Tilt Shift"
PLUGIN_ICONE = "📷"

def aplicar(imagem):
    largura, altura = imagem.size

    img_blur = imagem.filter(ImageFilter.GaussianBlur(radius=12))
    mask = Image.new("L", (largura, altura), 0)
    draw = ImageDraw.Draw(mask)

    faixa_central = altura // 3
    faixa_inicio = (altura - faixa_central) // 2
    faixa_fim = faixa_inicio + faixa_central

    for y in range(altura):
        if y < faixa_inicio:
            fade = int((y / faixa_inicio) * 255)
        elif y > faixa_fim:
            fade = int(((altura - y) / (altura - faixa_fim)) * 255)
        else:
            fade = 255
        draw.line([(0, y), (largura, y)], fill=fade)

    imagem_editada = Image.composite(imagem, img_blur, mask)

    enhancer = ImageEnhance.Color(imagem_editada)
    return enhancer.enhance(1.7)