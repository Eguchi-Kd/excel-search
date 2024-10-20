import os
test_id = os.environ.get.("TEST_ID")
return render_template(index.html,TEST_ID=test_id)
