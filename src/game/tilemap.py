# -*- coding: utf-8 -*-

import tile

class TileMap(object):
    """ This class holds the tiles. """

    def __init__(self, x, y, res, batch, *args, **kwargs):
        super(TileMap, self).__init__(*args, **kwargs)
        
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        self.res = res
        self.batch = batch
        self.tile_size = 32
        
        self.tiles = []
        
        self.init_tiles()
        
    def init_tiles(self, default_tile=0):
        blit_y = self.y - self.tile_size
        
        for y in range(0, self.height):
            blit_x = self.x
            
            new_row = []
            
            for x in range(0, self.width):
                temp_tile = tile.Tile(self.res.gfx["grass"])
                temp_tile.x = blit_x
                temp_tile.y = blit_y
                temp_tile.batch = self.batch

                
                new_row.append(temp_tile)
                blit_x = blit_x + self.tile_size
                
            self.tiles.append(new_row)
            blit_y = blit_y - self.tile_size