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
    manifests = [m.strip() for m in client_manifest.get("included_manifests", []) if m]
    if not manifests:
        manifests = ["NO INCLUDED MANIFESTS"]
    sal.add_plugin_results('Manifests', {"included_manifests": "+".join(manifests)})


if __name__ == "__main__":
    main()
