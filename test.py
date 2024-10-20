import os
def test():
  print("テステス")
  return print(os.environ.get("TEST_ID"))#render_template(index.html,TEST_ID=os.environ.get("TEST_ID"))
test()
