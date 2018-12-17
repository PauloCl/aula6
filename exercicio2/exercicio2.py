#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pygame import *
from sys import exit


def tela():
    tamanho = largura, altura = 800, 600

    janela = display.set_mode(tamanho)
    display.set_caption("Tela básica criada!")

    init()
    while True:
        for evento in event.get():
            if evento.type == QUIT:
                exit()
            elif evento.type == KEYDOWN and evento.key == K_ESCAPE:
                exit()

        display.flip()


if __name__ == '__main__':
    tela()
