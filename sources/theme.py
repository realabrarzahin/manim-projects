# theme.py

class Theme:
    def __init__(self):
        # Background and surface tones
        self.background_primary = "#191521"  # deep black-purple
        self.background_secondary = "#231E30"  # twilight shadow

        # Accent colors
        self.teal = "#53D69A"       # minty signal
        self.steel = "#626769"      # industrial gray
        self.sky = "#7EAEF2"        # clear sky blue
        self.violet = "#A277FF"     # classic Aura violet
        self.apricot = "#F1BF78"    # sun-washed gold
        self.rose = "#F27A7A"       # calm crimson
        self.pink = "#F694FF"       # soft magenta
        self.white = "#FFFFFF"      # pure white for contrast

    def to_dict(self):
        return self.__dict__

