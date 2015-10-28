#!/usr/bin/python3

import sys
import os
import datetime
import operator

from jinja2 import Environment, PackageLoader

import nm

class ProfObject:

	def __init__(self, line):
		parts = line.split(" ")
		self.size = int(parts[0], 16)
		self.type = parts[1].strip()
		self.name = parts[2].strip()

	def html_row(self):
		return "<tr><td>{}</td><td>{}</td></tr>".format(self.name, self.size)

	def __gt__(self, other):
		return self.size > other.size

	def __lt__(self, other):
		return self.size < other.size

	def __eq__(self, other):
			return self.size == other.size

	def __repr__(self):
		return "{} ({})\n".format(self.name, self.size)

class Profiler:

	def __init__(self, fname, objs):
		self.full_path = fname
		self.objs = sorted(objs, reverse=True)
		self.date = datetime.datetime.now().strftime("%y-%m-%d")
		self.time = datetime.datetime.now().strftime("%H:%M:%S")
		type_sizes = {}

		for nm_type in nm.get_types():
			type_sizes[nm_type] = self.get_size_for_type(nm_type)

		self.type_sizes = sorted(type_sizes.items(), key=operator.itemgetter(1), reverse=True)

	def get_size_for_type(self, nm_type):
		size = 0
		for obj in self.objs:
			size += obj.size if obj.type == nm_type else 0

		return size

	def html_table(self, types, count=None):

		headers = "<tr><th>Name</th><th>Size</th><tr>"

		rows = [obj.html_row() for obj in self.objs if obj.type in types]

		if count is None:
			count = len(rows)

		return "<table>" + headers + ''.join(rows[:count]) + "</table>"

	def sorted_types(self):
		return self.type_sizes

	@property
	def filename(self):
	    return os.path.basename(self.full_path)
	
	@property
	def path(self):
	    return self.full_path
	
	@classmethod
	def from_objects(cls, fname, objs):
		return cls(fname, objs)

	@classmethod
	def from_file(cls, fname, f):
		objs = [ProfObject(line) for line in f]
		return cls(fname, objs)


def parse_file(fname):
	
	with open(fname, "r") as f:
		profiler = Profiler.from_file(fname, f)
		env = Environment(loader=PackageLoader('nm-printer', 'nm-templates'))
		template = env.get_template("default-template.html")
		return template.render(profiler=profiler, nm=nm)
		
if __name__ == "__main__":

	html = parse_file(sys.argv[1])

	with open(sys.argv[2], 'w') as f:
		f.write(html)
