from phase import Phase
from player import Player
import pandas as pd

class Files:
    def load_from_file(self, filename):
        phases_df = pd.read_csv(filename)
        #print(phases_df.head())
        phases = []
        for ind in phases_df.index:
            player = Player(phases_df["x"][ind], phases_df["y"][ind], eval(phases_df["color"][ind]), 
                            phases_df["height"][ind], phases_df["width"][ind], phases_df["vel"][ind])
            phase = Phase(player, phases_df["background"][ind], eval(phases_df["pos"][ind]), 
                          eval(phases_df["end_pos"][ind]), phases_df["d_x"][ind], phases_df["d_y"][ind])
            phases.append(phase)
        return phases