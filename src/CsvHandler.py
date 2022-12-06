import pandas as pd

class CsvHandler:
    def __init__(self, file_name):
        """
        Description:
        ------------
        Reads the csv file and stores as a dataframe.
        """
        file_name = '{}/{}'.format('resources', file_name)
        self.csv_file = pd.read_csv(file_name)

    def get_artist(self):
        """
        Description:
        ------------
        returns the artist names from the specified file.
        """
        return self.csv_file['Artist Name'].tolist()
    
    def get_views(self):
        """
        Description:
        ------------
        returns the view count of each artist.
        """
        return self.csv_file['Views'].tolist()

    def get_artist_with_views(self):
        """
        Description:
        ------------
        returns the artist name with the associated view count as a dictionary.
        """
        return dict(zip(self.get_artist(), self.get_views()))

    def get_track_names(self):
        """
        Description:
        ------------
        returns the track name.
        """
        return self.csv_file['Track Name'].tolist()

    