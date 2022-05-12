# ACME

### Content:

- `classes` --> Folder that contains the File class representation.
- `modules` --> Folder that contains the methods and validations before generating the final report.
- `test` --> Folder that contains the necessary unit tests to check the correct operation of the application.
- `files` --> Folder that contains the files to read.
- `main.py` --> File to start the aplication.


### Desciption

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

```bash
Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```

```bash
Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3
```
  

### Overview Solution

The first step was to really understand the requirement, making a whiteboard to generate a flow from start to finish of the application and dividing the problem into smaller problems.

Once the small problems were identified, I defined the design pattern that best fit, in this case I implemented Singleton, which guarantees the existence of a single object of its type and provides a single point of access.

Finally I developed the application using the OOP paradigm.



### FlowChart

<a href="https://cdn.discordapp.com/attachments/887159577802604575/974193440399171604/Untitled_1.jpg"></a>



### Usage

- Store the files you want to read in the `files` folder as .txt

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974101619648102451/unknown.png" width = "200"/>

### Format by line

```bash
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```



### Interact with app

- Enter valid username

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974088147275247646/unknown.png" width = "900"/>

- Select valid option

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974094426429358170/unknown.png" width = "900"/>

- Enter the filename you want to read

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974099123626201138/unknown.png" width = "900"/>

- Finally you will see the report

<img src = "https://cdn.discordapp.com/attachments/887159577802604575/974102499273351189/unknown.png" width = "900"/>



### Install
- Copy the repository
- Enter the new folder `ACME`.
- Execute the main.py file: `python3 main.py` or `./main.py`



### Authors

- **Manuel Alejandro Gomez** - [LinkedIn](https://www.linkedin.com/in/manolobkno08/)
