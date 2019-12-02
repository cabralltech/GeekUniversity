class Televisao:
    def __init__(self, volume, canais):
        self.volume = [x for x in range(volume)]
        self.canais = [y for y in range(canais)]


class ControleRemoto:
    def __init__(self, tv, canal, volume):
        self.tv = tv
        self._canal = canal
        self._volume = volume

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, channel):
        self._canal = channel

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, vol):
        self._volume = vol

    def aumentar_canal(self):
        if self._canal < len(self.tv.canais):
            self._canal += 1
        else:
            print('Canal inexistente')

    def diminuir_canal(self):
        if self._canal > 0:
            self._canal -= 1
        else:
            print('Canal inexistente')

    def aumentar_vol(self):
        if self._volume < len(self.tv.volume):
            self._volume += 1
        else:
            print('Volume no máximo')

    def diminuir_vol(self):
        if self._volume > 0:
            self._volume -= 1
        else:
            print('Volume no mínimo')
