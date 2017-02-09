import os
from os.path import basename
import sublime, sublime_plugin

class FilenameCommand(sublime_plugin.TextCommand):  
  def pattern(self, body):
    return ('(function(){console.log(' body '); return' body '})()' )

  def run(self, edit):
    sel = self.view.sel()

    if len(sel) > 0:
      # если выбран текст - заменяем каждый элемент
      for region in sel:
        self.view.replace(edit, region, self.pattern(region))

