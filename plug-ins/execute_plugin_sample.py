# -*- coding: utf-8 -*-
import maya.cmds as cmds

def initialize():
    cmds.setParent('MayaWindow')
    cmds.menu(label=u'ModulePluginSample')
    cmds.menuItem(l='ExecutePluginSample',
                  c=hello_world)

def hello_world(*args):
    print("hello_world")
