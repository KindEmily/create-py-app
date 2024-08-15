import os
import sys
import argparse

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure(project_name):
    base_dir = os.path.join(os.getcwd(), project_name)
    
    # Create main project directory
    create_directory(base_dir)

    # Create src directory
    src_dir = os.path.join(base_dir, 'src')
    create_directory(src_dir)

    # Create tests directory
    tests_dir = os.path.join(base_dir, 'tests')
    create_directory(tests_dir)

    # Create main.py
    create_file(os.path.join(src_dir, 'main.py'), 
                'def main():\n    print("Hello, World!")\n\nif __name__ == "__main__":\n    main()')

    # Create __init__.py files
    create_file(os.path.join(src_dir, '__init__.py'))
    create_file(os.path.join(tests_dir, '__init__.py'))

    # Create requirements.txt
    create_file(os.path.join(base_dir, 'requirements.txt'))

    # Create README.md
    create_file(os.path.join(base_dir, 'README.md'), 
                f'# {project_name}\n\nA Python project created with create-py-app.')

    # Create .gitignore
    create_file(os.path.join(base_dir, '.gitignore'), 
                '*.pyc\n__pycache__\nvenv/\n.vscode/\n*.egg-info/')

    print(f"Project '{project_name}' created successfully!")

def main():
    parser = argparse.ArgumentParser(description="Create a new Python project structure.")
    parser.add_argument("project_name", help="Name of the project to create")
    args = parser.parse_args()

    create_project_structure(args.project_name)

if __name__ == "__main__":
    main()
