class Paper:
    def __init__(self, title, authors, abstract, date, source, quality_score):
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.date = date
        self.source = source
        self.quality_score = quality_score

    def to_dict(self):
        return {
            'Title': self.title,
            'Authors': self.authors,
            'Abstract': self.abstract,
            'Date': self.date,
            'Source': self.source,
            'QualityScore': self.quality_score
        }
