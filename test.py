import os
from flask import Flask, request, render_template
def test():
  print("テステス")
  return render_template(index.html,TEST_ID=os.environ.get("TEST_ID"))
test()
