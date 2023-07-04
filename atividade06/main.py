from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def read_aeronet(filename):
    """Read a given AERONET AOT data file, and return it as a dataframe.
    
    This returns a DataFrame containing the AERONET data, with the index
    set to the timestamp of the AERONET observations. Rows or columns
    consisting entirely of missing data are removed. All other columns
    are left as-is.
    """
    dateparse = lambda x: datetime.strptime(x, "%d:%m:%Y %H:%M:%S")
    aeronet = pd.read_csv(filename, skiprows=6, na_values=['N/A'],
                          parse_dates={'times':[0,1]},
                          date_parser=dateparse)

    aeronet = aeronet.set_index('times')
    #del aeronet['Julian_Day']
    
    # Drop any rows that are all NaN and any cols that are all NaN
    # & then sort by the index
    an = (aeronet.dropna(axis=1, how='all')
                .dropna(axis=0, how='all')
                .rename(columns={'Last_Processing_Date(dd/mm/yyyy)': 'Last_Processing_Date'})
                .sort_index())

    return an

filename = '20140101_20151231_ARM_Manacapuru.lev15'
#filename = '20140101_20151231_ARM_Manacapuru.lev20'
df = read_aeronet(filename)
print(df.columns.values)
# Remove negative values
df = df[df['Precipitable_Water(cm)'] >= 0]

placename = df['AERONET_Site_Name'][0]
#varname = 'AOD_500nm'
#varname = 'Precipitable_Water(cm)'
varname = '440-675_Angstrom_Exponent'
df[varname].plot(linestyle='',marker='.')
plt.xlabel('')
plt.ylabel(varname)
plt.title(placename)
plt.savefig(f'{placename}_{varname}.png', bbox_inches='tight')