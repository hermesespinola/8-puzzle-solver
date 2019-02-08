import bfs
import dfs
import a_star

methods = {
    'bfs': (
        bfs.init_struct, # create structure function
        bfs.visit, # visit function
        bfs.expand, # expand function
        bfs.add, # add to structure
    ),
    'a_star': (
        a_star.init_struct, # create structure function
        a_star.visit, # visit function
        a_star.expand, # expand function
        a_star.add, # add to structure
    ),
    'dfs': (
        dfs.init_struct, # create structure function
        dfs.visit, # visit function
        dfs.expand, # expand function
        dfs.add, # add to structure
    )
}
