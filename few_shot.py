import json
import pandas as pd

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.unique_influencers = None 
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as file:
            posts = json.load(file)
            self.df = pd.json_normalize(posts)
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
            self.unique_influencers = self.df["Influencer"].unique().tolist() 
            all_tags = self.df["tags"].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    
    def get_influencers(self):
        return self.unique_influencers
    

    def get_posts_by_influencer(self, influencer):
        return self.df[self.df["Influencer"] == influencer].to_dict(orient="records")


    def get_filtered_posts(self, length, language, tag, influencer):
        df_filtered = self.df[
            (self.df["length"] == length) & 
            (self.df["language"] == language) & 
            (self.df["tags"].apply(lambda tags: tag in tags))&
            (self.df["Influencer"] == influencer)
        ]

        return df_filtered.to_dict(orient="records")

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags 
    
    



if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Short", "Hinglish", "Influencer")
    print(posts)
