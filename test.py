import os
def test():
  print("テステス")
  return print(os.environ.get("VITE_TEST"))#render_template(index.html,TEST_ID=os.environ.get("VITE_TEST"))
test()
