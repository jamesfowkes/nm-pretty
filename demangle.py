import subprocess
import locale

def demangle_cpp_name(string):
	output = subprocess.check_output(["c++filt", string])
	output = output.decode(locale.getpreferredencoding(False)).strip()
	return output
