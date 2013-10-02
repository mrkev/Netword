from network_draw  import *

def work_network(string):

    cpath = c_path_from_string(string)
    nmap  = map_node_list(get_node_names(c_path_from_string(string)))
    c_matrix = normalized_e_graph(c_graph_from_connection_path_and_map(cpath, nmap))

    draw_network(nmap, c_matrix)
    
    
if __name__ == '__main__':
    NETWORK      = "A.B.C.M.H.S.W.D.E.F.A.F.G.A.W.A.B.A.C.X.G.C.H.I.J.K.L.M"
    work_network(NETWORK)