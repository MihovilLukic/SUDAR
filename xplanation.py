xplanation
1
2
3
4
5
6
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
In this section, we’ve created “groups” for our sprites. A Sprite group is sort of like a classification. It’s much easier to deal with 2 or 3 groups, rather than having to deal with dozens or even hundreds of sprites. Keeping them in one group allows us to easily access every sprite in that group.

In the example above, we’ve created two groups one called enemy and the other called all_sprites. (This code doesn’t have more than one enemy, but since multiple enemies could easily be added here, we’ve created a separate group for it). To add a Sprite to a group, you just have to use the add() function.

1
2
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
We talked about event objects earlier, such as QUIT. Python Pygame, gives us the option to create custom events called “User events”. Here we’ve created an event called INC_SPEED. To do so, we called the pygame.USEREVENT and added one into it (to ensure that it will have a unique ID). More about events in a separate tutorial.

Next we use the Pygame time module’s set_timer() function to call the INC_SPEED event object every 1000 milliseconds, or 1 second.

1
2
3
4
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 2
The next piece of code if about the Game loop. In the for loop where we iterate over every event that occurs, we insert an if statement to check for the INC_SPEED event occuring. If it does, we increase the SPEED variable by 2. This variable us used by the Enemy class to determine it’s speed.

All in all, the purpose of this code is to make the game more challenging as time passes.
1
2
3
4
5
6
7
8
9
#To be run if collision occurs between Player and Enemy
if pygame.sprite.spritecollideany(P1, enemies):
      DISPLAYSURF.fill(RED)
      pygame.display.update()
      for entity in all_sprites:
            entity.kill() 
      time.sleep(2)
      pygame.quit()
      sys.exit() 
This section of code is related to collision detection in Python pygame. Remember how we created groups earlier? You’re about to see a massive benefit that we get from having meaningful groups.

The spritecollideany() function takes two parameters, the first must be a regular Sprite, like P1 or E1. The second must be a Sprite group, such as Enemies or all_sprites. This function compares the sprite passed in the first parameter, to see if it’s touching any of the sprites in the group passed in parameter two.

In our case, it checks to see whether our Player has collided with any of the sprites in the enemies group. The benefit of this function is that even if there are 1000 enemy sprites, we don’t have to check collisions with them individually, and instead just use this function.

Finally, the collision holds True, we kill all the sprites using the kill() function, fill the screen with red, wait two seconds and close the entire program.

(Calling kill() will remove the sprite from the group, hence it will no longer be drawn to the screen. If you don’t use groups, and try kill() on a sprite, you might not get the desired effect)

1
2
3
for entity in all_sprites:
    DISPLAYSURF.blit(entity.image, entity.rect)
    entity.move()
Yet another benefit of the grouping system, we can now call the “move” functions for all the sprites and redraw them in just 3 lines of code. If you’ve noticed, we’ve removed the two draw() functions from both the Player and Enemy class in our code.

