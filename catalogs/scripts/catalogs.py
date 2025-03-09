#!/usr/local/sal/Python.framework/Versions/Current/bin/python3

import os
import plistlib

import sal

from Foundation import CFPreferencesCopyAppValue

def main():
    bundle_id = "ManagedInstalls"
    manifest =  CFPreferencesCopyAppValue('ClientIdentifier', bundle_id)
    client_manifest_path = f'/Library/Managed Installs/manifests/{manifest}'
    
    if os.path.exists(client_manifest_path):
        with open(client_manifest_path, 'rb') as cm:
            client_manifest = plistlib.load(cm)
    else:
        client_manifest = {}

    # Drop any blank entries and trim WS.
    catalogs = [c.strip() for c in client_manifest.get("catalogs", []) if c]
    if not catalogs:
        catalogs = ["NO CATALOGS"]
    
    sal.add_plugin_results('Catalogs', {"Catalogs": "+".join(catalogs)})

if __name__ == "__main__":
    main()
