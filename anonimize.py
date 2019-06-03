import os, shutil, sys
import pandas as pd     
import unidecode


def anonimizar(csv_file,final_name,path_in,path_out,colum_to_anonimize,new_colum,colum_id,path_scrubber_exe,delimiter="~"):

    
    data=pd.read_csv(csv_file,delimiter=delimiter)
    
    if os.path.exists(path_in):
        shutil.rmtree(path_in)
    if os.path.exists(path_out):
        shutil.rmtree(path_out)
    os.mkdir(path_in)
    os.mkdir(path_out)
    
    for i in range(len(data)):
        with open(os.path.join(path_in,str(data[colum_id][i]))+".txt", "w") as text_file:
            text_file.write(unidecode.unidecode(data[colum_to_anonimize][i]))
    
    folder_exe,executer=os.path.split(path_scrubber_exe)
    
    config_file=os.path.join(os.path.dirname(final_name),"config.cfg")
    
    with open(config_file, "w") as text_file:
        text_file.write("ClinicalReports_dir = "+path_in+"\n")
        text_file.write("nPHI_outdir = "+path_out+"\n")
        text_file.write("ClinicalReports_files = [^\.].*")
        
    os.chdir(folder_exe)

    if sys.platform == 'linux':
        os.system("./"+executer + " " + config_file)
    else:
        os.system(executer + " " + config_file)
        
    lista=os.listdir(path_out)
    anonimos=[]    
    for i in lista:
        f = open (os.path.join(path_out,i),'r')
        mensaje = f.read()
        anonimos.append([int(os.path.basename(f.name).split(".")[0]),mensaje[:mensaje.index("###")-1]])
        f.close()
    
    new_data=pd.DataFrame(anonimos,columns=[colum_id,new_colum])
    data.drop(colum_to_anonimize,axis=1,inplace=True)
    
    merge=pd.merge(data,new_data,on=colum_id)
    merge.to_csv(final_name,sep=delimiter,index=False)

    shutil.rmtree(path_in)
    shutil.rmtree(path_out)
    os.remove(config_file)
        
    return "completo"          
             
if __name__ == "__main__":

    csv_file = sys.argv[1]
    final_name = sys.argv[2]
    path_in =  sys.argv[3]
    path_out = sys.argv[4]
    colum_to_anonimize= str(sys.argv[5])
    new_colum= str(sys.argv[6])
    colum_id= str(sys.argv[7])

    if len(sys.argv) > 8 :
        path_scrubber_exe= sys.argv[8]
        delimiter= str(sys.argv[9])
        anonimizar(csv_file,final_name,path_in,path_out,colum_to_anonimize,new_colum,colum_id,path_scrubber_exe,delimiter)
    else:
    
	    base_folder=os.path.dirname(os.path.abspath(__file__))

	    if sys.platform == 'linux':
	        path_scrubber_exe=os.path.join(base_folder,"scrubber.19.0403L/scrubber.19.0403.lnx")
	    else:
	        path_scrubber_exe=os.path.join(base_folder,"scrubber.19.0411W/scrubber.19.0411W.exe")

	    anonimizar(csv_file,final_name,path_in,path_out,colum_to_anonimize,new_colum,colum_id,path_scrubber_exe)    

