#!/usr/local/sal/Python.framework/Versions/Current/bin/python3
import pathlib

import sal

def main():
    manifests_dir = pathlib.Path('/Library/Managed Installs/manifests')
    manifests = [item.stem for item in manifests_dir.rglob('*')
                 if item.stem != 'SelfServeManifest' and item.is_file()]
    if not manifests:
        manifests = ["NO INCLUDED MANIFESTS"]
    sal.add_plugin_results('Manifests', {"Manifests": "+".join(manifests)})


if __name__ == "__main__":
    main()
