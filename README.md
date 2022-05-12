# ACME

It is a console that contains an interpreted environment and this is the content:

- `_freeenv` --> Release the memory used in environment variable



### Desciption

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00


OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3


  

### FlowChart

<a href="https://lucid.app/lucidchart/invitations/accept/inv_a1bc173c-ce8a-4496-b8c3-bcfad1636812?viewport_loc=-311%2C-106%2C2560%2C1168%2C0_0"><img src="https://github.com/manolobkno08/simple_shell/blob/main/images/diagrama.png"></a>



### Usage

- Store the files you want to read in the `files` folder as .txt

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974096326570696824/unknown.png" width = "500"/>



### Interact with app

- Enter valid username

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974088147275247646/unknown.png" width = "900"/>

- Select valid option

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974094426429358170/unknown.png" width = "900"/>

- Select the file you want to read

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974099123626201138/unknown.png" width = "900"/>



### Install
- Copy the repository
- Enter the new folder `ACME`.
- Execute the main.py file: `python3 main.py` or `./main.py`



### Authors

- **Manuel Alejandro Gomez** - [LinkedIn](https://www.linkedin.com/in/manolobkno08/)
