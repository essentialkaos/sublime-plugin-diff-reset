import sublime, sublime_plugin

class DiffResetOnSavePlugin(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.reset_reference_document()
