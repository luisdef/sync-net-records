# Syncing Network Registration Access via MAC Address

Script that will automatically check for updates between 
the forms database and also the application. Once those 
records are perfectly in sync it will do the registration 
in the router system (Mikrotik).

## Setting up

To begin with, it is highly recommended to create a 
Python virtual environment to run the script.

It can be done running the following commands:

### Linux (Ubuntu based)

In Linux (make sure to have `python3-venv` and `python3-pip`
installed):
```sh
python3 -m venv .venv # Creates a virtual environment directory named .venv
```

```sh
source .venv/bin/activate # Activates the virtual environment
```

And then proceed to install the packages required by 
the script.

```sh
pip3 install -r requirements.txt 
```

### Windows

In Windows Powershell:
```ps1
python.exe -m venv .venv
```

Run the Powershell script to enable the virtual environment 
(check if the Powershell is set to allow ps1 scripts).
Check [Execution Policy at Microsoft](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4).
```ps1
.\.venv\Scripts\Activate.ps1 
```

And then proceed to install the packages required by 
the script.

```ps1
pip install -r requirements.txt 
```

## Running the script

> [!WARNING]
> 
> Make sure to generate your credentials in the Google
> Console, and then put it into the `secrets/` directory in the
> root of this repository.

Once all configurations are done, run the script like so:

```sh
python3 main.py # In Linux
```

```ps1
python.exe main.py # In Windows
```

## Contributors

- Luis Felipe Assmann (luis.assmann.1234@gmail.com)
