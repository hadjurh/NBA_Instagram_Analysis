import sys
import os
import errno
import  numpy as np
from get_insta_data import get_insta_data
from make_network import build_adjacency_matrix

# ARG1 Name of new folder where to put 'player_username_id_team.csv'
# ARG2 Folder that contains your username and password ("username\npassword\n")

current_path = os.path.dirname(os.path.abspath(__file__))

folder_path = current_path + '/../database/' + sys.argv[1]
players_data = folder_path + '/player_username_id_team.csv'
json_file = folder_path + '/followings.json'
matrix_file = folder_path + '/adjacency_matrix.csv'
pass_file = sys.argv[2]

file = open(pass_file, 'r')
ids = [line[:-1] for line in file.readlines()]
username = ids[0]
password = ids[1]


def main(argv):
    get_insta_data(players_data, json_file, username, password)
    network_matrix = build_adjacency_matrix(players_data, json_file)
    np.savetxt(matrix_file, network_matrix, delimiter=",", fmt='%.0i')


if __name__ == '__main__':
    main(argv=sys.argv)