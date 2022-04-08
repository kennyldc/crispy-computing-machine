
import numpy as np
import pandas as pd
from functools import reduce

class window_time(object):
    """
    Class for feature engineering. Get a time window from the features current_price,
    market_cap, total_volume and get a time window from future incremental current_price.    

    Attributes
    ----------
    vobs : int
        Observation window backward for each day
    vdes : int
        Performance window forward for each day
    step : int
        Number of days grouped to get metrics in the observation window
    incremental : int
        Porcentage of increment minimum of the price in the performance window
    anclai: int
        Minimum day in data such that its observation window is full defined
    anclaf: int
        Maximum day in data such that its performance window is full defined
        
    Methods
    -------
    anclas(time_column)
        Initializes anclai and anclaf
    ing_X(df,ancla,k)
        Gets current_price mean, current_price std, market_cap mean, market_cap std,
        total_volume mean, total_volume std from a specific day and a specific 
        observation window
    ing_Y(df,ancla,inc)
        Gets a binary feature from a specific day and the perfomance window (vdes).
        1 when the future performance window price is greater than or equal to 
        the current price plus and specific incremental rate (inc); 0 in any other case
    eng_X(df,um)
        Gets all observation window features for each day in the data frame
    eng_Y(df)
        Gets all performance window features for each day in the data frame
    """
    def __init__(self,vobs,vdes,step,incremental):
        """
        Parameters
        ----------
        vobs : int
            Observation window backward for each day
        vdes : int
            Performance window forward for each day
        step : int
            Number of days grouped to get metrics in the observation window
        incremental : float
            Porcentage of increment minimum of the price in the performance window
        """
        self.vobs = vobs
        self.vdes = vdes    
        self.step = step
        self.incremental = incremental
    
    def anclas(self, time_column):
        """
        Initializes anclai and anclaf
        
        Parameters
        ----------        
        time_column : pd.Series
            Field of data frame to consider as day feature
        """
        self.anclai = self.vobs-1
        self.anclaf = time_column.max()- self.vdes
        
    def ing_X(self,df,ancla,k):
        """
        Gets current_price mean, current_price std, market_cap mean, market_cap std,
        total_volume mean, total_volume std from a specific day and a specific 
        observation window
        
        Parameters
        ----------        
        df : pd.DataFrame
            Data frame. The day feature must be named 't'
        ancla : int
            Initial day to get the features for observation window
        k: int
            Size (in days) for observation window
        
        Returns
        -------
        pd.DataFrame
            Data frame with the features from the observation window time of initial day (ancla)
        """
        
        l = []
        
        aux = df.loc[(df['t'] <= ancla) & (df['t'] >= (ancla-k+1))]
        
        #current_price_mean
        piv = aux.pivot_table(index='symbol',columns='t',values='current_price',aggfunc='sum')
        piv[f'x_current_price_mean_{k}'] = piv.mean(axis=1)
        l.append(piv.filter(like='x_'))
        
        #current_price_std
        piv = aux.pivot_table(index='symbol',columns='t',values='current_price',aggfunc='sum')
        piv[f'x_current_price_std_{k}'] = piv.std(axis=1)
        l.append(piv.filter(like='x_'))   
        
        #market_cap_mean
        piv = aux.pivot_table(index='symbol',columns='t',values='market_cap',aggfunc='sum')
        piv[f'x_market_cap_mean_{k}'] = piv.mean(axis=1)
        l.append(piv.filter(like='x_'))

        #market_cap_std
        piv = aux.pivot_table(index='symbol',columns='t',values='market_cap',aggfunc='sum')
        piv[f'x_market_cap_std_{k}'] = piv.std(axis=1)
        l.append(piv.filter(like='x_'))   

        #total_volume_mean
        piv = aux.pivot_table(index='symbol',columns='t',values='total_volume',aggfunc='sum')
        piv[f'x_total_volume_mean_{k}'] = piv.mean(axis=1)
        l.append(piv.filter(like='x_'))

        #total_volume_std
        piv = aux.pivot_table(index='symbol',columns='t',values='total_volume',aggfunc='sum')
        piv[f'x_total_volume_std_{k}'] = piv.std(axis=1)
        l.append(piv.filter(like='x_'))   

        aux = reduce(lambda x,y:pd.merge(x,y,left_index=True,right_index=True,how='outer'),l).reset_index()
        aux.insert(1,'ancla',ancla)
    
        return aux
    
    def ing_Y(self,df,ancla,inc):
        """
        Gets a binary feature from a specific day and the perfomance window (vdes).
        1 when the future performance window price is greater than or equal to 
        the current price plus and specific incremental rate (inc); 0 in any other case
        
        Parameters
        ----------        
        df : pd.DataFrame
            Data frame. The day feature must be named 't'
        ancla : int
            Initial day to get the features for performance window
        inc: float
            Incremental rate target for the initial day
        
        Returns
        -------
        pd.DataFrame
            Data frame with the features from the performance window time of initial day (ancla)
        """
        
        valor=df.loc[(df['t']>ancla-1)&(df['t']<=(ancla))][['current_price']].values[0][0]
        aux=df.loc[(df['t']>ancla)&(df['t']<=(ancla+self.vdes))][['symbol','current_price']]
        aux['tgt']=valor
        aux['ptgt']=aux["current_price"]/aux["tgt"]-1
        aux['obj']=np.where(aux['ptgt']>=inc,1,0)
        aux=aux['obj'].values
        aux=[i for i in range(len(aux)) if aux[i] ==1]
        if len(aux)>0:
            aux=1
        else:
            aux=0
        aux2 = df.loc[(df['t']>ancla)&(df['t']<=(ancla+self.vdes))][['symbol']].drop_duplicates().reset_index(drop=True).assign(tgt=aux)
        aux2.insert(1,'ancla',ancla)
        
        return aux2
    
    def eng_X(self,df,um):
        """
        Gets all observation window features for each day in the data frame
        
        Parameters
        ----------        
        df : pd.DataFrame
            Data frame to get all the features
        um : list
            List of data frame headers such that they define the sample unit
        
        Returns
        -------
        pd.DataFrame
            Data frame with all the features from the observation window time of all days
        """
        
        cruzar = lambda x,y:pd.merge(x,y,on=um,how='outer')
        
        apilar = lambda x,y:x.append(y,ignore_index=True)
        
        X = reduce(apilar,
                    map(lambda ancla:
                        reduce(cruzar,
                                map(lambda k:self.ing_X(df,ancla,k),range(self.step,self.vobs+self.step,self.step))
                                ),
                    range(self.anclai,self.anclaf+1)
                        )
                    )
        return X
    
    def eng_Y(self,df):
        """
        Gets all performance window features for each day in the data frame
        
        Parameters
        ----------        
        df : pd.DataFrame
            Data frame to get all the performance binary feature
        
        Returns
        -------
        pd.DataFrame
            Data frame with all the features from the performance window time of all days
        """
        
        apilar = lambda x,y:x.append(y,ignore_index=True)
        
        Y = reduce(apilar,map(lambda ancla:self.ing_Y(df,ancla,self.incremental),range(self.anclai,self.anclaf+1)))
        
        return Y
