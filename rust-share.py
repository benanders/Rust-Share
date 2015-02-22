import sublime, sublime_plugin
ST3 = int(sublime.version()) >= 3000
if ST3:
	from urllib.parse import quote_plus
	from urllib.request import urlopen
else:
	from urllib import quote_plus
	from urllib2 import urlopen

import json

class RustShareCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		everything = self.view.substr(sublime.Region(0, self.view.size()))
		url = "https://play.rust-lang.org/?code=" + quote_plus(everything)
		shortURL = "http://is.gd/create.php?format=json&url=" + quote_plus(url)
		contents = urlopen(shortURL).read()
		shortened = json.loads(contents.decode("utf-8"))["shorturl"]
		sublime.set_clipboard(shortened)
		if ST3:
			self.displayOutput(shortened)

	def displayOutput(self,link):
	    msg="Your Rust code has been shared online at {0}. \n\nThis link has been copied to your clipboard.\n\nPress Esc to Exit".format(link)
	    window=sublime.active_window()
	    self.output_view = window.get_output_panel("textarea")
	    window.run_command("show_panel", {"panel": "output.textarea"})
	    self.output_view.set_read_only(False)
	    self.output_view.run_command("append", {"characters": msg})
	    self.output_view.set_read_only(True)
