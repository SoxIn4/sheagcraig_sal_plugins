#!/usr/local/sal/Python.framework/Versions/Current/bin/python3
import pathlib

import sal

def main():
    catalogs_dir = pathlib.Path('/Library/Managed Installs/catalogs')
    catalogs = [item.stem for item in catalogs_dir.rglob('*')
                 if item.is_file()]
    if not catalogs:
        catalogs = ["NO INCLUDED CATALOGS"]
    sal.add_plugin_results('Catalogs', {"Catalogs": "+".join(catalogs)})


if __name__ == "__main__":
    main()
