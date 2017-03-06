#!/usr/bin/env python
from hsl import app
app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
