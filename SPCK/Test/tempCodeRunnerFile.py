import geshi

geshi = geshi.Geshi("python")
geshi.set_code("print('Hello, world!')")
highlighted_code = geshi.highlight()
print(highlighted_code)
