# create-py-app

`create-py-app` is a command-line tool that generates a basic Python project structure, similar to `create-react-app` for React projects. It sets up a lightweight yet professional folder structure with some best practices in mind, helping you kickstart your Python projects quickly and efficiently.

## In action 
### CMD 
![Create using cmd](https://github.com/KindEmily/create-py-app/blob/main/demo/create_new_app_from_cmd.gif)

## Features

- Creates a basic Python project structure
- Includes a `src` directory for your source code
- Sets up a `tests` directory for unit tests
- Generates `__init__.py` files to make directories into Python packages
- Creates a `requirements.txt` file for listing dependencies
- Adds a `README.md` file with a basic project description
- Includes a `.gitignore` file with common Python-related entries

## Installation

1. Clone this repository or download the source code:
   ```
   git clone https://github.com/yourusername/create-py-app.git
   ```
   or download and extract the ZIP file from the GitHub repository.

2. Navigate to the directory containing the `create-py-app` files:
   ```
   cd path/to/create-py-app
   ```

3. Add the directory to your system's PATH:
   - **Windows**:
     - Press Win + X and select "System"
     - Click on "Advanced system settings" on the right
     - Click on "Environment Variables"
     - Under "System variables", find and select "Path", then click "Edit"
     - Click "New" and add the full path to the directory containing `create-py-app.bat`
     - Click "OK" on all windows to save the changes
   
   - **macOS/Linux**:
     - Open your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`)
     - Add the following line, replacing `/path/to/create-py-app` with the actual path:
       ```
       export PATH=$PATH:/path/to/create-py-app
       ```
     - Save the file and run `source ~/.bashrc` (or the appropriate file you edited)

4. Ensure you have Python installed on your system (Python 3.6 or later is recommended).

## Usage

Once installed, you can use `create-py-app` from any directory in your terminal or command prompt.

Basic usage:
```
create-py-app your-project-name
```

This will create a new directory named `your-project-name` in the current location with the following structure:

```
your-project-name/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── __init__.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Example

```
$ cd ~/projects
$ create-py-app my-awesome-python-project
Project 'my-awesome-python-project' created successfully!
$ cd my-awesome-python-project
$ ls
README.md  requirements.txt  src  tests
```

## Customization

You can customize the project structure by modifying the `create_py_app.py` script. Feel free to add or remove files and directories according to your preferences or project requirements.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any problems or have any questions, please open an issue on the GitHub repository.

Happy coding!
