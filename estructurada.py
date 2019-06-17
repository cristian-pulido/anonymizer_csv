import pandas as pd
import hashlib

def limpiar(data,colum_to_hash,lista_eliminar):
    #print(list(data.columns))      
    for i in lista_eliminar:     
        data.drop(i,axis=1,inplace=True)

    A=[]
    for i in list(data[colum_to_hash]):
    	try:
        	A.append(hashlib.md5(str(int(float(i))).encode('utf-8')).hexdigest())
    	except:
    		A.append(i)
    		
    data['hash_'+str(colum_to_hash)]=A
    
    data.drop(colum_to_hash,axis=1,inplace=True)
        
    return data

def limpiar_csv(path_in,path_out,colum_to_hash,lista_eliminar,delimiter="~"):
    #print(lista_eliminar)
    try:
        data=pd.read_csv(path_in,delimiter,encoding='utf-8')
    except:
        data=pd.read_excel(path_in,encoding='utf-8')
    new_data=limpiar(data,colum_to_hash,lista_eliminar)
    new_data.to_csv(path_out,sep=delimiter,index=False,encoding='utf-8')
    
    return 'completo'

    
