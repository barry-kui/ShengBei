import pygame

class TButton:
    NORMAL = 0
    MOVE = 1
    DOWN = 2

    def __init__(self, x, y, text, imgNormal, imgMove=None, imgDown=None, callBackFunc=None, font=None, rgb=(0, 0, 0)):

        self.imgs = []
        if not imgNormal:
            raise Exception("请设置普通状态的图片")
        self.imgs.append(imgNormal)  # 普通状态显示的图片
        self.imgs.append(imgMove)  # 被选中时显示的图片
        self.imgs.append(imgDown)  # 被按下时的图片
        for i in range(2, 0, -1):
            if not self.imgs[i]:
                self.imgs[i] = self.imgs[i - 1]

        self.callBackFunc = callBackFunc
        self.status = TButton.NORMAL
        self.x = x
        self.y = y
        self.w = imgNormal.get_width()
        self.h = imgNormal.get_height()
        self.text = text
        self.font = font
        self.textSuf = font.render(self.text, True, rgb)

    def draw(self, destSuf):
        dx = (self.w / 2) - (self.textSuf.get_width() / 2)
        dy = (self.h / 2) - (self.textSuf.get_height() / 2)

        if self.imgs[self.status]:
            destSuf.blit(self.imgs[self.status], [self.x, self.y])
        destSuf.blit(self.textSuf, [self.x + dx, self.y + dy])

    def colli(self, x, y):
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        else:
            return False

    def getFocus(self, x, y):
        if self.status == TButton.DOWN:
            return
        if self.colli(x, y):
            self.status = TButton.MOVE
        else:
            self.status = TButton.NORMAL

    def mouseDown(self, x, y):
        if self.colli(x, y):
            self.status = TButton.DOWN

    def mouseUp(self, x, y):
        if self.colli(x, y):
            self.status = TButton.MOVE
            if self.callBackFunc:
                surface = pygame.display.get_surface()
                return self.callBackFunc()
        else:
            self.status = TButton.NORMAL
            return