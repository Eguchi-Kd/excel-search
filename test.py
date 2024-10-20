import os
def test():
  print("テステス")
  return render_template(index.html,TEST_ID=os.environ.get("TEST_ID"))
