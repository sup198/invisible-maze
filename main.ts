scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile2`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite3, location3) {
    tiles.setCurrentTilemap(tilemap`level4`)
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile10`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile9`, function (sprite4, location4) {
    game.over(true, effects.smiles)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile8`, function (sprite5, location5) {
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile6`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite2, location2) {
    tiles.setCurrentTilemap(tilemap`level2`)
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile6`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile5`, function (sprite6, location6) {
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile3`)
})
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
tiles.setCurrentTilemap(tilemap`level1`)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
tiles.placeOnRandomTile(mySprite, assets.tile`myTile0`)
