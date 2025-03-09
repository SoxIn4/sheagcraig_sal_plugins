import sal.plugin
from server.models import PluginScriptRow


class MachineDetailManifests(sal.plugin.DetailPlugin):

    description = "Lists the device's manifests"

    def get_context(self, machine, **kwargs):
        context = self.super_get_context(machine, **kwargs)
        rows = (PluginScriptRow.objects
            .filter(
                submission__machine=machine,
                submission__plugin='Manifests')
             .values('pluginscript_name', 'pluginscript_data'))
        context.update({r['pluginscript_name']: r['pluginscript_data'].split('+') for r in rows})

        return context
