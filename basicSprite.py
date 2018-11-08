""" basicSprite.py
   like a class - uses a sprite """
# pygame has a built-in Sprite object that is a useful template for your own sprites
# It's designed a s abase class you can build your own sprites with.
# The built in sprite object has some feature your other sprites will need.
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))


# the built-in sprite has 2 primary attributes: image and rect.  A common way to give a
# sprite an image is to use the pygame.images.load() function.  You may instead use any
# pygame surface object.

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Sprite objects almost always have at least 2 methods; __init__(seld) - acting as the
        # object constructor) AND update(self).  NOTE:This isn't truly a constructor, but think
        # of it as that for now and things will work.

        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 200
        self.dx = 10
        self.dy = 0

    # Note: pygame expects every sprite to have an images and rect attribute.  if not, you will get
    # an AttributeError exception, which you can handle.
    # the following common (and other) attributes are available; top, bottom, left, right, centerx,
    # centery, size, height, width, colliderect(rect2), collidepoint(point), inflate(x,y), and move(dx, dy)

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.rect.left = 0


def main():
    pygame.display.set_caption("basic sprite demo")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0, 0))  # not copying but blitting one time before loop begins, then
    # changing only the pixels that changed.( less overhead, better memory)

    box = Box()
    allSprites = pygame.sprite.Group(box)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        allSprites.clear(screen, background)  # special method - clears off all sprites drawn in previous frame
        # and replaces them iwith the appropriate part of the background.  clear needs a surfrace.
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip() # won't need to blit each surface (sprite now does that), vut will need to flip
        # the displayt to let pygame know you're ready to update the actual graphics.


if __name__ == "__main__":
    main()
