# -*- coding: utf-8 -*-
import sys
import maya.utils
import execute_plugin_sample


def show():
    cmds.setParent('MayaWindow')
    cmds.menu(label=u'ModulePluginSample')
    cmds.menuItem(l='ExecutePluginSample',
                  c='execute_plugin_sample.hello_world()')


maya.utils.executeDeferred(show)
