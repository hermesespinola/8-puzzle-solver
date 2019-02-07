import bfs

methods = {
    'bfs': (
        bfs.init_struct, # create structure function
        bfs.visit, # visit function
        bfs.expand, # expand function
        bfs.add, # add to structure
    ),
}