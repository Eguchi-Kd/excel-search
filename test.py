import os
def test():
  print(os.environ.get("TEST_ID"))
  return render_template(index.html,TEST_ID=os.environ.get("TEST_ID"))
