import pandas as pd

class qualityindex:
    def __init__(self, h_index, recency, number_of_citations, journal_impact):
        self.h_index = h_index
        self.recency = recency
        self.number_of_citations = number_of_citations
        self.journal_impact = journal_impact
        self.h_index_para = 10 #more than or equal to
        self.number_of_citations_para = 10 #more than or equal to
        self.recency_para = 5 ##less than or equal to 5 years
        self.journal_impact_para = 2##more than or equal to

    def update_h_index(self, bool):
        if bool == true
            
    def update_h_index(self, bool):
        if 
    def update_h_index(self, bool):
        if 
    def update_h_index(self, bool):
        if 

    def __decision_tree___(self, other):
        if h_index < h_index_para:
            return f"h_index error"
        if number_of_citations < number_of_citations_para:
            return f"number_of_citations error"
        if journal_impact < journal_impact_para:
            return f"journal_impact error"
        if recency > recency_para:
            return f"recency error"

    def accuracy_quality_index
        return metrics.accuracy_score(y_test, y_pred))
    

##below is some feedback I got from gemini on how to make a decisiontree with sklearn, I have to look into it more
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth=4)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


##from datacamp
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
