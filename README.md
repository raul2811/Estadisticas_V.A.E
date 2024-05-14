# Estadísticas V.A.E

Este proyecto integra un apartado de estadísticas para [revistas de la universidad de panama](https://revistas.up.ac.pa) el cual utiliza como base el proyecto [OJS](https://github.com/pkp/ojs).

## Datos a tener en cuenta

- La tabla 'journal_setting' contiene cada uno de los archivos detallados que está en la tabla 'journals', incluido el ISSN.

- Las revistas activas en la tabla 'journals' tienen el valor 1 en la columna 'enable', mientras que las inactivas tienen el valor 0.

- La tabla 'journals_setting' muestra la información correspondiente a cada revista a través del 'journal_id', incluido el ISSN asociado.

- Los artículos que contiene cada revista están ordenados en la tabla 'issues', la cual contiene todos los artículos que son parte de cada revista ordenado por año y fecha de publicación.

- La tabla 'issue_setting' contiene la información correspondiente a cada uno de los artículos, incluido el tomo de la revista y la fecha de publicación.

## Tablas importantes

- La tabla 'journals' contiene el id y el nombre de todas las revistas que se publican en la Universidad de Panamá. La columna 'path' indica el nombre de la revista, y la columna 'enable' indica qué revistas están activas (valor 1) y cuáles no (valor 0).

- La tabla 'journals_setting' muestra la información correspondiente a cada revista en general por medio del 'journal_id', e indica dónde está alojado el valor ISSN asociado a la revista.

- La tabla 'issues' contiene todos los artículos que son parte de cada revista ordenados por año y fecha de publicación.

- La tabla 'issue_setting' contiene la información correspondiente a cada uno de los artículos, como el tomo de la revista, la fecha de publicación, etc.



