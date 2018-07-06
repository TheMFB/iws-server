from app import app
import sys

port = 8080
if len(sys.argv) == 2:
    port = int(sys.argv[1])

#debug set to False due to "code" module naming conflict 
app.run(host='0.0.0.0', port=port, debug=True)
