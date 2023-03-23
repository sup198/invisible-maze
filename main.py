def on_overlap_tile(sprite, location):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile2
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile6
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile10
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile6
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile8
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile3
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile6)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 e e e f f f f 
            f f f 4 4 4 e e f f f f 
            f f f 4 4 4 4 e e f f f 
            f 4 e 4 4 4 4 4 4 e 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f e 4 d d d d d d 4 e f 
            . f e d d b b d d e f . 
            . f f e 4 4 4 4 e f f . 
            e 4 f b 1 1 1 1 b f 4 e 
            4 d f 1 1 1 1 1 1 f d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile0
"""))