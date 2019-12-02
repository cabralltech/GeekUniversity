def struct_ponto(v1, v2, p):
    if v1[0] <= p[0] <= v2[0] and v1[1] <= p[1] <= v2[1]:
        return 1
    return 0



esqx = int(input('Coordenada "x" do vértice inferior esquerdo o retângulo: '))
esqy = int(input('Coordenada "y" do vértice inferior esquedo do retângulo: '))
v_esq = (esqx, esqy)
dirx = int(input('Coordenada "x" do vértice superior direito do retângulo: '))
diry = int(input('Coordenada "y" do vértice superior direito do retângulo: '))
v_dir = (dirx, diry)
px = int(input('Coordenada "x" do ponto: '))
py = int(input('Coordanada "y" do ponto: '))
ponto = (px, py)
print(struct_ponto(v_esq, v_dir, ponto))
