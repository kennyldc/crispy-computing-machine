
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class scaler_split(object):
    """
    Class for scaling and splitting independent and target features.    

    Attributes
    ----------
    df : pd.DataFrame
        Data frame to get the independent and target features
    X : list
        List of data frame independent headers 
    Y : list
        List of data frame target header
    X_train : array
        Train set of independient features
    X_val : array
        Validation set of independient features
    X_test: array
        Test set of independient features
    Y_train : pd.DataFrame
        Train set of target feature
    Y_val : pd.DataFrame
        Validation set of target feature
    Y_test: pd.DataFrame
        Test set of target feature
    Methods
    -------
    split(val,test,rs=None)
        Splits data frame and gets train, validation, test sets
    scaler(scaler='MinMaxScaler')
        Scales independient (X) sets. There are tow options MinMaxScaler and StandardScaler
    """
    
    def __init__(self, df,X,Y):
        """
        Parameters
        ----------
        df : pd.DataFrame
            Data frame to get the independent and target features
        X : list
            List of data frame independent headers 
        Y : list
            List of data frame target header
        """
        self.df = df
        self.X = X
        self.Y = Y
        
    def split(self,val,test,rs=None):
        """
        Gets X_train, X_val, X_test, Y_train, Y_val, Y_test
        
        Parameters
        ----------        
        val : float
            Must be between 0 and 1. Porcentage of validation set
        test : float
            Must be between 0 and 1. Porcentage of test set
        rs : float
            Random state for split. Default = None
        """
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.df[self.X],self.df[self.Y], test_size=test,random_state=rs)
        self.X_train, self.X_val, self.Y_train, self.Y_val = train_test_split(self.X_train,self.Y_train, test_size=val/(1-test),random_state=rs)
    
    def scaler(self, scaler='MinMaxScaler'):
        """
        Scales X_train, X_val, X_test
        
        Parameters
        ----------        
        scaler : string
            'MinMaxScaler': Uses MinMaxScaler from scikit-learn
            'StandardScaler': Uses StandardScaler from scikit-learn
            In another case, it does not scale
        
        Returns
        -------
        object
            Returns object scaler. If scaler not in ('MinMaxScaler','StandardScaler'),
            returns None
        """
        
        if scaler=='MinMaxScaler':
            scalerc = MinMaxScaler()
            self.X_train = scalerc.fit_transform(self.X_train)
            self.X_val = scalerc.transform(self.X_val)
            self.X_test = scalerc.transform(self.X_test)
            return scalerc
        else:
            if scaler=='StandardScaler':
                scalerc = StandardScaler()
                self.X_train = scalerc.fit_transform(self.X_train)
                self.X_val = scalerc.transform(self.X_val)
                self.X_test = scalerc.transform(self.X_test)
                return scalerc
            else:
                print('Supported values: "MinMaxScaler", "StandardScaler"')
                return None
