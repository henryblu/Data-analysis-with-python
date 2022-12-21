#!/usr/bin/env python3

import pandas as pd

def cities():
    '''Returns a list of cities in finland with their population and area.'''
    return pd.DataFrame({
        'Population': [643272, 279044, 231853, 223027, 201810],
        'Total area': [715.48, 528.03, 689.59, 240.35, 228.5], 
        
    }, index= ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu'])
    
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
