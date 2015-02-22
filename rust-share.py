import sublime, sublime_plugin
import urllib.request
import urllib
import json

class RustShareCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		everything = self.view.substr(sublime.Region(0, self.view.size()))
		url = "https://play.rust-lang.org/?code=" + urllib.parse.quote_plus(everything)
		shortURL = "http://is.gd/create.php?format=json&url=" + urllib.parse.quote_plus(url)
		contents = urllib.request.urlopen(shortURL).read()
		shortened = json.loads(contents.decode("utf-8"))["shorturl"]
		sublime.set_clipboard(shortened)
