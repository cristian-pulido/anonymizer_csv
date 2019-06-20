# ANONYMIZER CSV

Anonymize a text column of a csv with the help of [NLM-Scrubber](https://scrubber.nlm.nih.gov/).

## Install

- Install and run [Docker](https://www.docker.com/) *(this project use **docker-compose**)*.

- Download or clone this git repository in your local machine.

- Open terminal and change directory to root project.

- Execute `docker-compose build` to install **docker images** *(Wait a few seconds for the command to complete)*.

## Run develop environment

- Execute `docker-compose up -d develop` to init **docker container**.

> Use `docker-compose up -d --build develop` in case the docker files have been changed.

## Stop

- Execute `docker-compose stop` to **stop** container.

*or*

- Execute `docker-compose down` to **stop** and **delete** container.

## Install with PIP

- Add your package in `~/requirements.txt` file.

- Execute `docker-compose up -d --build develop` to install packages with PIP.

> If docker container is running execute `docker-compose down` to stop and delete container.

## Show logs

Execute `docker-compose logs develop` to show container logs.

## Execute commands

Execute `docker-compose exec develop bash` to attach the container terminal.

## Code scaffolding

#### Anonymize column CSV

Execute to anonymize.

> Add your CSV to `~/data` directory.

```shell
python anonimize.py /data/<csv_file> /data/<final_name> <colum_to_anonimize> <new_colum> <colum_id> <path_scrubber_exe> <delimiter>
```

- **csv_file:** location (complete) csv file to anonymize.
- **final_name:** location (complete) resulting csv file.
- **colum_to_anonimize:** Name of the column to anonymize.
- **new_colum:** name of the resulting column with anonymized text.
- **colum_id:** name of the index column of the table.
- **path_scrubber_exe:** *(optional)* location (complete) of the NLM-Scrubber executable.
- **delimiter:** *(optional)* delimiter of the csv file, default `~`.

Example (columns csv: `id`, `...`, `description`):

```shell
python anonimize.py /app/data/example.csv /app/data/example-anonymized.csv description description id
python anonimize.py /app/data/example.csv /app/data/example-anonymized.csv description description id /app/scrubber.19.0403L/scrubber.19.0403.lnx ","
```

> Default separator is `~`.

---

### Additional resources

- [Docker get started](https://www.docker.com/get-started)