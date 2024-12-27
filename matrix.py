# moves up,down,left,right
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#moves up,down,left,right,diagonally
moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

# chess - moves made by a knight
knight_moves = [
    (2, 1),  (2, -1),  # Two steps vertically, one step horizontally
    (-2, 1), (-2, -1), # Two steps vertically, one step horizontally (opposite)
    (1, 2),  (1, -2),  # Two steps horizontally, one step vertically
    (-1, 2), (-1, -2)  # Two steps horizontally, one step vertically (opposite)
]