# anonymizer_csv
Anonymize a text column of a csv with the help of [NLM-Scrubber](https://scrubber.nlm.nih.gov/)


## Requeriments
-Pandas

-unidecode

-spacy

run next line for download model in spanish 
```python
$~ python -m spacy download es_core_news_sm

```




## Run in Windows or Linux

 
```python
>> python anonymizer_csv/anonimize.py <csv_file> <final_name> <colum_to_anonimize> <new_colum> <colum_id> <path_scrubber_exe> <delimiter>

```

* In linux is necessary to grant execution permission to the file anonymizer_csv/scrubber.19.0403L/scrubber.19.0403.lnx
 
```python
$~ sudo chmod 700 anonymizer_csv/scrubber.19.0403L/scrubber.19.0403.lnx

```



-csv_file: location (complete) csv file to anonymize

-final_name: location (complete) resulting csv file

-colum_to_anonimize: Name of the column to anonymize

-new_colum: name of the resulting column with anonymized text

-colum_id: name of the index column of the table

-path_scrubber_exe: location (complete) of the NLM-Scrubber executable (optional)

-delimiter: delimiter of the csv file
