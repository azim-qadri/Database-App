# Database App

This is a simple database application built using Python's Tkinter library and SQLite. The app allows users to manage a database of addresses, including adding, viewing, updating, and deleting records.

## Prerequisites

To run this application, you need to have Python and the Tkinter library installed on your system.

## Getting Started

1. Clone the repository:

```
git clone <repository_url>
```

2. Change into the cloned directory:

```
cd <repository_name>
```

3. Run the Python script to launch the application:

```
python main.py
```

## Usage

The application provides a graphical user interface with the following features:

### Add Record

To add a new address record, fill in the First Name, Last Name, Address, City, State, and Zip code fields, and then click the "Add Record" button.

### Show Records

To view all records currently stored in the database, click the "Show Records" button. The records will be displayed below the buttons.

### Update Record

To update an existing record, first, enter the ID of the record you wish to update in the "Select Id" field. Then, click the "Update Record" button. A new window will pop up, allowing you to modify the address details. After making the necessary changes, click the "Save" button to update the record.

### Delete Record

To delete a record, enter the ID of the record you wish to delete in the "Select Id" field, and then click the "Delete Record" button.

## Database

The application uses an SQLite database named `data.db` to store the address records. If the database file does not exist, it will be created automatically when you run the application.

## Screenshots
![Image](https://github.com/azim-qadri/Database-App/blob/main/Screenshot%20(83).png) ![Image](https://github.com/azim-qadri/Database-App/blob/main/Screenshot%20(84).png)
## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.
